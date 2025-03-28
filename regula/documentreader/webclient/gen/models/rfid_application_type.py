# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RfidApplicationType(int, Enum):
    """
    Enumeration contains a set of constants that define the type of application within the context of the communication session with electronic document
    """

    """
    allowed enum values
    """
    UNSPECIFIED = 0
    E_PASSPORT = 1
    E_ID = 2
    E_SIGN = 3
    E_DL = 4
    LDS2_TravelRecords = 5
    LDS2_VisaRecords = 6
    LDS2_AddBiometrics = 7
    eDTC_PC = 8
    ROOT_FILES = 0

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RfidApplicationType from a JSON string"""
        return cls(json.loads(json_str))


