# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from regula.documentreader.webclient.gen.models.result import Result
from regula.documentreader.webclient.gen.models.result_item import ResultItem
from regula.documentreader.webclient.gen.models.t_doc_binary_info import TDocBinaryInfo
from typing import Optional, Set
from typing_extensions import Self

class DocumentBinaryInfoResult(ResultItem):
    """
    Structure is used to store the data reading results from the RFID-chip in a form of a list of the logically separated data groups.
    """ # noqa: E501
    t_doc_binary_info: TDocBinaryInfo = Field(alias="TDocBinaryInfo")
    __properties: ClassVar[List[str]] = ["buf_length", "light", "list_idx", "page_idx", "result_type", "TDocBinaryInfo"]

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
        """Create an instance of DocumentBinaryInfoResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of t_doc_binary_info
        if self.t_doc_binary_info:
            _dict['TDocBinaryInfo'] = self.t_doc_binary_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentBinaryInfoResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buf_length": obj.get("buf_length"),
            "light": obj.get("light"),
            "list_idx": obj.get("list_idx"),
            "page_idx": obj.get("page_idx"),
            "result_type": obj.get("result_type"),
            "TDocBinaryInfo": TDocBinaryInfo.from_dict(obj["TDocBinaryInfo"]) if obj.get("TDocBinaryInfo") is not None else None
        })
        return _obj


