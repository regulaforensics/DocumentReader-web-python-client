# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RfidDataGroupTypeTag(int, Enum):
    """
    Enumeration representing RFID Data Group Types. Constants with prefix  correspond to the informational data groups of ePassport application, with prefix EID_ – those of eID application, with prefix EDL_ – eDL application
    """

    """
    allowed enum values
    """
    COM = 96
    DG1 = 97
    DG2 = 117
    DG3 = 99
    DG4 = 118
    DG5 = 101
    DG6 = 102
    DG7 = 103
    DG8 = 104
    DG9 = 105
    DG10 = 106
    DG11 = 107
    DG12 = 108
    DG13 = 109
    DG14 = 110
    DG15 = 111
    DG16 = 112
    SOD = 119
    DG17 = 113
    DG18 = 114
    DG22 = 115
    DG23 = 116
    DG24 = 98
    EID_DG1 = 97
    EID_DG2 = 98
    EID_DG3 = 99
    EID_DG4 = 100
    EID_DG5 = 101
    EID_DG6 = 102
    EID_DG7 = 103
    EID_DG8 = 104
    EID_DG9 = 105
    EID_DG10 = 106
    EID_DG11 = 107
    EID_DG12 = 108
    EID_DG13 = 109
    EID_DG14 = 110
    EID_DG15 = 111
    EID_DG16 = 112
    EID_DG17 = 113
    EID_DG18 = 114
    EID_DG19 = 115
    EID_DG20 = 116
    EID_DG21 = 117
    EDL_COM = 96
    EDL_SOD = 119
    EDL_CE = 83
    EDL_DG1 = 97
    EDL_DG2 = 107
    EDL_DG3 = 108
    EDL_DG4 = 101
    EDL_DG5 = 103
    EDL_DG6 = 117
    EDL_DG7 = 99
    EDL_DG8 = 118
    EDL_DG9 = 112
    EDL_DG11 = 109
    EDL_DG12 = 113
    EDL_DG13 = 111
    EDL_DG14 = 110

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RfidDataGroupTypeTag from a JSON string"""
        return cls(json.loads(json_str))


