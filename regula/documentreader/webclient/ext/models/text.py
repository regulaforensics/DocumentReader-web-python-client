from typing import Optional, List

from regula.documentreader.webclient.ext.models.text_field import TextField
from regula.documentreader.webclient.gen.models import Text as GenText


class Text(GenText):

    def get_field(self, field_type: int, lcid: int = None) -> Optional[TextField]:
        for field in self.field_list:
            if field.field_type == field_type and (not lcid or field.lcid == lcid):
                return field
        return None

    @GenText.field_list.getter
    def field_list(self) -> List[TextField]:
        # fix type hinting
        return super().field_list
