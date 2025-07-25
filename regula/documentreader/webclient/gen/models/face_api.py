# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.face_api_search import FaceApiSearch
from typing import Optional, Set
from typing_extensions import Self

class FaceApi(BaseModel):
    """
    FaceApi
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="The URL of the Regula Face Web service to be used.")
    mode: Optional[StrictStr] = Field(default=None, description="The processing mode: \"match\" or \"match+search\".")
    search: Optional[FaceApiSearch] = None
    threshold: Optional[StrictInt] = Field(default=None, description="The similarity threshold, 0-100. Above 75 means that the faces' similarity is verified, below 75 is not.")
    service_timeout: Optional[StrictInt] = Field(default=None, description="The Regula Face Web service requests timeout, ms.", alias="serviceTimeout")
    proxy: Optional[StrictStr] = Field(default=None, description="Proxy to use, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXY.html\" target=\"_blank\">cURL standard</a>.")
    proxy_userpwd: Optional[StrictStr] = Field(default=None, description="Username and password to use for proxy authentication, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYUSERPWD.html\" target=\"_blank\">cURL standard</a>.")
    proxy_type: Optional[StrictInt] = Field(default=None, description="Proxy protocol type, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYTYPE.html\" target=\"_blank\">cURL standard</a>.")
    child_age_threshold: Optional[StrictInt] = Field(default=None, description="The age threshold for the portrait comparison. Default: 13.", alias="childAgeThreshold")
    child_doc_validity_years: Optional[StrictInt] = Field(default=None, description="Estimated duration of validity for a child's passport, years. Default: 5.", alias="childDocValidityYears")
    __properties: ClassVar[List[str]] = ["url", "mode", "search", "threshold", "serviceTimeout", "proxy", "proxy_userpwd", "proxy_type", "childAgeThreshold", "childDocValidityYears"]

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
        """Create an instance of FaceApi from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaceApi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "mode": obj.get("mode"),
            "search": FaceApiSearch.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "threshold": obj.get("threshold"),
            "serviceTimeout": obj.get("serviceTimeout"),
            "proxy": obj.get("proxy"),
            "proxy_userpwd": obj.get("proxy_userpwd"),
            "proxy_type": obj.get("proxy_type"),
            "childAgeThreshold": obj.get("childAgeThreshold"),
            "childDocValidityYears": obj.get("childDocValidityYears")
        })
        return _obj


