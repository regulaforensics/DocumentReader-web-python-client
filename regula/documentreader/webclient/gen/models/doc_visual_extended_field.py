# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from regula.documentreader.webclient.gen.models.string_recognition_result import StringRecognitionResult
from regula.documentreader.webclient.gen.models.text_field_type import TextFieldType
from typing import Optional, Set
from typing_extensions import Self

class DocVisualExtendedField(BaseModel):
    """
    DocVisualExtendedField
    """ # noqa: E501
    field_type: StrictInt = Field(alias="FieldType")
    w_field_type: TextFieldType = Field(alias="wFieldType")
    field_name: StrictStr = Field(description="Field symbolic name (null-terminated string)", alias="FieldName")
    strings_count: Union[StrictFloat, StrictInt] = Field(description="Number of StringsResult array elements", alias="StringsCount")
    strings_result: List[StringRecognitionResult] = Field(description="Array of recognizing probabilities for a each line of text field. Only for Result.VISUAL_TEXT and Result.MRZ_TEXT results.", alias="StringsResult")
    buf_length: Union[StrictFloat, StrictInt] = Field(description="Buf_Text text string length", alias="Buf_Length")
    buf_text: StrictStr = Field(description="Text field data in UTF8 format. Results of reading different lines of a multi-line field are separated by '^'", alias="Buf_Text")
    field_mask: Optional[StrictStr] = Field(default=None, alias="FieldMask")
    validity: Optional[StrictInt] = Field(default=None, alias="Validity")
    in_comparison: Optional[StrictInt] = Field(default=None, alias="InComparison")
    w_lcid: Optional[StrictInt] = Field(default=None, alias="wLCID")
    reserved2: Optional[StrictInt] = Field(default=None, alias="Reserved2")
    reserved3: Optional[StrictInt] = Field(default=None, alias="Reserved3")
    __properties: ClassVar[List[str]] = ["FieldType", "wFieldType", "FieldName", "StringsCount", "StringsResult", "Buf_Length", "Buf_Text", "FieldMask", "Validity", "InComparison", "wLCID", "Reserved2", "Reserved3"]

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
        """Create an instance of DocVisualExtendedField from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocVisualExtendedField from a dict"""
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
            "Reserved3": obj.get("Reserved3")
        })
        return _obj


