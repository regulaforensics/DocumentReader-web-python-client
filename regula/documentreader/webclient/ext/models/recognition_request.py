import base64
from typing import List, Union

from regula.documentreader.webclient import LicenseResult, EncryptedRCLResult, ContainerList, Result
from regula.documentreader.webclient.gen.models import ImageData, ProcessParams
from regula.documentreader.webclient.gen.models.process_request import ProcessRequest
from regula.documentreader.webclient.gen.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.models.process_system_info import ProcessSystemInfo

Base64String = str


class RecognitionImage(ProcessRequestImage):
    def __init__(self, image: Union[bytes, Base64String], light_index=None, page_index=None):
        if isinstance(image, bytes):
            image = base64.b64encode(image).decode("utf-8")
        super().__init__(
            ImageData = ImageData(image = image),
            light = light_index,
            page_index = page_index,
        )


class LicenseRequest(LicenseResult):
    def __init__(self, _license: Union[bytes, Base64String],
                 _light: int = None, _list_idx: int = None, _page_idx: int = None):
        if isinstance(_license, bytes):
            # if we need to encode
            __license = base64.b64encode(_license).decode("uft-8")
        else:
            __license = _license
        _buf_length = len(_license)
        _result_type = Result.LICENSE
        super().__init__(
            License = __license,
            buf_length = _buf_length,
            light = _light,
            list_idx = _list_idx,
            page_idx = _page_idx,
            result_type = _result_type
        )


class EncryptedRCLRequest(EncryptedRCLResult):
    def __init__(self, _encrypted_rcl: Union[bytes, Base64String] = None,
                 _light: int = None, _list_idx: int = None, _page_idx: int = None):
        if isinstance(_encrypted_rcl, bytes):
            # if we need to encode
            __encrypted_rcl = base64.b64encode(_encrypted_rcl).decode("uft-8")
        else:
            __encrypted_rcl = _encrypted_rcl

        _buf_length = len(_encrypted_rcl)
        _result_type = Result.ENCRYPTED_RCL
        super().__init__(
            EncryptedRCL = __encrypted_rcl,
            buf_length = _buf_length,
            light = _light,
            list_idx = _list_idx,
            page_idx = _page_idx,
            result_type = _result_type
        )


class RecognitionRequest(ProcessRequest):
    def __init__(
            self,
            process_params: ProcessParams,
            images: List[Union[RecognitionImage, bytes, Base64String]] = None,
            container_list: ContainerList = None, tag=None,
            system_info: ProcessSystemInfo = ProcessSystemInfo(),
    ):
        input_images = []
        if images:
            for image in images:
                if isinstance(image, (bytes, str)):
                    input_images.append(RecognitionImage(image))
                else:
                    input_images.append(image)
            super().__init__(
                processParam=process_params,
                List=input_images,
                systemInfo=system_info,
                tag=tag
            )
        if container_list:
            super().__init__(
                processParam=process_params,
                ContainerList=container_list,
                systemInfo=system_info,
                tag=tag
            )
