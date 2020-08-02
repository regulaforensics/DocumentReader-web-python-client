from typing import Optional

from regula.documentreader.webclient.gen.models.check_result import CheckResult
from regula.documentreader.webclient.gen.models.text_field import TextField as GenTextField


class TextField(GenTextField):

    def get_value(self, source: str, original=False) -> Optional[str]:
        for i in self.value_list:
            if i.source == source:
                if original:
                    return i.original_value
                else:
                    return i.value
        return None

    def get_validity(self, source) -> CheckResult:
        for i in self.validity_list:
            if i.source == source:
                return i.status
        return CheckResult.WAS_NOT_DONE

    def get_comparison(self, one, other) -> CheckResult:
        for i in self.comparison_list:
            a = i.source_left == one and i.source_right == other
            b = i.source_right == one and i.source_left == other
            if a or b:
                return i.status
        return CheckResult.WAS_NOT_DONE
