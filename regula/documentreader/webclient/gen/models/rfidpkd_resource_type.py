# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RFIDPKDResourceType(int, Enum):
    """
    Enumeration contains a set of constants that define the type of certificate
    """

    """
    allowed enum values
    """
    CERTIFICATE_PA = 0
    CERTIFICATE_TA = 1
    LDIF = 2
    CRL = 3
    ML = 4
    DEFL = 5
    DEVL = 6
    BL = 7
    LDIF_TA = 8
    ML_TA = 9

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RFIDPKDResourceType from a JSON string"""
        return cls(json.loads(json_str))


