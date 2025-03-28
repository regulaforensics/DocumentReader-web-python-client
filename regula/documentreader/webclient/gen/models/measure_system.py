# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MeasureSystem(int, Enum):
    """
    MeasureSystem
    """

    """
    allowed enum values
    """
    METRIC = 0
    IMPERIAL = 1

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MeasureSystem from a JSON string"""
        return cls(json.loads(json_str))


