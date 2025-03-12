# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.doc_visual_extended_field import DocVisualExtendedField
from regula.documentreader.webclient.gen.models.rectangle_coordinates import RectangleCoordinates
from regula.documentreader.webclient.gen.models.string_recognition_result import StringRecognitionResult
from regula.documentreader.webclient.gen.models.text_field_type import TextFieldType
from typing import Optional, Set
from typing_extensions import Self

class DocVisualExtendedFieldRect(DocVisualExtendedField):
    """
    Structure and serves for storing information from one text data field. Variant with field logical type and field rectangular area coordinates on the image.
    """ # noqa: E501
    field_rect: Optional[RectangleCoordinates] = Field(default=None, alias="FieldRect")
    __properties: ClassVar[List[str]] = ["FieldType", "wFieldType", "FieldName", "StringsCount", "StringsResult", "Buf_Length", "Buf_Text", "FieldMask", "Validity", "InComparison", "wLCID", "Reserved2", "Reserved3", "FieldRect"]

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
        """Create an instance of DocVisualExtendedFieldRect from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in strings_result (list)
        _items = []
        if self.strings_result:
            for _item_strings_result in self.strings_result:
                if _item_strings_result:
                    _items.append(_item_strings_result.to_dict())
            _dict['StringsResult'] = _items
        # override the default output from pydantic by calling `to_dict()` of field_rect
        if self.field_rect:
            _dict['FieldRect'] = self.field_rect.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocVisualExtendedFieldRect from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FieldType": obj.get("FieldType"),
            "wFieldType": obj.get("wFieldType"),
            "FieldName": obj.get("FieldName"),
            "StringsCount": obj.get("StringsCount"),
            "StringsResult": [StringRecognitionResult.from_dict(_item) for _item in obj["StringsResult"]] if obj.get("StringsResult") is not None else None,
            "Buf_Length": obj.get("Buf_Length"),
            "Buf_Text": obj.get("Buf_Text"),
            "FieldMask": obj.get("FieldMask"),
            "Validity": obj.get("Validity"),
            "InComparison": obj.get("InComparison"),
            "wLCID": obj.get("wLCID"),
            "Reserved2": obj.get("Reserved2"),
            "Reserved3": obj.get("Reserved3"),
            "FieldRect": RectangleCoordinates.from_dict(obj["FieldRect"]) if obj.get("FieldRect") is not None else None
        })
        return _obj


