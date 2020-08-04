import base64
from typing import Union

from regula.documentreader.webclient.ext.models.recognition_response import RecognitionResponse
from regula.documentreader.webclient.gen import ApiClient, Configuration
from regula.documentreader.webclient.gen.api import DefaultApi
from regula.documentreader.webclient.gen.models import ProcessRequest

Base64String = str


class DocumentReaderApi(DefaultApi):

    def __init__(self, host=None, debug=False, verify_ssl=False, api_client=None):
        if api_client:
            super().__init__(api_client)
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl

            super().__init__(ApiClient(configuration=configuration))
        self.__license = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.api_client.close()

    @property
    def license(self) -> Base64String:
        return self.__license

    @license.setter
    def license(self, value: Union[Base64String, bytes]):
        if isinstance(value, bytes):
            self.__license = base64.b64encode(value).decode("utf-8")
        else:
            self.__license = value

    def process(self, process_request: ProcessRequest) -> RecognitionResponse:
        process_request.system_info.license = self.license
        return RecognitionResponse(self.api_process(process_request))
