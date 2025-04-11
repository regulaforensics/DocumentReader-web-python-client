from typing import List, cast

from regula.documentreader.webclient.gen.models import AuthenticityCheckResult, OCRSecurityTextResult


class OCRSecurityTextChecks(AuthenticityCheckResult):

    @property
    def checks_list(self) -> List[OCRSecurityTextResult]:
        ocr_security_text_list: List[OCRSecurityTextResult] = cast(List[OCRSecurityTextResult], self.list)
        return ocr_security_text_list
