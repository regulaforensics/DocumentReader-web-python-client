import regula.documentreader.webclient
from pprint import pprint
from regula.documentreader.webclient.api import default_api
from regula.documentreader.webclient.model import process_request

configuration = regula.documentreader.webclient.Configuration(
    host="http://localhost:8080"
)

# Enter a context with an instance of the API client
with regula.documentreader.webclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    process_request_process_request = process_request.ProcessRequest()

    try:
        # Process list of documents images and return extracted data
        api_response = api_instance.api_process(process_request_process_request)
        pprint(api_response)
    except regula.documentreader.webclient.ApiException as e:
        print("Exception when calling DefaultApi->api_process: %s\n" % e)
