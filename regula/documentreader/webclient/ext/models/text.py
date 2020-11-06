from typing import Optional, List

from regula.documentreader.webclient.ext.models.text_field import TextField
from regula.documentreader.webclient.gen.models import LCID, Text as GenText


class Text(GenText):

    def get_field(self, field_type: int, lcid: int = None) -> Optional[TextField]:
        result = None
        for field in self.field_list:
            if field.field_type == field_type:
                if lcid is not None and field.lcid == lcid:
                    return field
                elif lcid is None and field.lcid == LCID.LATIN:
                    return field
                elif lcid is None and result is None:
                    result = field
        return result

    def get_field_value(self, field_type: int, lcid: int = None) -> Optional[str]:
        field = self.get_field(field_type, lcid)
        return field.value if field else None

    def get_field_by_name(self, field_name: str, lcid: int = None) -> Optional[TextField]:
        result = None
        for field in self.field_list:
            if field.field_name == field_name:
                if lcid is not None and field.lcid == lcid:
                    return field
                elif lcid is None and field.lcid == LCID.LATIN:
                    return field
                elif lcid is None and result is None:
                    result = field
        return result

    def get_field_value_by_name(self, field_name: str, lcid: int = None) -> Optional[str]:
        field = self.get_field_by_name(field_name, lcid)
        return field.value if field else None

    @GenText.field_list.getter
    def field_list(self) -> List[TextField]:
        # fix type hinting
        return super().field_list
