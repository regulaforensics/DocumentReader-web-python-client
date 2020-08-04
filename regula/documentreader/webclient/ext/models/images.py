import base64
from typing import Optional, List

from regula.documentreader.webclient.gen.models import Images as GenImages, ImagesField as GetImagesField, Source


class ImagesField(GetImagesField):

    def get_value(self, source: str = None, original=False) -> Optional[bytes]:

        if not source:
            value = self.get_value(Source.RFID)
            if not value: value = self.get_value(Source.VISUAL)
            if not value: value = self.get_value(Source.BARCODE)
            if not value: value = self.get_value("UNKNOWN") # temp fix, will be removed
            return value
        else:
            field_value = None
            for v in self.value_list:
                if v.source == source:
                    field_value = v

            if not field_value:
                return None

            if original:
                return base64.b64decode(field_value.original_value)
            return base64.b64decode(field_value.value)


class Images(GenImages):

    def get_field(self, field_type: int) -> Optional[ImagesField]:
        for field in self.field_list:
            if field.field_type == field_type:
                return field
        return None

    def get_fields(self, field_type: int) -> List[ImagesField]:
        return [field for field in self.field_list if field.field_type == field_type]
