import os

from regula.documentreader.webclient import *

host = os.getenv("API_BASE_PATH", "http://localhost:8080")
regula_license = os.getenv("TEST_LICENSE", None)  # optional, used here only for smoke test purposes

# read optional local license file
if os.path.isfile('regula.license') and os.access('regula.license', os.R_OK):
    with open("regula.license", "rb") as f:
        print("Found local license file. Using it for performing request...")
        regula_license = f.read()

with open("WHITE.jpg", "rb") as f:
    white_page_0 = f.read()

with open("IR.jpg", "rb") as f:
    ir_page_0 = f.read()

with open("UV.jpg", "rb") as f:
    uv_page_0 = f.read()

with DocumentReaderApi(host) as api:
    api.license = regula_license

    params = ProcessParams(
        scenario=Scenario.FULL_AUTH,
        result_type_output=[
            # actual results
            Result.STATUS, Result.AUTHENTICITY, Result.TEXT, Result.IMAGES,
            Result.DOCUMENT_TYPE, Result.DOCUMENT_TYPE_CANDIDATES,
            # legacy results
            Result.MRZ_TEXT, Result.VISUAL_TEXT, Result.BARCODE_TEXT, Result.RFID_TEXT,
            Result.VISUAL_GRAPHICS, Result.BARCODE_GRAPHICS, Result.RFID_GRAPHICS,
            Result.LEXICAL_ANALYSIS
        ]
    )
    request = RecognitionRequest(process_params=params, images=[
        RecognitionImage(image=white_page_0, light_index=Light.WHITE, page_index=0),
        RecognitionImage(image=ir_page_0, light_index=Light.IR, page_index=0),
        RecognitionImage(image=uv_page_0, light_index=Light.UV, page_index=0),
    ])
    response = api.process(request)

    # status examples
    response_status = response.status
    doc_overall_status = "valid" if response_status.overall_status == CheckResult.OK else "not valid"

    # text fields example
    doc_number_field = response.text.get_field(TextFieldType.DOCUMENT_NUMBER)
    doc_number_field_by_name = response.text.get_field_by_name("Document Number")

    doc_number_mrz = doc_number_field.get_value()
    doc_number_visual = doc_number_field.get_value(Source.VISUAL)
    doc_number_visual_validity = doc_number_field.source_validity(Source.VISUAL)
    doc_number_mrz_validity = doc_number_field.source_validity(Source.MRZ)
    doc_number_mrz_visual_matching = doc_number_field.cross_source_comparison(Source.MRZ, Source.VISUAL)

    # images fields example
    document_image = response.images.get_field(GraphicFieldType.DOCUMENT_FRONT).get_value()
    portrait_from_visual = response.images.get_field(GraphicFieldType.PORTRAIT).get_value(Source.VISUAL)
    with open('portrait.jpg', 'wb') as f:
        f.write(portrait_from_visual)
    with open('document-image.jpg', 'wb') as f:
        f.write(document_image)

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
