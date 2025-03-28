# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.face_item import FaceItem
from typing import Optional, Set
from typing_extensions import Self

class FaceDetection(BaseModel):
    """
    FaceDetection
    """ # noqa: E501
    count: StrictInt = Field(alias="Count")
    count_false_detection: StrictInt = Field(alias="CountFalseDetection")
    res: List[FaceItem] = Field(alias="Res")
    reserved1: Optional[StrictInt] = Field(default=None, alias="Reserved1")
    reserved2: Optional[StrictInt] = Field(default=None, alias="Reserved2")
    __properties: ClassVar[List[str]] = ["Count", "CountFalseDetection", "Res", "Reserved1", "Reserved2"]

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
        """Create an instance of FaceDetection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in res (list)
        _items = []
        if self.res:
            for _item_res in self.res:
                if _item_res:
                    _items.append(_item_res.to_dict())
            _dict['Res'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaceDetection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Count": obj.get("Count"),
            "CountFalseDetection": obj.get("CountFalseDetection"),
            "Res": [FaceItem.from_dict(_item) for _item in obj["Res"]] if obj.get("Res") is not None else None,
            "Reserved1": obj.get("Reserved1"),
            "Reserved2": obj.get("Reserved2")
        })
        return _obj


