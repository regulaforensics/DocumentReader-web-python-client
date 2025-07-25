# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RfidAccessControlProcedureType(int, Enum):
    """
    Enumeration contains a set of constants that define the type of authentication or secure data access procedure
    """

    """
    allowed enum values
    """
    UNDEFINED = 0
    BAC = 1
    PACE = 2
    CA = 3
    TA = 4
    AA = 5
    RI = 6
    CARD_INFO = 10
    DTC_INFO = 11

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RfidAccessControlProcedureType from a JSON string"""
        return cls(json.loads(json_str))


