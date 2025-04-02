from typing import List

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, PhotoIdentResult


class ImageIdentChecks(AuthenticityCheckResult):

    @property
    def list(self) -> List[PhotoIdentResult]:
        # noinspection PyTypeChecker
        return self.list
