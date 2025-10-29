from typing import Union

from regula.documentreader.webclient import ProcessResponse
from regula.documentreader.webclient.gen import ApiClient
from regula.documentreader.webclient.ext.models.recognition_response import RecognitionResponse
from regula.documentreader.webclient.gen.api import HealthcheckApi, ProcessApi, ResourcesApi, TransactionApi
from regula.documentreader.webclient.gen.configuration import Configuration
from regula.documentreader.webclient.gen.models import ProcessRequest

Base64String = str


class DocumentReaderApi(HealthcheckApi, ProcessApi, ResourcesApi, TransactionApi):

    def __init__(self, host=None, debug=False, verify_ssl=True, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl
            self.api_client = ApiClient(configuration=configuration)
        super().__init__(self.api_client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def set_configuration(self, configuration) -> None:
        self.api_client.configuration = configuration

    def process(self, process_request: ProcessRequest) -> RecognitionResponse:
        return RecognitionResponse(self.api_process(process_request))

    def deserialize_to_recognition_response(self, content: Union[bytes, bytearray, str]) -> RecognitionResponse:
        response = self.__to_response_object(content)

        if hasattr(response, 'to_str'):
            response_text = response.to_str()
        elif hasattr(response, 'data'):
            data = response.data
            if isinstance(data, (bytes, bytearray)):
                response_text = data.decode('utf-8')
            else:
                response_text = str(data)
        else:
            response_text = str(content) if not isinstance(content, str) else content

        content_type = "application/json"
        process_response = self.api_client.deserialize(response_text, "ProcessResponse", content_type)

        return RecognitionResponse(process_response)

    @staticmethod
    def __to_response_object(content: Union[bytes, bytearray, str]):
        return type(ProcessResponse.__name__, (object,), {"data": content})()
