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
    _document_images_results = None

    def get_field(self, field_type: int) -> Optional[ImagesField]:
        for field in self.field_list:
            if field.field_type == field_type:
                return field
        return None

    def document_image(self) -> Optional[bytes]:
        """
           Contains cropped and rotated with perspective compensation image of document.
           Single input image can contain multiple document side/pages, which will be returned as separated results.
           Most coordinates in other types defined on that image.
        """
        images = self.document_images()
        if not images:
            return None
        return images.pop()

    def document_images(self) -> Optional[List[bytes]]:
        """
           Contains cropped and rotated with perspective compensation image of document.
           Single input image can contain multiple document side/pages, which will be returned as separated results.
           Most coordinates in other types defined on that image.
        """
        if self._document_images_results:
            return [base64.b64decode(image.raw_image_container.image)
                    for image in self._document_images_results]
        return None
