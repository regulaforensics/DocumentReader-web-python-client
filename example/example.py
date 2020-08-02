import os

from regula.documentreader.webclient.ext.api import DocumentReaderApi
from regula.documentreader.webclient.ext.models import RecognitionRequest
from regula.documentreader.webclient.gen.models import ProcessParams, Scenario, Result, TextFieldType, Source, \
    CheckResult, GraphicFieldType

host = os.getenv("API_BASE_PATH", "http://localhost:8080")
license = os.getenv("TEST_LICENSE", None)  # optional, used here only for smoke test purposes

with open("australia_passport.jpg", "rb") as f:
    input_image = f.read()

with DocumentReaderApi(host) as api:
    api.license = license  # used here only for smoke test purposes, most of clients will attach license on server side

    params = ProcessParams(
        scenario=Scenario.FULL_PROCESS,
        result_type_output=[Result.RAW_IMAGE, Result.STATUS, Result.TEXT, Result.IMAGES]
    )
    request = RecognitionRequest(process_params=params, images=[input_image])
    response = api.process(request)

    # status examples
    response_status = response.status
    doc_overall_status = "valid" if response_status.overall_status == CheckResult.OK else "not valid"

    # text fields example
    doc_number_field = response.text.get_field(TextFieldType.DOCUMENT_NUMBER)
    doc_number_visual = doc_number_field.get_value()
    doc_number_mrz = doc_number_field.get_value(Source.MRZ)
    doc_number_visual_validity = doc_number_field.source_validity(Source.VISUAL)
    doc_number_mrz_validity = doc_number_field.source_validity(Source.MRZ)
    doc_number_mrz_visual_matching = doc_number_field.cross_source_comparison(Source.MRZ, Source.VISUAL)

    # images fields example
    normalized_input_image = response.images.normalized_input_image()
    portrait_Field = response.images.get_field(GraphicFieldType.PORTRAIT)
    portrait_From_Visual = portrait_Field.get_value(Source.VISUAL)
    with open('portraitFromVisual.jpg', 'wb') as f: f.write(portrait_From_Visual)
    with open('normalizedInputImage.jpg', 'wb') as f: f.write(normalized_input_image)

    # low-lvl(original) response
    response.low_lvl_response

    print("""
    ---------------------------------------------------------------------------
                   Document Overall Status: {doc_overall_status}
                    Document Number Visual: {doc_number_visual}
                       Document Number MRZ: {doc_number_mrz}
        Validity Of Document Number Visual: {doc_number_visual_validity}
           Validity Of Document Number MRZ: {doc_number_mrz_validity}
              MRZ-Visual values comparison: {doc_number_mrz_visual_matching}
    ---------------------------------------------------------------------------
    """.format(
        doc_overall_status=doc_overall_status, doc_number_visual=doc_number_visual,
        doc_number_mrz=doc_number_mrz, doc_number_visual_validity=doc_number_mrz_validity,
        doc_number_mrz_validity=doc_number_mrz_validity, doc_number_mrz_visual_matching=doc_number_mrz_visual_matching,
    ))
