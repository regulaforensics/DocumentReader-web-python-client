from typing import List, Optional

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, SecurityFeatureResult


class SecurityFeatureChecks(AuthenticityCheckResult):

    @property
    def list(self) -> List[SecurityFeatureResult]:
        # noinspection PyTypeChecker
        return self.list

    # element_type is SecurityFeatureType
    def checks_by_element(self, element_type: int) -> List[SecurityFeatureResult]:
        return [check for check in self.list if check.element_type == element_type]
