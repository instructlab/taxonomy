#!/usr/bin/env bash
# Copyright The InstructLab Authors, 2024
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

if [ $# -lt 1 ]; then
    echo "Usage: check-yaml.sh [CHANGED_FILES] - Ensure changed Taxonomy YAML files follow proper schema"
    exit 1
fi

SCHEMA_VERSION=1
SCHEMAS="$(dirname ${BASH_SOURCE[0]})/../schemas/v${SCHEMA_VERSION}"
CHANGED_FILES="$@"
ERR=0
error() { printf "ERROR: %s: %s \"%s\"\n" "$1" "$2" "$3" 1>&2; ERR=1; }
warn() { printf "WARN: %s: %s \"%s\"\n" "$1" "$2" "$3" 1>&2; }
for file in ${CHANGED_FILES}; do
    case $file in 
      compositional_skills/*/qna.yaml)
        eval "$(check-jsonschema --schemafile $SCHEMAS/compositional_skills.json -o JSON $file | jq -r '.errors[] | (.path | ltrimstr("$") | select(. != "") // ".") as $path | "\($path)|line" as $yqline | @sh "$(yq \($yqline) \(.filename))" as $yqcmd | @sh "\(.message[-200:])" as $message | "error \"\(.filename):\($yqcmd):1\" \"\($path)\" \($message)"')"
        ;;
      knowledge/*/qna.yaml)
        eval "$(check-jsonschema --schemafile $SCHEMAS/knowledge.json -o JSON $file | jq -r '.errors[] | (.path | ltrimstr("$") | select(. != "") // ".") as $path | "\($path)|line" as $yqline | @sh "$(yq \($yqline) \(.filename))" as $yqcmd | @sh "\(.message[-200:])" as $message | "error \"\(.filename):\($yqcmd):1\" \"\($path)\" \($message)"')"
        ;;
      *)
        error "$file:1:1" "." "Taxonomy file must be named 'qna.yaml', not '$(basename $file)'"
        ;;
    esac
done
exit $ERR
