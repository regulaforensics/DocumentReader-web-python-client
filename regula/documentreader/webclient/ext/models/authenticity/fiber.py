from typing import List, cast

from regula.documentreader.webclient.gen.models import FiberResult, AuthenticityCheckResult


class FiberChecks(AuthenticityCheckResult):

    @property
    def checks_list(self) -> List[FiberResult]:
        fiber_list: List[FiberResult] = cast(List[FiberResult], self.list)
        return fiber_list
