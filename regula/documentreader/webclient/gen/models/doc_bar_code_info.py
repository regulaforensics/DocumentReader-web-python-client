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
from regula.documentreader.webclient.gen.models.doc_bar_code_info_fields_list import DocBarCodeInfoFieldsList
from regula.documentreader.webclient.gen.models.result_item import ResultItem
from typing import Optional, Set
from typing_extensions import Self

class DocBarCodeInfo(ResultItem):
    """
    Raw data from BarCodes
    """ # noqa: E501
    doc_bar_code_info: DocBarCodeInfoFieldsList = Field(alias="DocBarCodeInfo")
    __properties: ClassVar[List[str]] = ["buf_length", "light", "list_idx", "page_idx", "result_type", "DocBarCodeInfo"]

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
        """Create an instance of DocBarCodeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of doc_bar_code_info
        if self.doc_bar_code_info:
            _dict['DocBarCodeInfo'] = self.doc_bar_code_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocBarCodeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buf_length": obj.get("buf_length"),
            "light": obj.get("light"),
            "list_idx": obj.get("list_idx"),
            "page_idx": obj.get("page_idx"),
            "result_type": obj.get("result_type") if obj.get("result_type") is not None else 0,
            "DocBarCodeInfo": DocBarCodeInfoFieldsList.from_dict(obj["DocBarCodeInfo"]) if obj.get("DocBarCodeInfo") is not None else None
        })
        return _obj


