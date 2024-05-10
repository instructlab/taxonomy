import yaml
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Validate the YAML file keys")
    parser.add_argument("yaml_file", help="A qna.yaml file.", nargs="+", type=Path )

    args = parser.parse_args()

    yaml_files = args.yaml_file

    errors = 0

    for file in yaml_files:
        data = yaml.safe_load(file.read_text())

        if data['created_by'] is None:
            print("You are missing a created_by")
            errors += 1

        if data['domain'] is None:
            print("You are missing a domain")
            errors += 1

        if data['seed_examples'] is None:
            print("You are missing seed_examples")
            errors += 1

        if data['task_description'] is None:
            print("You are missing task_description")
            errors += 1

        if data['document'] is None:
            print("You are missing a document")
            errors += 1

        if data['document']['repo'] is None:
            print("You are missing a document repo")
            errors += 1

        if data['document']['commit'] is None:
            print("You are missing a document commit")
            errors += 1

        if data['document']['patterns'] is None:
            print("You are missing a document files/patterns")
            errors += 1

    if errors > 0:
        exit(1)
    else:
        exit(0)


if __name__ == '__main__':
    main()
