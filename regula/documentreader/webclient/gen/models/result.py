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
class Result(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    DOCUMENT_IMAGE = int("1")

    MRZ_TEXT = int("3")

    BARCODES = int("5")

    VISUAL_GRAPHICS = int("6")

    DOCUMENT_TYPE_CANDIDATES = int("8")

    DOCUMENT_TYPE = int("9")

    LEXICAL_ANALYSIS = int("15")

    RAW_UNCROPPED_IMAGE = int("16")

    VISUAL_TEXT = int("17")

    BARCODE_TEXT = int("18")

    BARCODE_GRAPHICS = int("19")

    AUTHENTICITY = int("20")

    IMAGE_QUALITY = int("30")

    STATUS = int("33")

    PORTRAIT_COMPARISON = int("34")

    TEXT = int("36")

    IMAGES = int("37")

    FINGERPRINT_COMPARISON = int("39")

    ENCRYPTED_RCL = int("49")

    LICENSE = int("50")

    DOCUMENT_POSITION = int("85")

    RFID_RAW_DATA = int("101")

    RFID_TEXT = int("102")

    RFID_GRAPHICS = int("103")

    RFID_BINARY_DATA = int("104")

    RFID_ORIGINAL_GRAPHICS = int("105")

    DTC_VC = int("109")

    allowable_values = [DOCUMENT_IMAGE, MRZ_TEXT, BARCODES, VISUAL_GRAPHICS, DOCUMENT_TYPE_CANDIDATES, DOCUMENT_TYPE, LEXICAL_ANALYSIS, RAW_UNCROPPED_IMAGE, VISUAL_TEXT, BARCODE_TEXT, BARCODE_GRAPHICS, AUTHENTICITY, IMAGE_QUALITY, STATUS, PORTRAIT_COMPARISON, TEXT, IMAGES, FINGERPRINT_COMPARISON, ENCRYPTED_RCL, LICENSE, DOCUMENT_POSITION, RFID_RAW_DATA, RFID_TEXT, RFID_GRAPHICS, RFID_BINARY_DATA, RFID_ORIGINAL_GRAPHICS, DTC_VC]  # noqa: E501

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
        """Result - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, Result):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Result):
            return True

        return self.to_dict() != other.to_dict()
