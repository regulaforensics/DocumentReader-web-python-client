# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.document_type_recognition_result import DocumentTypeRecognitionResult
from regula.documentreader.webclient.gen.models.one_candidate import OneCandidate
from typing import Optional, Set
from typing_extensions import Self

class DocumentTypesCandidatesList(BaseModel):
    """
    DocumentTypesCandidatesList
    """ # noqa: E501
    rec_result: Optional[DocumentTypeRecognitionResult] = Field(default=None, alias="RecResult")
    candidates: Optional[List[OneCandidate]] = Field(default=None, alias="Candidates")
    __properties: ClassVar[List[str]] = ["RecResult", "Candidates"]

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
        """Create an instance of DocumentTypesCandidatesList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in candidates (list)
        _items = []
        if self.candidates:
            for _item_candidates in self.candidates:
                if _item_candidates:
                    _items.append(_item_candidates.to_dict())
            _dict['Candidates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentTypesCandidatesList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RecResult": obj.get("RecResult"),
            "Candidates": [OneCandidate.from_dict(_item) for _item in obj["Candidates"]] if obj.get("Candidates") is not None else None
        })
        return _obj


