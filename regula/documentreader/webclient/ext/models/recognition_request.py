import base64
import json
from typing import List, Union, Optional

from regula.documentreader.webclient.gen.api_client import ModelSerDe
from regula.documentreader.webclient.gen.models import ImageData, ProcessParams
from regula.documentreader.webclient.gen.models.process_request import ProcessRequest
from regula.documentreader.webclient.gen.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.models.process_system_info import ProcessSystemInfo

Base64String = str
serde = ModelSerDe()


class RecognitionImage(ProcessRequestImage):
    def __init__(self, image: Union[bytes, Base64String], light_index=None, page_index=None):
        if isinstance(image, bytes):
            image = base64.b64encode(image).decode("utf-8")
        super().__init__(ImageData(image), light_index, page_index)


class RecognitionRequest(ProcessRequest):
    def __init__(self, process_params: ProcessParams, images: List[Union[RecognitionImage, bytes, Base64String]]):
        input_images = []
        for image in images:
            if isinstance(image, (bytes, str)):
                input_images.append(RecognitionImage(image))
            else:
                input_images.append(image)
        super().__init__(process_params, input_images, ProcessSystemInfo())


class RawRecognitionRequest(dict):
    def __init__(self, raw_json_request: Union[bytes, str], process_params: Optional[ProcessParams] = None):
        request = json.loads(raw_json_request)
        if process_params:
            request["processParam"] = serde.sanitize_for_serialization(process_params)
        super().__init__(request)
