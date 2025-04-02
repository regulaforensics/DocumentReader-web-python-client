from typing import List

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, IdentResult


class IdentChecks(AuthenticityCheckResult):

    @property
    def list(self) -> List[IdentResult]:
        # noinspection PyTypeChecker
        return self.list

    # element_type is SecurityFeatureType
    def checks_by_element(self, element_type: int) -> List[IdentResult]:
        return [check for check in self.list if check.element_type == element_type]
