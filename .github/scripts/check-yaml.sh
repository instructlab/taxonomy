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

TAXONOMY_FOLDERS=("compositional_skills" "knowledge")
SCHEMA_BASE="$(dirname ${BASH_SOURCE[0]})/../schemas"
YAMLLINT_CONFIG="{extends: relaxed, rules: {line-length: {max: 120}}}"
CHANGED_FILES="$@"
ERR=0
if [ -z ${GITHUB_ACTIONS+x} -o -z ${GITHUB_WORKFLOW+x} ]; then
  error() { printf "ERROR: %s:%s:%s [%s] %s\n" "$1" "$2" "$3" "$4" "$5"; ERR=1; }
  warn() { printf "WARN: %s:%s:%s [%s] %s\n" "$1" "$2" "$3" "$4" "$5"; }
else
  # https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-error-message
  error() { printf "::error file=%s,line=%s,col=%s::%s:%s [%s] %s\n" "$1" "$2" "$3" "$2" "$3" "$4" "$5"; ERR=1; }
  warn() { printf "::warning file=%s,line=%s,col=%s::%s:%s [%s] %s\n" "$1" "$2" "$3" "$2" "$3" "$4" "$5"; }
fi
for file in ${CHANGED_FILES}; do
    if [ ! -f "$file" ]; then
      error "$file" "1" "1" "." "The file does not exist or is not a file"
      continue
    fi
    if [ "$(basename "$file")" != "qna.yaml" ]; then
      error "$file" "1" "1" "." "Taxonomy file must be named \"qna.yaml\"; \"$(basename "$file")\" is not a valid name"
      continue
    fi
    if ! yamllint -d "$YAMLLINT_CONFIG" "$file" ; then
      ERR=1
      continue
    fi
    schema_version=$(yq '.version // 1' "$file")
    schema_name=$(echo "$file" | cut -f1 -d/)
    if [[ ! " ${TAXONOMY_FOLDERS[*]} " =~ [[:space:]]${schema_name}[[:space:]] ]]; then
      schema_name=$(yq 'has("document") // "compositional_skills" | select(tag == "!!str") // "knowledge"' "$file")
    fi
    schema="$SCHEMA_BASE/v${schema_version}/${schema_name}.json"
    if [ ! -f "$schema" ]; then
      error "$file" "1" "1" "." "Schema \"$schema\" was not found"
      continue
    fi
    eval "$(check-jsonschema --schemafile "$schema" -o JSON "$file" | jq -r '.errors[] | (.path | ltrimstr("$") | select(. != "") // ".") as $path | "\($path)|line" as $yqline | @sh "$(yq \($yqline) \(.filename))" as $yqcmd | @sh "\(.message[-200:])" as $message | "error \"\(.filename)\" \"\($yqcmd)\" \"1\" \"\($path)\" \($message)"')"
done
exit $ERR
