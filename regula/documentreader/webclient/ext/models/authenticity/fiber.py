from typing import List

from regula.documentreader.webclient.gen.models import FiberResult, AuthenticityCheckResult


class FiberChecks(AuthenticityCheckResult):

    @property
    def list(self) -> List[FiberResult]:
        # noinspection PyTypeChecker
        return super().list
