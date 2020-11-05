from typing import Optional, List

from regula.documentreader.webclient.ext.models.text_field import TextField
from regula.documentreader.webclient.gen.models import Text as GenText


class Text(GenText):

    def get_field(self, field_type: int, lcid: int = None) -> Optional[TextField]:
        for field in self.field_list:
            if field.field_type == field_type and (not lcid or field.lcid == lcid):
                return field
        return None

    def get_field_value(self, field_type: int, lcid: int = None) -> Optional[str]:
        field = self.get_field(field_type, lcid)
        if field:
            return field.value
        return None

    def get_field_by_name(self, field_name: str, lcid: int = None) -> Optional[TextField]:
        for field in self.field_list:
            if field.field_name == field_name and (not lcid or field.lcid == lcid):
                return field
        return None

    def get_field_value_by_name(self, field_name: str, lcid: int = None) -> Optional[str]:
        field = self.get_field_by_name(field_name, lcid)
        if field:
            return field.value
        return None

    @GenText.field_list.getter
    def field_list(self) -> List[TextField]:
        # fix type hinting
        return super().field_list
