from regula.documentreader.webclient import CheckResult
from regula.documentreader.webclient.models import TextField as GetTextField


class TextField:
    __payload: GetTextField

    def __init__(self, payload):
        self.__payload = payload

    def get_value(self, source, original=False):
        for i in self.__payload.value_list:
            if i.source == source:
                if original:
                    return i.original_value
                else:
                    return i.value
        return None

    def get_validity(self, source):
        for i in self.__payload.validity_list:
            if i.source == source:
                return i.status
        return CheckResult.WAS_NOT_DONE

    def get_comparison(self, one, other):
        for i in self.__payload.comparison_list:
            a = i.source_left == one and i.source_right == other
            b = i.source_right == one and i.source_left == other
            if a or b:
                return i.status
        return CheckResult.WAS_NOT_DONE
