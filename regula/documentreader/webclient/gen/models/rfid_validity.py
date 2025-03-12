# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from regula.documentreader.webclient.gen.models.trf_ft_string import TrfFtString
from typing import Optional, Set
from typing_extensions import Self

class RfidValidity(BaseModel):
    """
    Structure contains information on a certificate validity.
    """ # noqa: E501
    not_before: TrfFtString = Field(alias="NotBefore")
    not_after: TrfFtString = Field(alias="NotAfter")
    __properties: ClassVar[List[str]] = ["NotBefore", "NotAfter"]

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
        """Create an instance of RfidValidity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of not_before
        if self.not_before:
            _dict['NotBefore'] = self.not_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of not_after
        if self.not_after:
            _dict['NotAfter'] = self.not_after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RfidValidity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NotBefore": TrfFtString.from_dict(obj["NotBefore"]) if obj.get("NotBefore") is not None else None,
            "NotAfter": TrfFtString.from_dict(obj["NotAfter"]) if obj.get("NotAfter") is not None else None
        })
        return _obj


