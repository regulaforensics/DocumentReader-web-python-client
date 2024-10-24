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
class RawImageContainerFieldList(object):
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
        'format': 'str',
        'image': 'str'
    }

    attribute_map = {
        'format': 'format',
        'image': 'image'
    }

    def __init__(self, format=None, image=None, local_vars_configuration=None):  # noqa: E501
        """RawImageContainerFieldList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._format = None
        self._image = None
        self.discriminator = None

        self.format = format
        self.image = image

    @property
    def format(self):
        """Gets the format of this RawImageContainerFieldList.  # noqa: E501

        Image format  # noqa: E501

        :return: The format of this RawImageContainerFieldList.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RawImageContainerFieldList.

        Image format  # noqa: E501

        :param format: The format of this RawImageContainerFieldList.  # noqa: E501
        :type format: str
        """

        self._format = format

    @property
    def image(self):
        """Gets the image of this RawImageContainerFieldList.  # noqa: E501

        Base64 encoded image  # noqa: E501

        :return: The image of this RawImageContainerFieldList.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this RawImageContainerFieldList.

        Base64 encoded image  # noqa: E501

        :param image: The image of this RawImageContainerFieldList.  # noqa: E501
        :type image: str
        """

        self._image = image

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
        if not isinstance(other, RawImageContainerFieldList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawImageContainerFieldList):
            return True

        return self.to_dict() != other.to_dict()
