import base64
from typing import Optional, List

from regula.documentreader.webclient.gen.models import Images as GenImages, ImagesField as GetImagesField, Source


class ImagesField(GetImagesField):

    def get_value(self, source: str = None, original=False) -> Optional[bytes]:
        field_value = None
        if not source:
            field_value = self.get_value(Source.RFID)
            if not field_value: field_value = self.get_value(Source.VISUAL)
            if not field_value: field_value = self.get_value(Source.BARCODE)
        else:
            for v in self.value_list:
                if v.source == source:
                    field_value = v

        if not field_value:
            return None

        if original:
            return base64.b64decode(field_value.original_value)
        return base64.b64decode(field_value.value)


class Images(GenImages):
    _normalized_input_images_results = None

    def get_field(self, field_type: int) -> Optional[ImagesField]:
        for field in self.field_list:
            if field.field_type == field_type:
                return field
        return None

    def normalized_input_image(self) -> Optional[bytes]:
        images = self.normalized_input_images()
        if not images:
            return None
        return images.pop()

    def normalized_input_images(self) -> Optional[List[bytes]]:
        if self._normalized_input_images_results:
            return [base64.b64decode(image.raw_image_container.image)
                    for image in self._normalized_input_images_results]
        return None
