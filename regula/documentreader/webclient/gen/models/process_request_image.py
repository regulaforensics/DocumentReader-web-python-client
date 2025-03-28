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
class ProcessRequestImage(object):
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
        'image_data': 'ImageData',
        'light': 'Light',
        'page_idx': 'int'
    }

    attribute_map = {
        'image_data': 'ImageData',
        'light': 'light',
        'page_idx': 'page_idx'
    }

    def __init__(self, image_data=None, light=None, page_idx=None, local_vars_configuration=None):  # noqa: E501
        """ProcessRequestImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image_data = None
        self._light = None
        self._page_idx = None
        self.discriminator = None

        if image_data is not None:
            self.image_data = image_data
        if light is not None:
            self.light = light
        if page_idx is not None:
            self.page_idx = page_idx

    @property
    def image_data(self):
        """Gets the image_data of this ProcessRequestImage.  # noqa: E501


        :return: The image_data of this ProcessRequestImage.  # noqa: E501
        :rtype: ImageData
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """Sets the image_data of this ProcessRequestImage.


        :param image_data: The image_data of this ProcessRequestImage.  # noqa: E501
        :type image_data: ImageData
        """

        self._image_data = image_data

    @property
    def light(self):
        """Gets the light of this ProcessRequestImage.  # noqa: E501


        :return: The light of this ProcessRequestImage.  # noqa: E501
        :rtype: Light
        """
        return self._light

    @light.setter
    def light(self, light):
        """Sets the light of this ProcessRequestImage.


        :param light: The light of this ProcessRequestImage.  # noqa: E501
        :type light: Light
        """

        self._light = light

    @property
    def page_idx(self):
        """Gets the page_idx of this ProcessRequestImage.  # noqa: E501

        page/image number  # noqa: E501

        :return: The page_idx of this ProcessRequestImage.  # noqa: E501
        :rtype: int
        """
        return self._page_idx

    @page_idx.setter
    def page_idx(self, page_idx):
        """Sets the page_idx of this ProcessRequestImage.

        page/image number  # noqa: E501

        :param page_idx: The page_idx of this ProcessRequestImage.  # noqa: E501
        :type page_idx: int
        """

        self._page_idx = page_idx

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
        if not isinstance(other, ProcessRequestImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessRequestImage):
            return True

        return self.to_dict() != other.to_dict()
