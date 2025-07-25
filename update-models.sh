#!/bin/sh

DOCS_DEFINITION_FOLDER="${PWD}/../DocumentReader-web-openapi" \
\
&& docker run --user "$(id -u):$(id -g)" --rm \
-v "${PWD}:/client" \
-v "$DOCS_DEFINITION_FOLDER:/definitions" \
openapitools/openapi-generator-cli:v7.13.0 generate \
-g python \
-i /definitions/index.yml \
-o /client \
-t /client/generator-templates \
-c /client/generator-config.json || exit 1
