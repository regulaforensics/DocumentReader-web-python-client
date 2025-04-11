from typing import List, cast

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, PhotoIdentResult


class ImageIdentChecks(AuthenticityCheckResult):

    @property
    def checks_list(self) -> List[PhotoIdentResult]:
        image_ident_list: List[PhotoIdentResult] = cast(List[PhotoIdentResult], self.list)
        return image_ident_list
