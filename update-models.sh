#!/bin/sh

MODE="$1"
DOCS_DEFINITION_FOLDER="${PWD}/../DocumentReader-web-openapi"
TEMPLATE_PATH="/client/generator-templates/lenient"

if [ "$MODE" = "strict" ]; then
    TEMPLATE_PATH="/client/generator-templates/strict"
fi

docker run --user "$(id -u):$(id -g)" --rm \
-v "${PWD}:/client" \
-v "$DOCS_DEFINITION_FOLDER:/definitions" \
openapitools/openapi-generator-cli:v7.15.0 generate \
-g python \
-i /definitions/index.yml \
-o /client \
-t $TEMPLATE_PATH \
-c /client/generator-config.json || exit 1
