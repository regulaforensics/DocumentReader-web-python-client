from typing import List

from regula.documentreader.webclient import gen


class FiberChecks(gen.AuthenticityCheckResult):

    @property
    def list(self) -> List[gen.FiberResult]:
        # noinspection PyTypeChecker
        return super().list
