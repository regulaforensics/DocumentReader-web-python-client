# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from regula.documentreader.webclient.gen.models.container_list import ContainerList
from regula.documentreader.webclient.gen.models.process_params import ProcessParams
from regula.documentreader.webclient.gen.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.models.process_system_info import ProcessSystemInfo
from typing import Optional, Set
from typing_extensions import Self

class TransactionProcessRequest(BaseModel):
    """
    TransactionProcessRequest
    """ # noqa: E501
    process_param: ProcessParams = Field(alias="processParam")
    list: Optional[List[ProcessRequestImage]] = Field(default=None, alias="List")
    live_portrait: Optional[StrictStr] = Field(default=None, description="Live portrait photo", alias="livePortrait")
    ext_portrait: Optional[StrictStr] = Field(default=None, description="Portrait photo from an external source", alias="extPortrait")
    container_list: Optional[ContainerList] = Field(default=None, alias="ContainerList")
    system_info: Optional[ProcessSystemInfo] = Field(default=None, alias="systemInfo")
    pass_back_object: Optional[Dict[str, Any]] = Field(default=None, description="Free-form object to be included in response. Must be object, not list or simple value. Do not affect document processing. Use it freely to pass your app params. Stored in process logs.", alias="passBackObject")
    dtc: Optional[StrictStr] = Field(default=None, description="Digital Travel Credential (DTC-VC) data in base64 format for processing")
    __properties: ClassVar[List[str]] = ["processParam", "List", "livePortrait", "extPortrait", "ContainerList", "systemInfo", "passBackObject", "dtc"]

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
        """Create an instance of TransactionProcessRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of process_param
        if self.process_param:
            _dict['processParam'] = self.process_param.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in list (list)
        _items = []
        if self.list:
            for _item_list in self.list:
                if _item_list:
                    _items.append(_item_list.to_dict())
            _dict['List'] = _items
        # override the default output from pydantic by calling `to_dict()` of container_list
        if self.container_list:
            _dict['ContainerList'] = self.container_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_info
        if self.system_info:
            _dict['systemInfo'] = self.system_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionProcessRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "processParam": ProcessParams.from_dict(obj["processParam"]) if obj.get("processParam") is not None else None,
            "List": [ProcessRequestImage.from_dict(_item) for _item in obj["List"]] if obj.get("List") is not None else None,
            "livePortrait": obj.get("livePortrait"),
            "extPortrait": obj.get("extPortrait"),
            "ContainerList": ContainerList.from_dict(obj["ContainerList"]) if obj.get("ContainerList") is not None else None,
            "systemInfo": ProcessSystemInfo.from_dict(obj["systemInfo"]) if obj.get("systemInfo") is not None else None,
            "passBackObject": obj.get("passBackObject"),
            "dtc": obj.get("dtc")
        })
        return _obj


