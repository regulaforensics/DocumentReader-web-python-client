from copy import copy

from regula.documentreader.webclient.gen.models.result_item import ResultItem


class RawResultItem(ResultItem):
    openapi_types = copy(ResultItem.openapi_types)
    openapi_types["raw"] = "dict"

    attribute_map = copy(ResultItem.attribute_map)
    attribute_map["raw"] = "raw"

    def __init__(self, buf_length=None, light=None, list_idx=None, page_idx=None, result_type=None, raw=None,
                 local_vars_configuration=None):
        super().__init__(buf_length, light, list_idx, page_idx, result_type, local_vars_configuration)
        self.__raw = raw

    @property
    def raw(self):
        return self.__raw

    def to_dict(self):
        result = super(RawResultItem, self).to_dict()
        result["raw"] = self.__raw
        return result

    def get_real_child_model(self, data):
        return None
