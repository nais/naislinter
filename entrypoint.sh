#!/bin/bash

if [ -z "$TEAM" ]; then
    export TEAM="bogus-owner"
fi

if [ -z "$OWNER" ]; then
    OWNER=$(echo "$GITHUB_REPOSITORY" | cut -f1 -d/)
    export OWNER=$OWNER
fi

if [ -z "$REPOSITORY" ]; then
    REPOSITORY=$(echo "$GITHUB_REPOSITORY" | cut -f2 -d/)
    export REPOSITORY="$REPOSITORY"
fi

if [ -z "$REF" ]; then
    export REF="$GITHUB_REF"
fi

# Inject "image" as a template variable to a new copy of the vars file.
# If the file doesn't exist, it is created. The original file is left untouched.
if [ -n "$IMAGE" ]; then
    export VARS_ORIGINAL="$VARS"
    VARS=$(mktemp)
    export VARS="$VARS"
    if [ -z "$VARS_ORIGINAL" ]; then
        echo "---" > "$VARS"
    else
        cat "$VARS_ORIGINAL" > "$VARS"
    fi
    yq w --inplace "$VARS" image "$IMAGE"
fi

export TEMP_RESOURCE="$RESOURCE"

for x in ${TEMP_RESOURCE//,/ }; do
    RESOURCE=$x
    echo "Linting $x"
    /app/deploy --dry-run --print-payload --quiet | jq -c .resources[0] > nais.lint
    naislinter nais.lint
    echo
done