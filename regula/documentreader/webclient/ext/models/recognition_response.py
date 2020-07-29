from typing import Optional

from regula.documentreader.webclient import ProcessResponse, Result, Status, Images
from regula.documentreader.webclient.ext.models.text import Text


class RecognitionResponse:
    __process_response: ProcessResponse

    def __init__(self, process_response: ProcessResponse):
        self.__process_response = process_response

    @property
    def text(self) -> Optional[Text]:
        result = self.result_by_type(Result.TEXT)
        if result:
            i = result.text
            return Text(i)
        return None

    @property
    def status(self) -> Optional[Status]:
        result = self.result_by_type(Result.STATUS)
        if result:
            return result.status
        return None

    @property
    def images(self) -> Optional[Images]:
        result = self.result_by_type(Result.IMAGES)
        if result:
            return result.images
        return None

    def result_by_type(self, result_type):
        for i in self.__process_response.container_list.list:
            if i.result_type == result_type:
                return i
        return None
