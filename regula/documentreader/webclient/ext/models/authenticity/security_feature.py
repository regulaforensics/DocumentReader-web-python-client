from typing import List, cast

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, SecurityFeatureResult


class SecurityFeatureChecks(AuthenticityCheckResult):

    @property
    def checks_list(self) -> List[SecurityFeatureResult]:
        security_feature_list: List[SecurityFeatureResult] = cast(List[SecurityFeatureResult], self.list)
        return security_feature_list

    # element_type is SecurityFeatureType
    def checks_by_element(self, element_type: int) -> List[SecurityFeatureResult]:
        return [check for check in self.checks_list if check.element_type == element_type]
