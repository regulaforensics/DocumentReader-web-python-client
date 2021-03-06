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
class ImageQA(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dpi_threshold': 'int',
        'angle_threshold': 'int'
    }

    attribute_map = {
        'dpi_threshold': 'dpiThreshold',
        'angle_threshold': 'angleThreshold'
    }

    def __init__(self, dpi_threshold=150, angle_threshold=5, local_vars_configuration=None):  # noqa: E501
        """ImageQA - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dpi_threshold = None
        self._angle_threshold = None
        self.discriminator = None

        if dpi_threshold is not None:
            self.dpi_threshold = dpi_threshold
        if angle_threshold is not None:
            self.angle_threshold = angle_threshold

    @property
    def dpi_threshold(self):
        """Gets the dpi_threshold of this ImageQA.  # noqa: E501

        This parameter sets threshold for Image QA check of the presented document physical dpi. If actual document dpi is below this threshold, check will fail.  # noqa: E501

        :return: The dpi_threshold of this ImageQA.  # noqa: E501
        :rtype: int
        """
        return self._dpi_threshold

    @dpi_threshold.setter
    def dpi_threshold(self, dpi_threshold):
        """Sets the dpi_threshold of this ImageQA.

        This parameter sets threshold for Image QA check of the presented document physical dpi. If actual document dpi is below this threshold, check will fail.  # noqa: E501

        :param dpi_threshold: The dpi_threshold of this ImageQA.  # noqa: E501
        :type dpi_threshold: int
        """

        self._dpi_threshold = dpi_threshold

    @property
    def angle_threshold(self):
        """Gets the angle_threshold of this ImageQA.  # noqa: E501

        This parameter sets threshold for Image QA check of the presented document perspective angle in degrees. If actual document perspective angle is above this threshold, check will fail.  # noqa: E501

        :return: The angle_threshold of this ImageQA.  # noqa: E501
        :rtype: int
        """
        return self._angle_threshold

    @angle_threshold.setter
    def angle_threshold(self, angle_threshold):
        """Sets the angle_threshold of this ImageQA.

        This parameter sets threshold for Image QA check of the presented document perspective angle in degrees. If actual document perspective angle is above this threshold, check will fail.  # noqa: E501

        :param angle_threshold: The angle_threshold of this ImageQA.  # noqa: E501
        :type angle_threshold: int
        """

        self._angle_threshold = angle_threshold

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
        if not isinstance(other, ImageQA):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageQA):
            return True

        return self.to_dict() != other.to_dict()
