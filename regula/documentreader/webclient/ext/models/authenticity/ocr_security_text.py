from typing import List

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, OCRSecurityTextResult


class OCRSecurityTextChecks(AuthenticityCheckResult):

    @property
    def list(self) -> List[OCRSecurityTextResult]:
        # noinspection PyTypeChecker
        return self.list
