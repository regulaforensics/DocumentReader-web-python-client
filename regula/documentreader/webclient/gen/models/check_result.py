# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CheckResult(int, Enum):
    """
    0 - result is negative; 1 - result is positive; 2 - сheck was not performed
    """

    """
    allowed enum values
    """
    ERROR = 0
    OK = 1
    WAS_NOT_DONE = 2

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CheckResult from a JSON string"""
        return cls(json.loads(json_str))


