#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

# Standard
import argparse
import json
import os
import subprocess
import sys
from functools import cache, partial
from importlib.resources.abc import Traversable
from pathlib import Path
from typing import List, Optional, Union

# Third Party
import yaml
from jsonschema.protocols import Validator
from jsonschema.validators import validator_for
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012
from referencing.typing import URI
from yamllint import linter
from yamllint.config import YamlLintConfig


class CheckYaml:
    def __init__(
        self,
        *,
        yaml_files: List[Path],
        schema_base: Path,
        taxonomy_folders: List[str],
        yamllint_config: YamlLintConfig,
        message_format: Optional[str] = None,
    ) -> None:
        self.yaml_files = yaml_files
        self.schema_base = schema_base
        self.taxonomy_folders = taxonomy_folders
        self.yamllint_config = yamllint_config
        if message_format is None or message_format == "auto":
            message_format = (
                "github"
                if "GITHUB_ACTIONS" in os.environ and "GITHUB_WORKFLOW" in os.environ
                else "standard"
            )
        self.message_format = message_format
        self.exit_code: int = 0

    @cache
    def _load_schema(self, path: Union[Path, Traversable]) -> Resource:
        try:
            contents = json.loads(path.read_text(encoding="utf-8"))
            resource = Resource.from_contents(
                contents=contents, default_specification=DRAFT202012
            )
        except Exception as e:
            raise NoSuchResource(ref=str(path)) from e
        return resource

    def _retrieve(self, schemas_path: Union[Path, Traversable], uri: URI) -> Resource:
        path = schemas_path.joinpath(uri)
        return self._load_schema(path)

    def error(
        self,
        file: Union[str, Path],
        message: str,
        line: Union[str, int] = 1,
        col: Union[str, int] = 1,
        yaml_path: Optional[str] = None,
    ) -> None:
        if yaml_path:
            message = f"[{yaml_path}] {message}"
        match self.message_format:
            case "github":
                print(
                    f"::error file={file},line={line},col={col}::{line}:{col} {message}"
                )
            case "standard" | _:
                print(f"ERROR: {file}:{line}:{col} {message}")
        self.exit_code = 1

    def warning(
        self,
        file: Union[str, Path],
        message: str,
        line: Union[str, int] = 1,
        col: Union[str, int] = 1,
        yaml_path: Optional[str] = None,
    ) -> None:
        if yaml_path:
            message = f"[{yaml_path}] {message}"
        match self.message_format:
            case "github":
                print(
                    f"::warning file={file},line={line},col={col}::{line}:{col} {message}"
                )
            case "standard" | _:
                print(f"WARN: {file}:{line}:{col} {message}")

    def check(self) -> int:
        for file in self.yaml_files:
            full_path = file.resolve()
            for i in range(len(full_path.parts) - 1, -1, -1):
                if full_path.parts[i] in self.taxonomy_folders:
                    taxonomy_path = Path(*full_path.parts[i:])
                    break
            else:
                taxonomy_path = full_path

            if not os.path.isfile(full_path):
                self.error(
                    file=full_path,
                    message="The file does not exist or is not a file",
                )
                continue

            if taxonomy_path.name != "qna.yaml":
                self.error(
                    file=taxonomy_path,
                    message=f'Taxonomy file must be named "qna.yaml"; "{taxonomy_path.name}" is not a valid name',
                )
                continue

            try:
                with open(full_path, "r", encoding="utf-8") as stream:
                    content = stream.read()

                lint_error = False
                for lint_problem in linter.run(
                    input=content, conf=self.yamllint_config
                ):
                    message = (
                        f"{lint_problem.desc} ({lint_problem.rule})"
                        if lint_problem.rule
                        else lint_problem.desc
                    )
                    match lint_problem.level:
                        case "error":
                            self.error(
                                file=taxonomy_path,
                                message=message,
                                line=lint_problem.line,
                                col=lint_problem.column,
                            )
                            lint_error = True
                        case _:
                            self.warning(
                                file=taxonomy_path,
                                message=message,
                                line=lint_problem.line,
                                col=lint_problem.column,
                            )
                if lint_error:
                    continue

                parsed = yaml.safe_load(content)
                if not parsed:
                    self.error(file=taxonomy_path, message="The file is empty")
                    continue

                version = parsed.get("version", 1)
                if not isinstance(version, int):
                    # schema validation will complain about the type
                    try:
                        version = int(version)
                    except ValueError:
                        version = 1  # fallback to version 1

                schemas_path = self.schema_base.joinpath(f"v{version}")
                retrieve = partial(self._retrieve, schemas_path)

                schema_name = taxonomy_path.parts[0]
                if schema_name not in self.taxonomy_folders:
                    schema_name = (
                        "knowledge" if "document" in parsed else "compositional_skills"
                    )

                try:
                    schema_resource = retrieve(f"{schema_name}.json")
                    schema = schema_resource.contents
                    validator_cls = validator_for(schema)
                    validator: Validator = validator_cls(
                        schema, registry=Registry(retrieve=retrieve)
                    )

                    for validation_error in validator.iter_errors(parsed):
                        yaml_path = validation_error.json_path[1:]
                        if not yaml_path:
                            yaml_path = "."
                        try:
                            yq_expression = f"{yaml_path} | line"
                            line = subprocess.check_output(
                                ["yq", yq_expression], input=content, text=True
                            )
                            line = line.strip() if line else 1
                        except (subprocess.SubprocessError, FileNotFoundError) as e:
                            line = 1
                            self.warning(
                                file=taxonomy_path,
                                message=f"could not run yq command: {e}",
                            )
                        match validation_error.validator:
                            # Special handling for minItems which can have a long message for seed_examples
                            case "minItems":
                                message = f"Value must have at least {validation_error.validator_value} items"
                            case _:
                                message = validation_error.message[-200:]
                        self.error(
                            file=taxonomy_path,
                            message=message,
                            line=line,
                            yaml_path=yaml_path,
                        )
                except NoSuchResource as e:
                    self.error(
                        file=taxonomy_path,
                        message=f"Cannot load schema file {e.ref}. {e}",
                    )

                attribution_path = full_path.with_name("attribution.txt")
                if not os.path.isfile(attribution_path):
                    self.error(
                        file=taxonomy_path,
                        message=f"The {attribution_path.name} file does not exist or is not a file",
                    )
                elif os.path.getsize(attribution_path) == 0:
                    self.error(
                        file=taxonomy_path.with_name(attribution_path.name),
                        message="The file must be non-empty",
                    )

            except Exception as e:
                self.exit_code = 1
                raise SystemExit(self.exit_code) from e

        return self.exit_code


def cli() -> int:
    parser = argparse.ArgumentParser(
        description="Check Taxonomy YAML files for linting and schema validation.",
    )
    parser.add_argument(
        "-t",
        "--taxonomy-folder",
        action="append",
        metavar="TAXONOMY_FOLDER",
        dest="taxonomy_folders",
        help="""
            A taxonomy folder. This argument can be specified multiple times.
            Alternately, the TAXONOMY_FOLDERS environment variable can be used
            to specify a space-separated list of folders.
            """,
        default=os.environ.get(
            "TAXONOMY_FOLDERS", "compositional_skills knowledge"
        ).split(),
    )
    parser.add_argument(
        "-s",
        "--schema-base",
        help="""
            The base directory of the Taxonomy schema files.
            Alternately, the SCHEMA_BASE environment variable can be used
            to specify the base directory.
            """,
        default=os.environ.get("SCHEMA_BASE", _find_schema_base()),
        type=Path,
    )
    parser.add_argument(
        "-l",
        "--lint-config",
        dest="yamllint_config",
        help="""
            The yamllint configuration data.
            Alternately, the YAMLLINT_CONFIG environment variable can be used
            to specify the configuration data.
            """,
        default=os.environ.get(
            "YAMLLINT_CONFIG", "{extends: relaxed, rules: {line-length: {max: 120}}}"
        ),
        type=YamlLintConfig,
    )
    parser.add_argument(
        "-f",
        "--format",
        help="The message format.",
        dest="message_format",
        choices=["standard", "github", "auto"],
        default="auto",
    )
    parser.add_argument(
        "yaml_file",
        help="A qna.yaml file.",
        nargs="+",
        type=Path,
    )
    args = parser.parse_args()

    check_yaml = CheckYaml(
        yaml_files=args.yaml_file,
        taxonomy_folders=args.taxonomy_folders,
        yamllint_config=args.yamllint_config,
        schema_base=args.schema_base,
        message_format=args.message_format,
    )
    exit_code = check_yaml.check()
    return exit_code


def _find_schema_base() -> Path:
    for parent in Path(sys.argv[0]).parents:
        candidate = parent.joinpath("schema")
        if os.path.isdir(candidate):
            return candidate
        if os.path.exists(parent.joinpath(".git")):
            break
    return Path.cwd().joinpath("schema")


if __name__ == "__main__":
    sys.exit(cli())
