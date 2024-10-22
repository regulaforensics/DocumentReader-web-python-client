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
class GraphicFieldType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    PORTRAIT = int("201")

    FINGERPRINT = int("202")

    EYE = int("203")

    SIGNATURE = int("204")

    BAR_CODE = int("205")

    PROOF_OF_CITIZENSHIP = int("206")

    DOCUMENT_FRONT = int("207")

    DOCUMENT_REAR = int("208")

    COLOR_DYNAMIC = int("209")

    GHOST_PORTRAIT = int("210")

    STAMP = int("211")

    PORTRAIT_OF_CHILD = int("212")

    CONTACT_CHIP = int("213")

    OTHER = int("250")

    FINGER_LEFT_THUMB = int("300")

    FINGER_LEFT_INDEX = int("301")

    FINGER_LEFT_MIDDLE = int("302")

    FINGER_LEFT_RING = int("303")

    FINGER_LEFT_LITTLE = int("304")

    FINGER_RIGHT_THUMB = int("305")

    FINGER_RIGHT_INDEX = int("306")

    FINGER_RIGHT_MIDDLE = int("307")

    FINGER_RIGHT_RING = int("308")

    FINGER_RIGHT_LITTLE = int("309")

    FINGER_RIGHT_FOUR_FINGERS = int("313")

    FINGER_LEFT_FOUR_FINGERS = int("314")

    FINGER_TWO_THUMBS = int("315")

    allowable_values = [PORTRAIT, FINGERPRINT, EYE, SIGNATURE, BAR_CODE, PROOF_OF_CITIZENSHIP, DOCUMENT_FRONT, DOCUMENT_REAR, COLOR_DYNAMIC, GHOST_PORTRAIT, STAMP, PORTRAIT_OF_CHILD, CONTACT_CHIP, OTHER, FINGER_LEFT_THUMB, FINGER_LEFT_INDEX, FINGER_LEFT_MIDDLE, FINGER_LEFT_RING, FINGER_LEFT_LITTLE, FINGER_RIGHT_THUMB, FINGER_RIGHT_INDEX, FINGER_RIGHT_MIDDLE, FINGER_RIGHT_RING, FINGER_RIGHT_LITTLE, FINGER_RIGHT_FOUR_FINGERS, FINGER_LEFT_FOUR_FINGERS, FINGER_TWO_THUMBS]  # noqa: E501

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
        """GraphicFieldType - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, GraphicFieldType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphicFieldType):
            return True

        return self.to_dict() != other.to_dict()
