# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from regula.documentreader.webclient.gen.models.graphic_field import GraphicField
from typing import Optional, Set
from typing_extensions import Self

class GraphicFieldsList(BaseModel):
    """
    GraphicFieldsList
    """ # noqa: E501
    p_array_fields: List[GraphicField] = Field(alias="pArrayFields")
    n_fields: Union[StrictFloat, StrictInt] = Field(description="Number of pArrayFields array elements", alias="nFields")
    __properties: ClassVar[List[str]] = ["pArrayFields", "nFields"]

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
        """Create an instance of GraphicFieldsList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in p_array_fields (list)
        _items = []
        if self.p_array_fields:
            for _item_p_array_fields in self.p_array_fields:
                if _item_p_array_fields:
                    _items.append(_item_p_array_fields.to_dict())
            _dict['pArrayFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GraphicFieldsList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pArrayFields": [GraphicField.from_dict(_item) for _item in obj["pArrayFields"]] if obj.get("pArrayFields") is not None else None,
            "nFields": obj.get("nFields")
        })
        return _obj


