#!/bin/sh

docker run --user "$(id -u):$(id -g)" --rm -v "${PWD}:/client" -v "${PWD}/../DocumentReader-web-openapi:/definitions" \
openapitools/openapi-generator-cli:v5.0.0-beta generate -g python \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates
