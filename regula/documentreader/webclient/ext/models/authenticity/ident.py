from typing import List, cast

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, IdentResult


class IdentChecks(AuthenticityCheckResult):

    @property
    def checks_list(self) -> List[IdentResult]:
        ident_list: List[IdentResult] = cast(List[IdentResult], self.list)
        return ident_list

    # element_type is SecurityFeatureType
    def checks_by_element(self, element_type: int) -> List[IdentResult]:
        return [check for check in self.checks_list if check.element_type == element_type]