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
Document processing scenario
"""
class Scenario(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    MRZ = "Mrz"

    BARCODE = "Barcode"

    LOCATE = "Locate"

    OCR = "Ocr"

    DOCTYPE = "DocType"

    MRZ_OR_BARCODE = "MrzOrBarcode"

    MRZ_OR_LOCATE = "MrzOrLocate"

    MRZ_AND_LOCATE = "MrzAndLocate"

    BARCODE_AND_LOCATE = "BarcodeAndLocate"

    MRZ_OR_OCR = "MrzOrOcr"

    MRZ_OR_BARCODE_OR_OCR = "MrzOrBarcodeOrOcr"

    LOCATE_VISUAL_AND_MRZ_OR_OCR = "LocateVisual_And_MrzOrOcr"

    FULL_PROCESS = "FullProcess"

    FULL_AUTH = "FullAuth"

    RUS_STAMP = "RusStamp"

    OCR_FREE = "OcrFree"

    CREDIT_CARD = "CreditCard"

    CAPTURE = "Capture"

    DTC = "DTC"

    allowable_values = [MRZ, BARCODE, LOCATE, OCR, DOCTYPE, MRZ_OR_BARCODE, MRZ_OR_LOCATE, MRZ_AND_LOCATE, BARCODE_AND_LOCATE, MRZ_OR_OCR, MRZ_OR_BARCODE_OR_OCR, LOCATE_VISUAL_AND_MRZ_OR_OCR, FULL_PROCESS, FULL_AUTH, RUS_STAMP, OCR_FREE, CREDIT_CARD, CAPTURE, DTC]  # noqa: E501

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
        """Scenario - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, Scenario):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scenario):
            return True

        return self.to_dict() != other.to_dict()
