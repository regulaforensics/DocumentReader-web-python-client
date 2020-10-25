# Development

To regenerate models, clone [latest OpenAPI definitions](https://github.com/regulaforensics/DocumentReader-web-openapi)
and set `DEFINITION_FOLDER` as path to cloned directory, for example:
```bash
export DOCS_DEFINITION_FOLDER="/home/user/projects/DocumentReader-web-openapi"
```
Then use next command from the project root:
```bash
./update-models.sh
```
