# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from regula.documentreader.webclient.gen.models.file_image import FileImage
from typing import Optional, Set
from typing_extensions import Self

class GraphData(BaseModel):
    """
    GraphData
    """ # noqa: E501
    field_type: StrictInt = Field(alias="FieldType")
    file_image: FileImage = Field(alias="File_Image")
    graphics_type: StrictInt = Field(alias="GraphicsType")
    origin_dg: StrictInt = Field(alias="OriginDG")
    origin_dg_tag: StrictInt = Field(alias="OriginDGTag")
    origin_entry_view: StrictInt = Field(alias="OriginEntryView")
    origin_tag_entry: StrictInt = Field(alias="OriginTagEntry")
    __properties: ClassVar[List[str]] = ["FieldType", "File_Image", "GraphicsType", "OriginDG", "OriginDGTag", "OriginEntryView", "OriginTagEntry"]

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
        """Create an instance of GraphData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file_image
        if self.file_image:
            _dict['File_Image'] = self.file_image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GraphData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FieldType": obj.get("FieldType"),
            "File_Image": FileImage.from_dict(obj["File_Image"]) if obj.get("File_Image") is not None else None,
            "GraphicsType": obj.get("GraphicsType"),
            "OriginDG": obj.get("OriginDG"),
            "OriginDGTag": obj.get("OriginDGTag"),
            "OriginEntryView": obj.get("OriginEntryView"),
            "OriginTagEntry": obj.get("OriginTagEntry")
        })
        return _obj


