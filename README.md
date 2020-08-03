# Regula Document Reader web API Python 3.5+ client

[![pypi](https://img.shields.io/pypi/v/regula.documentreader.webclient?style=flat-square)](https://support.regulaforensics.com/hc/en-us/articles/115000916306-Documentation)
[![documentation](https://img.shields.io/badge/docs-en-f6858d?style=flat-square)](https://support.regulaforensics.com/hc/en-us/articles/115000916306-Documentation)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-defs-0a8c42?style=flat-square)](https://github.com/regulaforensics/DocumentReader-web-openapi)

Documents recognition as easy as reading two bytes.

If you have any problems with or questions about this client, please contact us
through a [GitHub issue](https://github.com/regulaforensics/DocumentReader-web-python-client/issues).
You are invited to contribute [new features, fixes, or updates](https://github.com/regulaforensics/DocumentReader-web-python-client/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22), large or small; We are always thrilled to receive pull requests, and do our best to process them as fast as we can.

## Install package
`regula.documentreader.webclient` is on the Python Package Index (PyPI):

```bash
pip install regula.documentreader.webclient
```

Or using `pipenv`
```bash
pipenv install regula.documentreader.webclient
```

## Example
Performing request:
```python
from regula.documentreader.webclient.ext.api import DocumentReaderApi
from regula.documentreader.webclient.ext.models import *
from regula.documentreader.webclient.gen.models import *

with open("australia_passport.jpg", "rb") as f:
    input_image = f.read()

with DocumentReaderApi(host='http://localhost:8080') as api:
    params = ProcessParams(
        scenario=Scenario.FULL_PROCESS,
        result_type_output=[Result.RAW_IMAGE, Result.STATUS, Result.TEXT, Result.IMAGES]
    )
    request = RecognitionRequest(process_params=params, images=[input_image])
    response = api.process(request)
```

Parsing results:
```python
# status examples
response_status = response.status
doc_overall_status = "valid" if response_status.overall_status == CheckResult.OK else "not valid"

# text fields example
doc_number_field = response.text.get_field(TextFieldType.DOCUMENT_NUMBER)
doc_number_mrz = doc_number_field.get_value()
doc_number_visual = doc_number_field.get_value(Source.VISUAL)
doc_number_visual_validity = doc_number_field.source_validity(Source.VISUAL)
doc_number_mrz_validity = doc_number_field.source_validity(Source.MRZ)
doc_number_mrz_visual_matching = doc_number_field.cross_source_comparison(Source.MRZ, Source.VISUAL)

# images fields example
normalized_input_image = response.images.normalized_input_image()
portrait_field = response.images.get_field(GraphicFieldType.PORTRAIT)
portrait_from_visual = portrait_field.get_value(Source.VISUAL)
portrait_from_rfid = portrait_field.get_value(Source.RFID, original=True)
```
You can find more detailed guide and run this sample in [example](./example) folder.

## Development

To regenerate models, clone [latest OpenAPI definitions](https://github.com/regulaforensics/DocumentReader-web-openapi)
and set `DEFINITION_FOLDER` as path to cloned directory, for example:
```bash
DEFINITION_FOLDER="/home/user/projects/DocumentReader-web-openapi"
```
Then use next command from the project root:
```bash
docker run --rm -v "${PWD}:/client" -v "${DEFINITION_FOLDER}:/definitions" \
openapitools/openapi-generator-cli generate -g python \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates
```
