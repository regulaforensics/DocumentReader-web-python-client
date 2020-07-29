import base64

from regula.documentreader.webclient.gen.models.image_data import ImageData
from regula.documentreader.webclient.gen.models.process_request import ProcessRequest
from regula.documentreader.webclient.gen.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.models.process_system_info import ProcessSystemInfo


class RecognitionRequest(ProcessRequest):
    def __init__(self, process_params, images):
        super().__init__(process_params, images, ProcessSystemInfo())


class RecognitionImage(ProcessRequestImage):
    def __init__(self, image: bytes, light_index=None, page_index=0):
        image_base64 = base64.b64encode(image).decode("utf-8")
        super().__init__(ImageData(image_base64), light_index, page_index)
