import base64

import regula.documentreader.webclient
from pprint import pprint
from regula.documentreader.webclient.api import default_api
from regula.documentreader.webclient.models.image_data import ImageData
from regula.documentreader.webclient.models.process_request import ProcessRequest
from regula.documentreader.webclient.models.process_params import ProcessParams
from regula.documentreader.webclient.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.models.result import Result
from regula.documentreader.webclient.models.scenario import Scenario

configuration = regula.documentreader.webclient.Configuration(
    host="http://localhost:8080", discard_unknown_keys = True
)

with open("australia_passport.jpg", "rb") as image_file:
    input_image_as_base64 = base64.b64encode(image_file.read()).decode('utf-8')

image = ProcessRequestImage(image_data=ImageData(image=input_image_as_base64))

# Enter a context with an instance of the API client
with regula.documentreader.webclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    process_request_process_request = ProcessRequest(
        list=[image],
        process_param=ProcessParams(
            scenario=Scenario.FULL_PROCESS, result_type_output=[Result.TEXT, Result.IMAGES]
        )
    )

    try:
        # Process list of documents images and return extracted data
        api_response = api_instance.api_process(process_request_process_request)
        pprint(api_response)
    except regula.documentreader.webclient.ApiException as e:
        print("Exception when calling DefaultApi->api_process: %s\n" % e)
