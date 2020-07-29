from typing import Optional

from regula.documentreader.webclient.ext.models.text_field import TextField
from regula.documentreader.webclient.gen.models.text import Text as GenText


class Text:
    __payload: GenText

    def __init__(self, payload):
        self.__payload = payload

    def get_field(self, field_type, lcid=0) -> Optional[TextField]:
        for i in self.__payload.field_list:
            if i.field_type == field_type and i.lcid == lcid:
                return TextField(i)
        return None

    def get_field_value(self, field_type, lcid=0):
        field = self.get_field(field_type, lcid)
        if field:
            return "todo"
        return None
