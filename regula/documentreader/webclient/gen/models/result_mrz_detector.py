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
from regula.documentreader.webclient.gen.models.mrz_rows_item import MRZRowsItem
from typing import Optional, Set
from typing_extensions import Self

class ResultMRZDetector(BaseModel):
    """
    ResultMRZDetector
    """ # noqa: E501
    mrz_format: StrictInt = Field(alias="MRZFormat")
    mrz_rows: List[MRZRowsItem] = Field(alias="MRZRows")
    mrz_rows_num: StrictInt = Field(alias="MRZRowsNum")
    bounding_quadrangle: List[Union[StrictFloat, StrictInt]] = Field(alias="boundingQuadrangle")
    __properties: ClassVar[List[str]] = ["MRZFormat", "MRZRows", "MRZRowsNum", "boundingQuadrangle"]

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
        """Create an instance of ResultMRZDetector from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mrz_rows (list)
        _items = []
        if self.mrz_rows:
            for _item_mrz_rows in self.mrz_rows:
                if _item_mrz_rows:
                    _items.append(_item_mrz_rows.to_dict())
            _dict['MRZRows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResultMRZDetector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MRZFormat": obj.get("MRZFormat"),
            "MRZRows": [MRZRowsItem.from_dict(_item) for _item in obj.get("MRZRows", []) if MRZRowsItem.from_dict(_item) is not None],
            "MRZRowsNum": obj.get("MRZRowsNum"),
            "boundingQuadrangle": obj.get("boundingQuadrangle")
        })
        return _obj


