from typing import List, Optional

from regula.documentreader.webclient import gen


class IdentChecks(gen.AuthenticityCheckResult):
    @gen.AuthenticityCheckResult.list.getter
    def list(self) -> List[gen.IdentResult]:
        # noinspection PyTypeChecker
        return super().list

    # element_type is SecurityFeatureType
    def checks_by_element(self, element_type: int) -> List[gen.IdentResult]:
        return [check for check in self.list if check.element_type == element_type]
