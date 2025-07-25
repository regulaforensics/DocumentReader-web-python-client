# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BarcodeType(int, Enum):
    """
    Enumeration contains the types of barcodes that can be processed
    """

    """
    allowed enum values
    """
    UNKNOWN = 0
    CODE128 = 1
    CODE39 = 2
    EAN8 = 3
    ITF = 4
    PDF417 = 5
    STF = 6
    MTF = 7
    IATA = 8
    CODABAR = 9
    UPCA = 10
    CODE93 = 11
    UPCE = 12
    EAN13 = 13
    QRCODE = 14
    AZTEC = 15
    DATAMATRIX = 16
    ALL_1D = 17
    CODE11 = 18
    JABCODE = 19

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BarcodeType from a JSON string"""
        return cls(json.loads(json_str))


