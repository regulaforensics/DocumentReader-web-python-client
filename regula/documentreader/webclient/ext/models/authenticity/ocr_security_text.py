from typing import List

from regula.documentreader.webclient import gen


class OCRSecurityTextChecks(gen.AuthenticityCheckResult):

    @property
    def list(self) -> List[gen.OCRSecurityTextResult]:
        # noinspection PyTypeChecker
        return super().list
