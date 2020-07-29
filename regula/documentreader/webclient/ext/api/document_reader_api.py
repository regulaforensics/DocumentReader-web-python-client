from regula.documentreader.webclient.ext.models.recognition_response import RecognitionResponse
from regula.documentreader.webclient.gen import ApiClient, Configuration
from regula.documentreader.webclient.gen.api import DefaultApi
from regula.documentreader.webclient.gen.models import ProcessRequest


class DocumentReaderApi(DefaultApi):
    __license: str

    def __init__(self, host=None, debug=False, verify_ssl=False, api_client=None):
        if api_client:
            super().__init__(api_client)
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl

            super().__init__(ApiClient(configuration=configuration))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.api_client.close()

    @property
    def license(self):
        return self.__license

    @license.setter
    def license(self, value):
        self.__license = value

    def process(self, process_request: ProcessRequest) -> RecognitionResponse:
        process_request.system_info.license = self.license
        return RecognitionResponse(self.api_process(process_request))
