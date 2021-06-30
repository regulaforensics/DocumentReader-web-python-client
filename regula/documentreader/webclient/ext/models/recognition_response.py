from typing import Optional, List
from regula.documentreader.webclient import ImageQualityCheckList
from regula.documentreader.webclient.ext.models.authenticity.authenticity_check_list import AuthenticityCheckList
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

    def authenticity(self, page_idx=0) -> Optional[AuthenticityCheckList]:
        result = self.pageable_result_by_type(Result.AUTHENTICITY, page_idx)
        if result:
            return result.authenticity_check_list
        return None

    def image_quality_checks(self, page_idx=0) -> Optional[ImageQualityCheckList]:
        result = self.pageable_result_by_type(Result.IMAGE_QUALITY, page_idx)
        return result.image_quality_check_list if result is not None else None

    def pageable_result_by_type(self, result_type: int, page_idx: int) -> Optional[ResultItem]:
        container_list = self.low_lvl_response.container_list.list
        for response in container_list:
            if response.result_type == result_type and response.page_idx == page_idx:
                return response
        return None

    def result_by_type(self, result_type: int) -> Optional[ResultItem]:
        container_list = self.low_lvl_response.container_list.list
        for response in container_list:
            if response.result_type == result_type:
                return response
        return None

    def results_by_type(self, result_type) -> List[ResultItem]:
        return [r for r in self.low_lvl_response.container_list.list if r.result_type == result_type]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RecognitionResponse):
            return False
        return self.low_lvl_response == other.low_lvl_response
