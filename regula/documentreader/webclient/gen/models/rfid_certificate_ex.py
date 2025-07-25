# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from regula.documentreader.webclient.gen.models.rfid_certificate_origin import RfidCertificateOrigin
from regula.documentreader.webclient.gen.models.rfid_certificate_type import RfidCertificateType
from regula.documentreader.webclient.gen.models.rfid_distinguished_name import RfidDistinguishedName
from regula.documentreader.webclient.gen.models.rfid_error_codes import RFIDErrorCodes
from regula.documentreader.webclient.gen.models.rfid_pki_extension import RfidPkiExtension
from regula.documentreader.webclient.gen.models.rfid_validity import RfidValidity
from regula.documentreader.webclient.gen.models.trf_ft_string import TrfFtString
from typing import Optional, Set
from typing_extensions import Self

class RfidCertificateEx(BaseModel):
    """
    Structure is used to describe the certificate contents used for the digital signature verification of the document security object within the context of the communication session with electronic document.
    """ # noqa: E501
    version: Union[StrictFloat, StrictInt] = Field(description="Version of Certificate ASN.1 structure", alias="Version")
    serial_number: StrictStr = Field(description="Certificate serial number. Base64 encoded.", alias="SerialNumber")
    signature_algorithm: StrictStr = Field(description="Certificate digital signature algorithm identifier (OID); String in the format S1 (S2), where S1 – algorithm name, S2 – identifier (OID string).", alias="SignatureAlgorithm")
    issuer: RfidDistinguishedName = Field(alias="Issuer")
    validity: RfidValidity = Field(alias="Validity")
    subject: RfidDistinguishedName = Field(alias="Subject")
    subject_pk_algorithm: StrictStr = Field(description="Certificate public key algorithm identifier (OID); String in the format S1 (S2), where S1 – algorithm name, S2 – identifier (OID string).", alias="SubjectPKAlgorithm")
    extensions: List[RfidPkiExtension] = Field(description="List of the certificate extensions", alias="Extensions")
    notifications: List[StrictInt] = Field(description="List of remarks arisen during the analysis of the certificate data structure and its validity verification. Can be ParsingErrorCodes or ParsingNotificationCodes enum.", alias="Notifications")
    origin: RfidCertificateOrigin = Field(alias="Origin")
    type: RfidCertificateType = Field(alias="Type")
    file_name: TrfFtString = Field(alias="FileName")
    pa_status: RFIDErrorCodes = Field(alias="PA_Status")
    __properties: ClassVar[List[str]] = ["Version", "SerialNumber", "SignatureAlgorithm", "Issuer", "Validity", "Subject", "SubjectPKAlgorithm", "Extensions", "Notifications", "Origin", "Type", "FileName", "PA_Status"]

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
        """Create an instance of RfidCertificateEx from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of issuer
        if self.issuer:
            _dict['Issuer'] = self.issuer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity
        if self.validity:
            _dict['Validity'] = self.validity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['Subject'] = self.subject.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in extensions (list)
        _items = []
        if self.extensions:
            for _item_extensions in self.extensions:
                if _item_extensions:
                    _items.append(_item_extensions.to_dict())
            _dict['Extensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of file_name
        if self.file_name:
            _dict['FileName'] = self.file_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RfidCertificateEx from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Version": obj.get("Version"),
            "SerialNumber": obj.get("SerialNumber"),
            "SignatureAlgorithm": obj.get("SignatureAlgorithm"),
            "Issuer": RfidDistinguishedName.from_dict(obj["Issuer"]) if obj.get("Issuer") is not None else None,
            "Validity": RfidValidity.from_dict(obj["Validity"]) if obj.get("Validity") is not None else None,
            "Subject": RfidDistinguishedName.from_dict(obj["Subject"]) if obj.get("Subject") is not None else None,
            "SubjectPKAlgorithm": obj.get("SubjectPKAlgorithm"),
            "Extensions": [RfidPkiExtension.from_dict(_item) for _item in obj.get("Extensions", []) if RfidPkiExtension.from_dict(_item) is not None],
            "Notifications": obj.get("Notifications"),
            "Origin": obj.get("Origin"),
            "Type": obj.get("Type"),
            "FileName": TrfFtString.from_dict(obj["FileName"]) if obj.get("FileName") is not None else None,
            "PA_Status": obj.get("PA_Status")
        })
        return _obj


