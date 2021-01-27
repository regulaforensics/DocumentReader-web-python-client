from copy import copy

from regula.documentreader.webclient.gen.models.authenticity_check_result_item import AuthenticityCheckResultItem


class RawAuthenticityCheckResultItem(AuthenticityCheckResultItem):
    openapi_types = copy(AuthenticityCheckResultItem.openapi_types)
    openapi_types["raw"] = "dict"

    attribute_map = copy(AuthenticityCheckResultItem.attribute_map)
    attribute_map["raw"] = "raw"

    def __init__(self, type=0, element_result=None, element_diagnose=None, raw=None, local_vars_configuration=None):
        super().__init__(type, element_result, element_diagnose, local_vars_configuration)
        self.__raw = raw

    @property
    def raw(self):
        return self.__raw

    def to_dict(self):
        result = super(RawAuthenticityCheckResultItem, self).to_dict()
        result["raw"] = self.__raw
        return result

    def get_real_child_model(self, data):
        return None
