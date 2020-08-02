from typing import Optional

from regula.documentreader.webclient.gen.models.check_result import CheckResult
from regula.documentreader.webclient.gen.models.text_field import TextField as GenTextField


class TextField(GenTextField):

    def get_value(self, source: str = None, original=False) -> Optional[str]:
        if not source:
            return self.value
        for i in self.value_list:
            if i.source == source:
                if original:
                    return i.original_value
                else:
                    return i.value
        return None

    def source_validity(self, source: str) -> CheckResult:
        for i in self.validity_list:
            if i.source == source:
                return i.status
        return CheckResult.WAS_NOT_DONE

    def cross_source_comparison(self, one: str, other: str) -> CheckResult:
        for i in self.comparison_list:
            a = i.source_left == one and i.source_right == other
            b = i.source_right == one and i.source_left == other
            if a or b:
                return i.status
        return CheckResult.WAS_NOT_DONE
