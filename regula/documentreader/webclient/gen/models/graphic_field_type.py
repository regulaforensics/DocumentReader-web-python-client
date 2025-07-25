# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class GraphicFieldType(int, Enum):
    """
    GraphicFieldType
    """

    """
    allowed enum values
    """
    PORTRAIT = 201
    FINGERPRINT = 202
    EYE = 203
    SIGNATURE = 204
    BAR_CODE = 205
    PROOF_OF_CITIZENSHIP = 206
    DOCUMENT_FRONT = 207
    DOCUMENT_REAR = 208
    COLOR_DYNAMIC = 209
    GHOST_PORTRAIT = 210
    STAMP = 211
    PORTRAIT_OF_CHILD = 212
    CONTACT_CHIP = 213
    OTHER = 250
    FINGER_LEFT_THUMB = 300
    FINGER_LEFT_INDEX = 301
    FINGER_LEFT_MIDDLE = 302
    FINGER_LEFT_RING = 303
    FINGER_LEFT_LITTLE = 304
    FINGER_RIGHT_THUMB = 305
    FINGER_RIGHT_INDEX = 306
    FINGER_RIGHT_MIDDLE = 307
    FINGER_RIGHT_RING = 308
    FINGER_RIGHT_LITTLE = 309
    FINGER_RIGHT_FOUR_FINGERS = 313
    FINGER_LEFT_FOUR_FINGERS = 314
    FINGER_TWO_THUMBS = 315

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GraphicFieldType from a JSON string"""
        return cls(json.loads(json_str))


