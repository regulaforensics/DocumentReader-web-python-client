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
Enumeration representing RFID Data Group Types. Constants with prefix  correspond to the informational data groups of ePassport application, with prefix EID_ – those of eID application, with prefix EDL_ – eDL application
"""
class RfidDataGroupTypeTag(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    COM = int("96")

    DG1 = int("97")

    DG2 = int("117")

    DG3 = int("99")

    DG4 = int("118")

    DG5 = int("101")

    DG6 = int("102")

    DG7 = int("103")

    DG8 = int("104")

    DG9 = int("105")

    DG10 = int("106")

    DG11 = int("107")

    DG12 = int("108")

    DG13 = int("109")

    DG14 = int("110")

    DG15 = int("111")

    DG16 = int("112")

    SOD = int("119")

    EID_DG1 = int("97")

    EID_DG2 = int("98")

    EID_DG3 = int("99")

    EID_DG4 = int("100")

    EID_DG5 = int("101")

    EID_DG6 = int("102")

    EID_DG7 = int("103")

    EID_DG8 = int("104")

    EID_DG9 = int("105")

    EID_DG10 = int("106")

    EID_DG11 = int("107")

    EID_DG12 = int("108")

    EID_DG13 = int("109")

    EID_DG14 = int("110")

    EID_DG15 = int("111")

    EID_DG16 = int("112")

    EID_DG17 = int("113")

    EID_DG18 = int("114")

    EID_DG19 = int("115")

    EID_DG20 = int("116")

    EID_DG21 = int("117")

    EDL_COM = int("96")

    EDL_SOD = int("119")

    EDL_CE = int("119")

    EDL_DG1 = int("97")

    EDL_DG2 = int("107")

    EDL_DG3 = int("108")

    EDL_DG4 = int("101")

    EDL_DG5 = int("103")

    EDL_DG6 = int("117")

    EDL_DG7 = int("99")

    EDL_DG8 = int("118")

    EDL_DG9 = int("112")

    EDL_DG11 = int("109")

    EDL_DG12 = int("113")

    EDL_DG14 = int("111")

    _110 = int("110")

    allowable_values = [COM, DG1, DG2, DG3, DG4, DG5, DG6, DG7, DG8, DG9, DG10, DG11, DG12, DG13, DG14, DG15, DG16, SOD, EID_DG1, EID_DG2, EID_DG3, EID_DG4, EID_DG5, EID_DG6, EID_DG7, EID_DG8, EID_DG9, EID_DG10, EID_DG11, EID_DG12, EID_DG13, EID_DG14, EID_DG15, EID_DG16, EID_DG17, EID_DG18, EID_DG19, EID_DG20, EID_DG21, EDL_COM, EDL_SOD, EDL_CE, EDL_DG1, EDL_DG2, EDL_DG3, EDL_DG4, EDL_DG5, EDL_DG6, EDL_DG7, EDL_DG8, EDL_DG9, EDL_DG11, EDL_DG12, EDL_DG14, _110]  # noqa: E501

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
        """RfidDataGroupTypeTag - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, RfidDataGroupTypeTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RfidDataGroupTypeTag):
            return True

        return self.to_dict() != other.to_dict()