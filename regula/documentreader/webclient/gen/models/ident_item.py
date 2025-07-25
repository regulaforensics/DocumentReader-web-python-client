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
from regula.documentreader.webclient.gen.models.area_container import AreaContainer
from regula.documentreader.webclient.gen.models.image_data import ImageData
from regula.documentreader.webclient.gen.models.light import Light
from regula.documentreader.webclient.gen.models.rectangle_coordinates import RectangleCoordinates
from regula.documentreader.webclient.gen.models.security_feature_type import SecurityFeatureType
from typing import Optional, Set
from typing_extensions import Self

class IdentItem(BaseModel):
    """
    IdentItem
    """ # noqa: E501
    element_type: SecurityFeatureType = Field(alias="ElementType")
    light_index: Light = Field(alias="LightIndex")
    area: Optional[RectangleCoordinates] = Field(default=None, alias="Area")
    image: ImageData = Field(alias="Image")
    etalon_image: ImageData = Field(alias="EtalonImage")
    area_list: Optional[AreaContainer] = Field(default=None, alias="AreaList")
    element_id: Optional[StrictInt] = Field(default=None, alias="ElementID")
    __properties: ClassVar[List[str]] = ["ElementType", "LightIndex", "Area", "Image", "EtalonImage", "AreaList", "ElementID"]

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
        """Create an instance of IdentItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['Image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of etalon_image
        if self.etalon_image:
            _dict['EtalonImage'] = self.etalon_image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of area_list
        if self.area_list:
            _dict['AreaList'] = self.area_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ElementType": obj.get("ElementType"),
            "LightIndex": obj.get("LightIndex"),
            "Area": RectangleCoordinates.from_dict(obj["Area"]) if obj.get("Area") is not None else None,
            "Image": ImageData.from_dict(obj["Image"]) if obj.get("Image") is not None else None,
            "EtalonImage": ImageData.from_dict(obj["EtalonImage"]) if obj.get("EtalonImage") is not None else None,
            "AreaList": AreaContainer.from_dict(obj["AreaList"]) if obj.get("AreaList") is not None else None,
            "ElementID": obj.get("ElementID")
        })
        return _obj


