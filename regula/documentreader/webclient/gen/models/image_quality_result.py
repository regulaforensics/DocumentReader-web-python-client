# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from regula.documentreader.webclient.gen.models.image_quality_check_list import ImageQualityCheckList
from regula.documentreader.webclient.gen.models.result_item import ResultItem
from typing import Optional, Set
from typing_extensions import Self

class ImageQualityResult(ResultItem):
    """
    ImageQualityResult
    """ # noqa: E501
    image_quality_check_list: ImageQualityCheckList = Field(alias="ImageQualityCheckList")
    __properties: ClassVar[List[str]] = ["buf_length", "light", "list_idx", "page_idx", "result_type", "ImageQualityCheckList"]

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
        """Create an instance of ImageQualityResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of image_quality_check_list
        if self.image_quality_check_list:
            _dict['ImageQualityCheckList'] = self.image_quality_check_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageQualityResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buf_length": obj.get("buf_length"),
            "light": obj.get("light"),
            "list_idx": obj.get("list_idx"),
            "page_idx": obj.get("page_idx"),
            "result_type": obj.get("result_type") if obj.get("result_type") is not None else 0,
            "ImageQualityCheckList": ImageQualityCheckList.from_dict(obj["ImageQualityCheckList"]) if obj.get("ImageQualityCheckList") is not None else None
        })
        return _obj


