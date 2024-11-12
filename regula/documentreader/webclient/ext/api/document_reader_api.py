import base64
from typing import Union

from regula.documentreader.webclient import ProcessResponse
from regula.documentreader.webclient.gen import ApiClient
from regula.documentreader.webclient.ext.models.recognition_response import RecognitionResponse
from regula.documentreader.webclient.gen.api import HealthcheckApi, ProcessApi
from regula.documentreader.webclient.gen.configuration import Configuration
from regula.documentreader.webclient.gen.models import ProcessRequest

Base64String = str


class DocumentReaderApi(HealthcheckApi, ProcessApi):

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

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.api_client.close()

    def set_configuration(self, configuration) -> None:
        self.api_client.configuration = configuration

    def process(self, process_request: ProcessRequest) -> RecognitionResponse:
        return RecognitionResponse(self.api_process(process_request))

    def deserialize_to_recognition_response(self, content: Union[bytes, bytearray, str]) -> RecognitionResponse:
        response = self.__to_response_object(content)
        response = self.api_client.deserialize(response, ProcessResponse)
        return RecognitionResponse(response)

    @staticmethod
    def __to_response_object(content: Union[bytes, bytearray, str]):
        return type(ProcessResponse.__name__, (object,), {"data": content})()
