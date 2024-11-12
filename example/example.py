import os

from regula.documentreader.webclient import *

host = os.getenv("API_BASE_PATH", "https://api.regulaforensics.com")
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
    api.api_client.default_headers = {
        "X-CLIENT-KEY": "123",
        "Authorization": "Bearer 123"
    }
    params = ProcessParams(already_cropped=True, scenario=Scenario.FULL_PROCESS)

    # Add license to request
    # request = RecognitionRequest(system_info=ProcessSystemInfo(license=base64.b64encode(regula_license).decode()), process_params=params, images=[
    #     RecognitionImage(image=white_page_0, light_index=Light.WHITE, page_index=0),
    # ])

    request = RecognitionRequest(process_params=params, images=[
        RecognitionImage(image=white_page_0, light_index=Light.WHITE, page_index=0),
        # RecognitionImage(image=ir_page_0, light_index=Light.IR, page_index=0),
        # RecognitionImage(image=uv_page_0, light_index=Light.UV, page_index=0),
    ])
    response = api.process(request)

    request_json = request.json   # example for request & response raw json
    response_json = response.json

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

    doc_authenticity = response.authenticity()

    doc_ir_b900 = doc_authenticity.ir_b900_checks \
        if doc_authenticity is not None else None
    #                                                      if FULL_PROCESS then auth is None

    doc_ir_b900_blank = doc_ir_b900.checks_by_element(SecurityFeatureType.BLANK) \
        if doc_authenticity is not None else None

    doc_image_pattern = doc_authenticity.image_pattern_checks \
        if doc_authenticity is not None else None

    doc_image_pattern_blank = doc_image_pattern.checks_by_element(SecurityFeatureType.BLANK) \
        if doc_authenticity is not None else None

    # images fields example
    document_image = response.images.get_field(GraphicFieldType.DOCUMENT_FRONT).get_value()
    portrait_from_visual = response.images.get_field(GraphicFieldType.PORTRAIT).get_value(Source.VISUAL)
    with open('portrait.jpg', 'wb') as f:
        f.write(portrait_from_visual)
    with open('document-image.jpg', 'wb') as f:
        f.write(document_image)
    print(f"""
    ---------------------------------------------------------------------------
                        Web API version: {api.ping().version}
    ---------------------------------------------------------------------------
                    Document Overall Status: {doc_overall_status}
                    Document Number Visual: {doc_number_visual}
                    Document Type: {response.result_by_type(result_type=Result.DOCUMENT_TYPE).one_candidate.document_name}
                    Validity Of Document Number Visual: {doc_number_visual_validity}
    """)

    print("-----------------------All Text Fields------------------------")
    for field in response.text.field_list:
        print(f"Source: {field.field_name}, Value: {field.value}")
