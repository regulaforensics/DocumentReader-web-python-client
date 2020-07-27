# Regula's Document Reader web application python client

## Development

To regenerate models from openapi definition, 
clone [latest open api definitions](https://github.com/regulaforensics/DocumentReader-api-openapi)
and set `DEFINITION_FOLDER` as path to cloned directory, for example:
```bash
DEFINITION_FOLDER="/home/user/projects/DocumentReader-api-openapi"
```
Then use next command from the project root:
```bash
docker run --rm -v "${PWD}:/client" -v "${DEFINITION_FOLDER}:/definitions" \
openapitools/openapi-generator-cli generate -g python-experimental \
-i /definitions/index.yml -o /client -c /client/generator-config.json
```
