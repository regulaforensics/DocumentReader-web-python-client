import pprint
from copy import copy

from regula.documentreader.webclient.gen.models.result_item import ResultItem


class RawResultItem:
    openapi_types = copy(ResultItem.openapi_types)
    openapi_types["OTHER"] = "Any"

    attribute_map = copy(ResultItem.attribute_map)
    attribute_map["OTHER"] = "raw"

    def __init__(self, buf_length=None, light=None, list_idx=None, page_idx=None, result_type=None, raw=None,
                 local_vars_configuration=None):
        self.result_item = ResultItem(buf_length, light, list_idx, page_idx, result_type, local_vars_configuration)
        self.__raw = raw

    @property
    def result_item(self):
        return self.__result_item

    @result_item.setter
    def result_item(self, value):
        self.__result_item = value

    @property
    def buf_length(self):
        return self.result_item.buf_length

    @buf_length.setter
    def buf_length(self, value):
        self.result_item.buf_length = value

    @property
    def light(self):
        return self.result_item.light

    @light.setter
    def light(self, value):
        self.result_item.light = value

    @property
    def list_idx(self):
        return self.result_item.list_idx

    @list_idx.setter
    def list_idx(self, value):
        self.result_item.list_idx = value

    @property
    def page_idx(self):
        return self.result_item.page_idx

    @page_idx.setter
    def page_idx(self, value):
        self.result_item.page_idx = value

    @property
    def result_type(self):
        return self.result_item.result_type

    @result_type.setter
    def result_type(self, value):
        self.result_item.result_type = value

    @property
    def raw(self):
        return self.__raw

    @raw.setter
    def raw(self, value):
        self.__raw = value

    def to_dict(self):
        result = self.result_item.to_dict()
        result["raw"] = self.__raw
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RawResultItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, RawResultItem):
            return False

        return self.to_dict() != other.to_dict()
