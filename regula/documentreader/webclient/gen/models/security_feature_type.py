# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


"""

"""
class SecurityFeatureType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    Blank = int("0")

    Fill = int("1")

    Photo = int("2")

    MRZ = int("3")

    FalseLuminescene = int("4")

    HoloSimple = int("5")

    HoloVerifyStatic = int("6")

    HoloVerifyMultyStatic = int("7")

    HoloVerifyDinamic = int("8")

    PatternNotInterrupted = int("9")

    PatternNotShifted = int("10")

    PatternSameColors = int("11")

    PatternIRInvisible = int("12")

    PhotoSizeCheck = int("13")

    Portrait_Comparison_vsGhost = int("14")

    Portrait_Comparison_vsRFID = int("15")

    Portrait_Comparison_vsVisual = int("16")

    Barcode = int("17")

    Pattern_DifferentLinesThickness = int("18")

    Portrait_Comparison_vsCamera = int("19")

    Portrait_Comparison_RFIDvsCamera = int("20")

    GhostPhoto = int("21")

    ClearGhostPhoto = int("22")

    InvisibleObject = int("23")

    LowContrastObject = int("24")

    Photo_Color = int("25")

    Photo_Shape = int("26")

    Photo_Corners = int("27")

    Document_Cancelling_Detector = int("28")

    Portrait_Comparison_ExtvsVisual = int("29")

    Portrait_Comparison_ExtvsRFID = int("30")

    Portrait_Comparison_ExtvsLive = int("31")

    allowable_values = [Blank, Fill, Photo, MRZ, FalseLuminescene, HoloSimple, HoloVerifyStatic, HoloVerifyMultyStatic, HoloVerifyDinamic, PatternNotInterrupted, PatternNotShifted, PatternSameColors, PatternIRInvisible, PhotoSizeCheck, Portrait_Comparison_vsGhost, Portrait_Comparison_vsRFID, Portrait_Comparison_vsVisual, Barcode, Pattern_DifferentLinesThickness, Portrait_Comparison_vsCamera, Portrait_Comparison_RFIDvsCamera, GhostPhoto, ClearGhostPhoto, InvisibleObject, LowContrastObject, Photo_Color, Photo_Shape, Photo_Corners, Document_Cancelling_Detector, Portrait_Comparison_ExtvsVisual, Portrait_Comparison_ExtvsRFID, Portrait_Comparison_ExtvsLive]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """SecurityFeatureType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityFeatureType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityFeatureType):
            return True

        return self.to_dict() != other.to_dict()
