#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

# Standard
import argparse
import os
import pathlib
import sys

# Third Party
from instructlab.schema.taxonomy import TaxonomyParser


class CheckYaml:
    def __init__(
        self,
        *,
        yaml_files: list[pathlib.Path],
        taxonomy_folders: list[str] | None = None,
        yamllint_config: str | None = None,
        schema_version: int | None = None,
        message_format: str | None = None,
    ) -> None:
        self.yaml_files = yaml_files
        self.taxonomy_folders = taxonomy_folders
        self.yamllint_config = yamllint_config
        self.schema_version = schema_version
        self.message_format = message_format

    def check(self) -> int:
        exit_code: int = 0
        parser = TaxonomyParser(
                    taxonomy_folders=self.taxonomy_folders,
                    schema_version=self.schema_version,
                    message_format=self.message_format,
                    yamllint_config=self.yamllint_config,
                )
        for file in self.yaml_files:
            taxonomy = parser.parse(file)
            if taxonomy.version > 1:
                attribution_path = taxonomy.rel_path.with_name("attribution.txt")
                if not attribution_path.is_file():
                    taxonomy.error(
                        "The \"%s\" file does not exist or is not a file",
                        attribution_path.name,
                    )
                elif os.path.getsize(attribution_path) == 0:
                    taxonomy.error(
                        "The \"%s\" file must be non-empty",
                        taxonomy.path.with_name(attribution_path.name),
                    )
            if taxonomy.errors > 0:
                exit_code = 1
        if not self.yaml_files:
            print("No yaml files specified.")
        return exit_code


def cli() -> int:
    parser = argparse.ArgumentParser(
        description="""
        Check Taxonomy YAML files for linting and schema validation.
        """,
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
        default=os.environ.get("TAXONOMY_FOLDERS"),
    )
    parser.add_argument(
        "-v",
        "--schema-version",
        help="""
            The version of the Taxonomy schema.
            Alternately, the SCHEMA_VERSION environment variable can be used
            to specify the version.
            Specifying a version less than 1 will use the schema version
            specified by each YAML document's "version" key.
            If not specified, the highest schema version is used.
            """,
        default=os.environ.get("SCHEMA_VERSION"),
        type=int,
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
        default=os.environ.get("YAMLLINT_CONFIG"),
    )
    parser.add_argument(
        "-f",
        "--format",
        help="The message format.",
        dest="message_format",
        choices=["standard", "github", "auto"],
        default=None,
    )
    parser.add_argument(
        "yaml_file",
        help="A qna.yaml file.",
        nargs="*",
        type=pathlib.Path,
    )
    args = parser.parse_args()

    taxonomy_folders = args.taxonomy_folders
    if isinstance(taxonomy_folders, str):
        taxonomy_folders = taxonomy_folders.split()
    check_yaml = CheckYaml(
        yaml_files=args.yaml_file,
        taxonomy_folders=taxonomy_folders,
        yamllint_config=args.yamllint_config,
        schema_version=args.schema_version,
        message_format=args.message_format,
    )
    exit_code = check_yaml.check()
    return exit_code


if __name__ == "__main__":
    sys.exit(cli())
