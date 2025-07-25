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
from regula.documentreader.webclient.gen.models.image_data import ImageData
from regula.documentreader.webclient.gen.models.light import Light
from regula.documentreader.webclient.gen.models.raw_image_container_list import RawImageContainerList
from regula.documentreader.webclient.gen.models.rectangle_coordinates import RectangleCoordinates
from typing import Optional, Set
from typing_extensions import Self

class PhotoIdentItem(BaseModel):
    """
    PhotoIdentItem
    """ # noqa: E501
    light_index: Light = Field(alias="LightIndex")
    area: RectangleCoordinates = Field(alias="Area")
    source_image: ImageData = Field(alias="SourceImage")
    result_images: RawImageContainerList = Field(alias="ResultImages")
    field_types_count: Optional[StrictInt] = Field(default=None, alias="FieldTypesCount")
    field_types_list: Optional[List[StrictInt]] = Field(default=None, alias="FieldTypesList")
    step: Optional[StrictInt] = Field(default=None, alias="Step")
    angle: Optional[StrictInt] = Field(default=None, alias="Angle")
    reserved3: Optional[StrictInt] = Field(default=None, alias="Reserved3")
    __properties: ClassVar[List[str]] = ["LightIndex", "Area", "SourceImage", "ResultImages", "FieldTypesCount", "FieldTypesList", "Step", "Angle", "Reserved3"]

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
        """Create an instance of PhotoIdentItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of area
        if self.area:
            _dict['Area'] = self.area.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_image
        if self.source_image:
            _dict['SourceImage'] = self.source_image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result_images
        if self.result_images:
            _dict['ResultImages'] = self.result_images.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhotoIdentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LightIndex": obj.get("LightIndex"),
            "Area": RectangleCoordinates.from_dict(obj["Area"]) if obj.get("Area") is not None else None,
            "SourceImage": ImageData.from_dict(obj["SourceImage"]) if obj.get("SourceImage") is not None else None,
            "ResultImages": RawImageContainerList.from_dict(obj["ResultImages"]) if obj.get("ResultImages") is not None else None,
            "FieldTypesCount": obj.get("FieldTypesCount"),
            "FieldTypesList": obj.get("FieldTypesList"),
            "Step": obj.get("Step"),
            "Angle": obj.get("Angle"),
            "Reserved3": obj.get("Reserved3")
        })
        return _obj


