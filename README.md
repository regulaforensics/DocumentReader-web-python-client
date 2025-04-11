# Regula Document Reader web API Python 3.8+ client

[![pypi](https://img.shields.io/pypi/v/regula.documentreader.webclient?style=flat-square)](https://support.regulaforensics.com/hc/en-us/articles/115000916306-Documentation)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-defs-8c0a56?style=flat-square)](https://github.com/regulaforensics/DocumentReader-web-openapi)
[![documentation](https://img.shields.io/badge/docs-en-f6858d?style=flat-square)](https://support.regulaforensics.com/hc/en-us/articles/115000916306-Documentation)
[![live](https://img.shields.io/badge/live-demo-0a8c42?style=flat-square)](https://api.regulaforensics.com/)

## ⚠️ Warning: Package Name Changed

Package name has been changed from `regula.documentreader.webclient` to `regula_documentreader_webclient`

Documents recognition as easy as reading two bytes.

If you have any problems with or questions about this client, please contact us
through a [GitHub issue](https://github.com/regulaforensics/DocumentReader-web-python-client/issues).
You are invited to contribute [new features, fixes, or updates](https://github.com/regulaforensics/DocumentReader-web-python-client/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22), large or small;
We are always thrilled to receive pull requests, and do our best to process them as fast as we can.
See [dev guide](./dev.md)

## Install package
`regula_documentreader_webclient` is on the Python Package Index (PyPI):

```bash
pip install regula_documentreader_webclient
```

Or using `pipenv`
```bash
pipenv install regula_documentreader_webclient
```

## Example
Performing request:
```python
from regula_documentreader_webclient import *

with open("australia_passport.jpg", "rb") as f:
    input_image = f.read()

with DocumentReaderApi(host='http://localhost:8080') as api:
    params = ProcessParams(
        scenario=Scenario.FULLPROCESS,
        result_type_output=[Result.DOCUMENT_IMAGE, Result.STATUS, Result.TEXT, Result.IMAGES]
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
normalized_input_image = response.images.document_image()
portrait_field = response.images.get_field(GraphicFieldType.PORTRAIT)
portrait_from_visual = portrait_field.get_value(Source.VISUAL)
portrait_from_rfid = portrait_field.get_value(Source.RFID, original=True)
```
You can find more detailed guide and run this sample in [example](./example) folder.
