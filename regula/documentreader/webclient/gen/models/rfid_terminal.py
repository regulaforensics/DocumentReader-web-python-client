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
from regula.documentreader.webclient.gen.models.rfid_terminal_type import RfidTerminalType
from typing import Optional, Set
from typing_extensions import Self

class RfidTerminal(BaseModel):
    """
    Structure is used to describe the terminal type within the context of the communication session with electronic document
    """ # noqa: E501
    term_type: RfidTerminalType = Field(alias="TermType")
    auth_req: Union[StrictFloat, StrictInt] = Field(description="Declared (set) combination of flags of access rights to the functionality of the document (combination of eRfidTerminalAuthorizationRequirement values)", alias="AuthReq")
    auth_req2: Union[StrictFloat, StrictInt] = Field(description="Declared (set) combination of flags of access rights to the functionality of the document (combination of RfidTerminalAuthorizationRequirement values)", alias="AuthReq2")
    __properties: ClassVar[List[str]] = ["TermType", "AuthReq", "AuthReq2"]

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
        """Create an instance of RfidTerminal from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RfidTerminal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TermType": obj.get("TermType"),
            "AuthReq": obj.get("AuthReq"),
            "AuthReq2": obj.get("AuthReq2")
        })
        return _obj


