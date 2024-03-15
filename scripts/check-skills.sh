#!/usr/bin/env bash

REPO_DIR=$(cd -- "$(dirname -- "$(dirname -- "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)

if [ ! $# -eq 1 ]; then
    echo "Usage: ./check-skills.sh [CHANGED_FILES] - Ensure changed Taxonomy YAML files follow proper schema"
    exit 0
else
    CHANGED_FILES=$1
    ERR=0
    error() { echo "ERROR: $file:$@" 1>&2; ERR=1; }
    warn()  { echo "WARN:  $file:$@" 1>&2; }
    echo
    for file in ${REPO_DIR}/${CHANGED_FILES}; do
        case $file in knowledge*)
            error "1:1: We do not accept knowledge PRs at this time"
        esac
        if [[ "$file" != *"/qna.yaml" ]]; then
            error "1:1: Skills file has to be named 'qna.yaml', not '$(basename $file)'"
        fi
        yq '.created_by       | length > 0'            $file | grep -q false && warn  "$(yq '.created_by|line'       $file):1: missing/empty 'created_by'"
        yq '.task_description | length > 0'            $file | grep -q false && warn  "$(yq '.task_description|line' $file):1: missing/empty 'task_description'"
        yq '.seed_examples'                            $file | grep -q null  && error "$(yq '.seed_examples|line'    $file):1: missing 'seed_examples'"
        yq '.seed_examples   | length >= 5'            $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: less than 5 'seed_examples'"
        yq '.seed_examples[] | .question | length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'question's"
        yq '.seed_examples[] | .answer   | length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'answer's"
        if $( yq '.seed_examples[] | has("context")'   $file | grep -q true ); then
            yq '.seed_examples[] | .context| length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'context's"
        fi
        yq '.seed_examples[].attribution | length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'attribution's"
        yq '.seed_examples[].attribution[].source | length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'attribution source's"
        yq '.seed_examples[].attribution[].license | length > 0' $file | grep -q false && error "$(yq '.seed_examples|line'    $file):1: missing/empty 'attribution license's"
    done
    exit $ERR
fi
