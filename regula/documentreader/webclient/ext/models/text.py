from typing import Optional, List

from regula.documentreader.webclient.ext.models.text_field import TextField
from regula.documentreader.webclient.gen.models.text import Text as GenText


class Text(GenText):

    def get_field(self, field_type: int, lcid=0) -> Optional[TextField]:
        for field in self.field_list:
            if field.field_type == field_type and field.lcid == lcid:
                return field
        return None

    def get_field_value(self, field_type: int, lcid=0) -> Optional[str]:
        field = self.get_field(field_type, lcid)
        if field:
            return "todo"
        return None

    @property
    def field_list(self) -> List[TextField]:
        # fix type hinting
        return super().field_list

    @field_list.setter
    def field_list(self, field_list: List[TextField]):
        if self.local_vars_configuration.client_side_validation and field_list is None:
            raise ValueError("Invalid value for `field_list`, must not be `None`")
        self._field_list = field_list
