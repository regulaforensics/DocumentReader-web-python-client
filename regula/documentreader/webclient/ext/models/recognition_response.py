from typing import Optional, List

from regula.documentreader.webclient.ext.models.images import Images
from regula.documentreader.webclient.ext.models.text import Text
from regula.documentreader.webclient.gen import ResultItem
from regula.documentreader.webclient.gen.models.process_response import ProcessResponse
from regula.documentreader.webclient.gen.models.result import Result
from regula.documentreader.webclient.gen.models.status import Status


class RecognitionResponse:

    def __init__(self, process_response: ProcessResponse):
        self.low_lvl_response = process_response

    @property
    def text(self) -> Optional[Text]:
        result = self.result_by_type(Result.TEXT)
        if result:
            return result.text
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

    def result_by_type(self, result_type) -> Optional[ResultItem]:
        for i in self.low_lvl_response.container_list.list:
            if i.result_type == result_type:
                return i
        return None

    def results_by_type(self, result_type) -> List[ResultItem]:
        return [r for r in self.low_lvl_response.container_list.list if r.result_type == result_type]
