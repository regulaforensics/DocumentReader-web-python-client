# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.liveness_params import LivenessParams
from typing import Optional, Set
from typing_extensions import Self

class AuthParams(BaseModel):
    """
    AuthParams
    """ # noqa: E501
    check_liveness: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable document liveness check", alias="checkLiveness")
    liveness_params: Optional[LivenessParams] = Field(default=None, alias="livenessParams")
    check_uv_luminiscence: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Document luminescence check in UV light", alias="checkUVLuminiscence")
    check_irb900: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable B900 ink MRZ contrast check in IR light", alias="checkIRB900")
    check_image_patterns: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Image patterns presence/absence check (position, shape, color)", alias="checkImagePatterns")
    check_fibers: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Fibers detection", alias="checkFibers")
    check_ext_mrz: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Extended MRZ Check", alias="checkExtMRZ")
    check_ext_ocr: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Extended OCR Check", alias="checkExtOCR")
    check_axial: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable laminate integrity check in axial light", alias="checkAxial")
    check_barcode_format: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Barcode format check (code metadata, data format, contents format, etc.)", alias="checkBarcodeFormat")
    check_ir_visibility: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Document elements visibility check in IR light", alias="checkIRVisibility")
    check_ipi: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Invisible Personal Information (IPI) check", alias="checkIPI")
    check_photo_embedding: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Owner's photo embedding check (is photo printed or sticked)", alias="checkPhotoEmbedding")
    check_photo_comparison: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Portrait comparison check", alias="checkPhotoComparison")
    check_letter_screen: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable LetterScreen check", alias="checkLetterScreen")
    check_security_text: Optional[StrictBool] = Field(default=None, description="This parameter is used to enable Security text check", alias="checkSecurityText")
    __properties: ClassVar[List[str]] = ["checkLiveness", "livenessParams", "checkUVLuminiscence", "checkIRB900", "checkImagePatterns", "checkFibers", "checkExtMRZ", "checkExtOCR", "checkAxial", "checkBarcodeFormat", "checkIRVisibility", "checkIPI", "checkPhotoEmbedding", "checkPhotoComparison", "checkLetterScreen", "checkSecurityText"]

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
        """Create an instance of AuthParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of liveness_params
        if self.liveness_params:
            _dict['livenessParams'] = self.liveness_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checkLiveness": obj.get("checkLiveness"),
            "livenessParams": LivenessParams.from_dict(obj["livenessParams"]) if obj.get("livenessParams") is not None else None,
            "checkUVLuminiscence": obj.get("checkUVLuminiscence"),
            "checkIRB900": obj.get("checkIRB900"),
            "checkImagePatterns": obj.get("checkImagePatterns"),
            "checkFibers": obj.get("checkFibers"),
            "checkExtMRZ": obj.get("checkExtMRZ"),
            "checkExtOCR": obj.get("checkExtOCR"),
            "checkAxial": obj.get("checkAxial"),
            "checkBarcodeFormat": obj.get("checkBarcodeFormat"),
            "checkIRVisibility": obj.get("checkIRVisibility"),
            "checkIPI": obj.get("checkIPI"),
            "checkPhotoEmbedding": obj.get("checkPhotoEmbedding"),
            "checkPhotoComparison": obj.get("checkPhotoComparison"),
            "checkLetterScreen": obj.get("checkLetterScreen"),
            "checkSecurityText": obj.get("checkSecurityText")
        })
        return _obj


