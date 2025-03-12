# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.auth_params import AuthParams
from regula.documentreader.webclient.gen.models.document_format import DocumentFormat
from regula.documentreader.webclient.gen.models.document_type import DocumentType
from regula.documentreader.webclient.gen.models.face_api import FaceApi
from regula.documentreader.webclient.gen.models.image_qa import ImageQA
from regula.documentreader.webclient.gen.models.input_barcode_type import InputBarcodeType
from regula.documentreader.webclient.gen.models.lcid import LCID
from regula.documentreader.webclient.gen.models.log_level import LogLevel
from regula.documentreader.webclient.gen.models.measure_system import MeasureSystem
from regula.documentreader.webclient.gen.models.mrz_detect_mode_enum import MrzDetectModeEnum
from regula.documentreader.webclient.gen.models.mrz_format import MRZFormat
from regula.documentreader.webclient.gen.models.per_document_config import PerDocumentConfig
from regula.documentreader.webclient.gen.models.process_params_rfid import ProcessParamsRfid
from regula.documentreader.webclient.gen.models.result import Result
from regula.documentreader.webclient.gen.models.scenario import Scenario
from regula.documentreader.webclient.gen.models.text_field_type import TextFieldType
from regula.documentreader.webclient.gen.models.text_post_processing import TextPostProcessing
from typing import Optional, Set
from typing_extensions import Self

class ProcessParams(BaseModel):
    """
    ProcessParams
    """ # noqa: E501
    generate_dtcvc: Optional[StrictBool] = Field(default=None, description="This parameter is used to generate separate DTC-VC data container from RFID session data.", alias="generateDTCVC")
    lcid_filter: Optional[List[LCID]] = Field(default=None, description="The list of LCID types to recognize. If empty, values with all LCID types will be extracted. Empty by default.", alias="lcidFilter")
    check_liveness: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable document liveness check.", alias="checkLiveness")
    lcid_ignore_filter: Optional[List[LCID]] = Field(default=None, description="The list of LCID types to ignore during the recognition. If empty, values with all LCID types will be extracted. Narrowing down the list can reduce processing time. Empty by default.", alias="lcidIgnoreFilter")
    one_shot_identification: Optional[StrictBool] = Field(default=None, description="This parameter allows processing an image that contains a person and a document and compare the portrait photo from the document with the person's face", alias="oneShotIdentification")
    use_face_api: Optional[StrictBool] = Field(default=None, description="This parameter allows comparing faces on Regula Face Web Service", alias="useFaceApi")
    face_api: Optional[FaceApi] = Field(default=None, alias="faceApi")
    do_detect_can: Optional[StrictBool] = Field(default=None, description="This parameter allows enabling the CAN (Card Access Number) detection and recognition when using scenarios with document location and MRZ reading, such as the MrzAndLocate scenario.", alias="doDetectCan")
    image_output_max_height: Optional[StrictInt] = Field(default=None, description="This parameter allows setting maximum height in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.", alias="imageOutputMaxHeight")
    image_output_max_width: Optional[StrictInt] = Field(default=None, description="This parameter allows setting maximum width in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.", alias="imageOutputMaxWidth")
    scenario: Scenario
    result_type_output: Optional[List[Result]] = Field(default=None, description="Types of results to return in response. See 'Result' enum for available options", alias="resultTypeOutput")
    double_page_spread: Optional[StrictBool] = Field(default=None, description="Enable this option if the image you provide contains double page spread of the passport and you want to process both pages in one go. It makes sense to use it for documents that have meaningful information on both pages, like Russian domestic passport, or some others. Disabled by default.", alias="doublePageSpread")
    generate_double_page_spread_image: Optional[StrictBool] = Field(default=None, description="When enabled together with \"doublePageSpread\" and there is a passport with two pages spread in the image, pages will be cropped, straightened and aligned together, as if the document was captured on a flatbed scanner. Disabled by default.", alias="generateDoublePageSpreadImage")
    field_types_filter: Optional[List[TextFieldType]] = Field(default=None, description="List of text field types to extract. If empty, all text fields from template will be extracted. Narrowing the list can shorten processing time. Empty by default.", alias="fieldTypesFilter")
    date_format: Optional[StrictStr] = Field(default=None, description="This option allows you to set dates format so that solution will return dates in this format. For example, if you supply 'MM/dd/yyyy', and document have printed date '09 JUL 2020' for the date os issue, you will get '07/09/2020' as a result. By default it is set to system locale default (where the service is running).", alias="dateFormat")
    measure_system: Optional[MeasureSystem] = Field(default=None, alias="measureSystem")
    image_dpi_out_max: Optional[StrictInt] = Field(default=None, description="This parameter controls maximum resolution in dpi of output images. Resolution will remain original in case 0 is supplied. By default is set to return images in response with resolution not greater than 300 dpi for all scenarios except FullAuth. In FullAuth scenario this limit is 1000 dpi by default.", alias="imageDpiOutMax")
    already_cropped: Optional[StrictBool] = Field(default=None, description="This option can be enabled if you know for sure that the image you provide contains already cropped document by its edges. This was designed to process on the server side images captured and cropped on mobile. Disabled by default.", alias="alreadyCropped")
    custom_params: Optional[Dict[str, Any]] = Field(default=None, description="This option allows passing custom processing parameters that can be implemented in future without changing API.", alias="customParams")
    config: Optional[List[PerDocumentConfig]] = Field(default=None, description="This option allows setting additional custom configuration per document type. If recognized document has ID specified in config, processing adjusts according to designated configuration.")
    log: Optional[StrictBool] = Field(default=None, description="When enabled, results will contain transaction processing log. Disabled by default")
    log_level: Optional[LogLevel] = Field(default=None, alias="logLevel")
    force_doc_id: Optional[StrictInt] = Field(default=None, description="Force use of specific template ID and skip document type identification step.", alias="forceDocID")
    match_text_field_mask: Optional[StrictBool] = Field(default=None, description="When disabled, text field OCR will be done as is and then the recognized value will be matched to the field mask for validity. If enabled, we are trying to read a field value with maximum efforts to match the mask and provide a correctly formatted value, making assumptions based on the provided field mask in the template. Enabled by default.", alias="matchTextFieldMask")
    fast_doc_detect: Optional[StrictBool] = Field(default=None, description="When enabled, shorten the list of candidates to process during document detection in a single image process mode. Reduces processing time for specific backgrounds. Enabled by default.", alias="fastDocDetect")
    update_ocr_validity_by_glare: Optional[StrictBool] = Field(default=None, description="When enabled, fail OCR field validity, if there is a glare over the text field on the image. Disabled by default.", alias="updateOCRValidityByGlare")
    check_required_text_fields: Optional[StrictBool] = Field(default=None, description="When enabled, each field in template will be checked for value presence and if the field is marked as required, but has no value, it will have 'error' in validity status. Disabled by default.", alias="checkRequiredTextFields")
    return_cropped_barcode: Optional[StrictBool] = Field(default=None, description="When enabled, returns cropped barcode images for unknown documents. Disabled by default.", alias="returnCroppedBarcode")
    image_qa: Optional[ImageQA] = Field(default=None, alias="imageQa")
    strict_image_quality: Optional[StrictBool] = Field(default=None, description="When enabled, the image quality check status affects the document optical and overall status. Disabled by default.", alias="strictImageQuality")
    respect_image_quality: Optional[StrictBool] = Field(default=None, description="Deprecated. Please use strictImageQuality instead. When enabled, image quality checks status affects document optical and overall status. Disabled by default.", alias="respectImageQuality")
    force_doc_format: Optional[DocumentFormat] = Field(default=None, alias="forceDocFormat")
    no_graphics: Optional[StrictBool] = Field(default=None, description="When enabled, no graphic fields will be cropped from document image. Disabled by default.", alias="noGraphics")
    depersonalize_log: Optional[StrictBool] = Field(default=None, description="When enabled, all personal data will be forcibly removed from the logs. Disabled by default.", alias="depersonalizeLog")
    multi_doc_on_image: Optional[StrictBool] = Field(default=None, description="This option allows locating and cropping multiple documents from one image if enabled. Disabled by default.", alias="multiDocOnImage")
    shift_expiry_date: Optional[StrictInt] = Field(default=None, description="This option allows shifting the date of expiry into the future or past for number of months specified. This is useful, for example, in some cases when document might be still valid for some period after original expiration date to prevent negative validity status for such documents. Or by shifting the date to the past will set negative validity for the documents that is about to expire in a specified number of months. 0 by default", alias="shiftExpiryDate")
    minimal_holder_age: Optional[StrictInt] = Field(default=None, description="This options allows specifying the minimal age in years of the document holder for the document to be considered valid.", alias="minimalHolderAge")
    return_uncropped_image: Optional[StrictBool] = Field(default=None, description="When enabled, returns input images in output. Disabled by default.", alias="returnUncroppedImage")
    mrz_formats_filter: Optional[List[MRZFormat]] = Field(default=None, description="This option allows limiting MRZ formats to be recognized by specifying them in array.", alias="mrzFormatsFilter")
    force_read_mrz_before_locate: Optional[StrictBool] = Field(default=None, description="When enabled, make sure that in series processing MRZ is located fully inside the result document image, if present on the document. Enabling this option may add extra processing time, by disabling optimizations, but allows more stability in output image quality. Disabled by default.", alias="forceReadMrzBeforeLocate")
    parse_barcodes: Optional[StrictBool] = Field(default=None, description="This option can be disabled to stop parsing after barcode is read. Enabled by default.", alias="parseBarcodes")
    convert_case: Optional[TextPostProcessing] = Field(default=None, alias="convertCase")
    split_names: Optional[StrictBool] = Field(default=None, description="When enabled, the Surname and GivenNames fields from MRZ will be divided into ft_First_Name, ft_Second_Name, ft_Third_Name, ft_Fourth_Name, ft_Last_Name fields. Disabled by default.", alias="splitNames")
    disable_perforation_ocr: Optional[StrictBool] = Field(default=None, description="When enabled, OCR of perforated fields in the document template will not be performed. Disabled by default.", alias="disablePerforationOCR")
    document_group_filter: Optional[List[DocumentType]] = Field(default=None, description="List of specific eligible document types from DocumentType enum to recognize from. You may, for example, specify only passports to be recognized by setting this property. Empty by default.", alias="documentGroupFilter")
    process_auth: Optional[StrictInt] = Field(default=None, description="Authenticity checks that should be performed regardless of the document type. The available checks are listed in the eRPRM_Authenticity enum. Note that only supported by your license checks can be added. ", alias="processAuth")
    device_id: Optional[StrictInt] = Field(default=None, description="This parameter is used to specify the document reader device type from which input images were captured. Default 0.", alias="deviceId")
    device_type: Optional[StrictInt] = Field(default=None, description="This parameter is used to specify the document reader device type from which input images were captured. Default 0.", alias="deviceType")
    device_type_hex: Optional[StrictStr] = Field(default=None, description="This parameter is used to specify the document reader device type from which input images were captured", alias="deviceTypeHex")
    ignore_device_id_from_image: Optional[StrictBool] = Field(default=None, description="This parameter is used to tell the processing engine to ignore any parameters saved in the image when scanned from the document reader device. Default false", alias="ignoreDeviceIdFromImage")
    document_id_list: Optional[List[StrictInt]] = Field(default=None, description="List of the document ID's to process. All documents will be processed, if empty.", alias="documentIdList")
    rfid: Optional[ProcessParamsRfid] = None
    check_auth: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable authenticity checks", alias="checkAuth")
    auth_params: Optional[AuthParams] = Field(default=None, alias="authParams")
    mrz_detect_mode: Optional[MrzDetectModeEnum] = Field(default=None, alias="mrzDetectMode")
    generate_numeric_codes: Optional[StrictBool] = Field(default=None, description="This parameter is used to generate numeric representation for issuing state and nationality codes", alias="generateNumericCodes")
    strict_barcode_digital_signature_check: Optional[StrictBool] = Field(default=None, description="This parameter if enabled will require all necessary certificates to verify digital signature in barcode data to be present in order for the Barcode format check to succeed.", alias="strictBarcodeDigitalSignatureCheck")
    select_longest_names: Optional[StrictBool] = Field(default=None, description="Select the longest value from the different value sources and write it to the value field if comparison is done successfully. The parameter applies this logic to the personal names, such as given name, surname, surname and given name, middle name and etc.", alias="selectLongestNames")
    do_barcodes: Optional[List[InputBarcodeType]] = Field(default=None, description="Set the types of barcodes to process.", alias="doBarcodes")
    __properties: ClassVar[List[str]] = ["generateDTCVC", "lcidFilter", "checkLiveness", "lcidIgnoreFilter", "oneShotIdentification", "useFaceApi", "faceApi", "doDetectCan", "imageOutputMaxHeight", "imageOutputMaxWidth", "scenario", "resultTypeOutput", "doublePageSpread", "generateDoublePageSpreadImage", "fieldTypesFilter", "dateFormat", "measureSystem", "imageDpiOutMax", "alreadyCropped", "customParams", "config", "log", "logLevel", "forceDocID", "matchTextFieldMask", "fastDocDetect", "updateOCRValidityByGlare", "checkRequiredTextFields", "returnCroppedBarcode", "imageQa", "strictImageQuality", "respectImageQuality", "forceDocFormat", "noGraphics", "depersonalizeLog", "multiDocOnImage", "shiftExpiryDate", "minimalHolderAge", "returnUncroppedImage", "mrzFormatsFilter", "forceReadMrzBeforeLocate", "parseBarcodes", "convertCase", "splitNames", "disablePerforationOCR", "documentGroupFilter", "processAuth", "deviceId", "deviceType", "deviceTypeHex", "ignoreDeviceIdFromImage", "documentIdList", "rfid", "checkAuth", "authParams", "mrzDetectMode", "generateNumericCodes", "strictBarcodeDigitalSignatureCheck", "selectLongestNames", "doBarcodes"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProcessParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of face_api
        if self.face_api:
            _dict['faceApi'] = self.face_api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in config (list)
        _items = []
        if self.config:
            for _item_config in self.config:
                if _item_config:
                    _items.append(_item_config.to_dict())
            _dict['config'] = _items
        # override the default output from pydantic by calling `to_dict()` of image_qa
        if self.image_qa:
            _dict['imageQa'] = self.image_qa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rfid
        if self.rfid:
            _dict['rfid'] = self.rfid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth_params
        if self.auth_params:
            _dict['authParams'] = self.auth_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProcessParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "generateDTCVC": obj.get("generateDTCVC"),
            "lcidFilter": obj.get("lcidFilter"),
            "checkLiveness": obj.get("checkLiveness"),
            "lcidIgnoreFilter": obj.get("lcidIgnoreFilter"),
            "oneShotIdentification": obj.get("oneShotIdentification"),
            "useFaceApi": obj.get("useFaceApi"),
            "faceApi": FaceApi.from_dict(obj["faceApi"]) if obj.get("faceApi") is not None else None,
            "doDetectCan": obj.get("doDetectCan"),
            "imageOutputMaxHeight": obj.get("imageOutputMaxHeight"),
            "imageOutputMaxWidth": obj.get("imageOutputMaxWidth"),
            "scenario": obj.get("scenario"),
            "resultTypeOutput": obj.get("resultTypeOutput"),
            "doublePageSpread": obj.get("doublePageSpread"),
            "generateDoublePageSpreadImage": obj.get("generateDoublePageSpreadImage"),
            "fieldTypesFilter": obj.get("fieldTypesFilter"),
            "dateFormat": obj.get("dateFormat"),
            "measureSystem": obj.get("measureSystem"),
            "imageDpiOutMax": obj.get("imageDpiOutMax"),
            "alreadyCropped": obj.get("alreadyCropped"),
            "customParams": obj.get("customParams"),
            "config": [PerDocumentConfig.from_dict(_item) for _item in obj["config"]] if obj.get("config") is not None else None,
            "log": obj.get("log"),
            "logLevel": obj.get("logLevel"),
            "forceDocID": obj.get("forceDocID"),
            "matchTextFieldMask": obj.get("matchTextFieldMask"),
            "fastDocDetect": obj.get("fastDocDetect"),
            "updateOCRValidityByGlare": obj.get("updateOCRValidityByGlare"),
            "checkRequiredTextFields": obj.get("checkRequiredTextFields"),
            "returnCroppedBarcode": obj.get("returnCroppedBarcode"),
            "imageQa": ImageQA.from_dict(obj["imageQa"]) if obj.get("imageQa") is not None else None,
            "strictImageQuality": obj.get("strictImageQuality"),
            "respectImageQuality": obj.get("respectImageQuality"),
            "forceDocFormat": obj.get("forceDocFormat"),
            "noGraphics": obj.get("noGraphics"),
            "depersonalizeLog": obj.get("depersonalizeLog"),
            "multiDocOnImage": obj.get("multiDocOnImage"),
            "shiftExpiryDate": obj.get("shiftExpiryDate"),
            "minimalHolderAge": obj.get("minimalHolderAge"),
            "returnUncroppedImage": obj.get("returnUncroppedImage"),
            "mrzFormatsFilter": obj.get("mrzFormatsFilter"),
            "forceReadMrzBeforeLocate": obj.get("forceReadMrzBeforeLocate"),
            "parseBarcodes": obj.get("parseBarcodes"),
            "convertCase": obj.get("convertCase"),
            "splitNames": obj.get("splitNames"),
            "disablePerforationOCR": obj.get("disablePerforationOCR"),
            "documentGroupFilter": obj.get("documentGroupFilter"),
            "processAuth": obj.get("processAuth"),
            "deviceId": obj.get("deviceId"),
            "deviceType": obj.get("deviceType"),
            "deviceTypeHex": obj.get("deviceTypeHex"),
            "ignoreDeviceIdFromImage": obj.get("ignoreDeviceIdFromImage"),
            "documentIdList": obj.get("documentIdList"),
            "rfid": ProcessParamsRfid.from_dict(obj["rfid"]) if obj.get("rfid") is not None else None,
            "checkAuth": obj.get("checkAuth"),
            "authParams": AuthParams.from_dict(obj["authParams"]) if obj.get("authParams") is not None else None,
            "mrzDetectMode": obj.get("mrzDetectMode"),
            "generateNumericCodes": obj.get("generateNumericCodes"),
            "strictBarcodeDigitalSignatureCheck": obj.get("strictBarcodeDigitalSignatureCheck"),
            "selectLongestNames": obj.get("selectLongestNames"),
            "doBarcodes": obj.get("doBarcodes")
        })
        return _obj


