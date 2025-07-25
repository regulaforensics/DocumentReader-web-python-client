# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from regula.documentreader.webclient.gen.models.input_image_quality_checks import InputImageQualityChecks
from typing import Optional, Set
from typing_extensions import Self

class ImageQA(BaseModel):
    """
    ImageQA
    """ # noqa: E501
    brightness_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set the threshold for an actual document brightness below which the check fails", alias="brightnessThreshold")
    dpi_threshold: Optional[StrictInt] = Field(default=None, description="This parameter sets threshold for Image QA check of the presented document physical dpi. If actual document dpi is below this threshold, check will fail.", alias="dpiThreshold")
    angle_threshold: Optional[StrictInt] = Field(default=None, description="This parameter sets threshold for Image QA check of the presented document perspective angle in degrees. If actual document perspective angle is above this threshold, check will fail.", alias="angleThreshold")
    focus_check: Optional[StrictBool] = Field(default=None, description="This option enables focus check while performing image quality validation.", alias="focusCheck")
    glares_check: Optional[StrictBool] = Field(default=None, description="This option enables glares check while performing image quality validation.", alias="glaresCheck")
    colorness_check: Optional[StrictBool] = Field(default=None, description="This option enables colorness check while performing image quality validation.", alias="colornessCheck")
    moire_check: Optional[StrictBool] = Field(default=None, description="This option enables screen capture (moire patterns) check while performing image quality validation.", alias="moireCheck")
    document_position_indent: Optional[StrictInt] = Field(default=None, description="This parameter specifies the necessary margin. Default 0.", alias="documentPositionIndent")
    expected_pass: Optional[List[InputImageQualityChecks]] = Field(default=None, description="This parameter controls the quality checks that the image should pass to be considered a valid input during the scanning process.", alias="expectedPass")
    __properties: ClassVar[List[str]] = ["brightnessThreshold", "dpiThreshold", "angleThreshold", "focusCheck", "glaresCheck", "colornessCheck", "moireCheck", "documentPositionIndent", "expectedPass"]

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
        """Create an instance of ImageQA from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageQA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brightnessThreshold": obj.get("brightnessThreshold"),
            "dpiThreshold": obj.get("dpiThreshold"),
            "angleThreshold": obj.get("angleThreshold"),
            "focusCheck": obj.get("focusCheck"),
            "glaresCheck": obj.get("glaresCheck"),
            "colornessCheck": obj.get("colornessCheck"),
            "moireCheck": obj.get("moireCheck"),
            "documentPositionIndent": obj.get("documentPositionIndent"),
            "expectedPass": obj.get("expectedPass")
        })
        return _obj


