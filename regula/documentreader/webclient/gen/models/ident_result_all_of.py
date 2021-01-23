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


class IdentResultAllOf(object):
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
        'element_type': 'SecurityFeatureType',
        'light_index': 'Light',
        'area': 'RectangleCoordinates',
        'image': 'ImageData',
        'etalon_image': 'ImageData',
        'percent_value': 'int',
        'area_list': 'list[AreaContainer]'
    }

    attribute_map = {
        'element_type': 'ElementType',
        'light_index': 'LightIndex',
        'area': 'Area',
        'image': 'Image',
        'etalon_image': 'EtalonImage',
        'percent_value': 'PercentValue',
        'area_list': 'AreaList'
    }

    def __init__(self, element_type=None, light_index=None, area=None, image=None, etalon_image=None, percent_value=None, area_list=None, local_vars_configuration=None):  # noqa: E501
        """IdentResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._element_type = None
        self._light_index = None
        self._area = None
        self._image = None
        self._etalon_image = None
        self._percent_value = None
        self._area_list = None
        self.discriminator = None

        if element_type is not None:
            self.element_type = element_type
        if light_index is not None:
            self.light_index = light_index
        if area is not None:
            self.area = area
        if image is not None:
            self.image = image
        if etalon_image is not None:
            self.etalon_image = etalon_image
        if percent_value is not None:
            self.percent_value = percent_value
        if area_list is not None:
            self.area_list = area_list

    @property
    def element_type(self):
        """Gets the element_type of this IdentResultAllOf.  # noqa: E501


        :return: The element_type of this IdentResultAllOf.  # noqa: E501
        :rtype: SecurityFeatureType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this IdentResultAllOf.


        :param element_type: The element_type of this IdentResultAllOf.  # noqa: E501
        :type element_type: SecurityFeatureType
        """

        self._element_type = element_type

    @property
    def light_index(self):
        """Gets the light_index of this IdentResultAllOf.  # noqa: E501


        :return: The light_index of this IdentResultAllOf.  # noqa: E501
        :rtype: Light
        """
        return self._light_index

    @light_index.setter
    def light_index(self, light_index):
        """Sets the light_index of this IdentResultAllOf.


        :param light_index: The light_index of this IdentResultAllOf.  # noqa: E501
        :type light_index: Light
        """

        self._light_index = light_index

    @property
    def area(self):
        """Gets the area of this IdentResultAllOf.  # noqa: E501


        :return: The area of this IdentResultAllOf.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this IdentResultAllOf.


        :param area: The area of this IdentResultAllOf.  # noqa: E501
        :type area: RectangleCoordinates
        """

        self._area = area

    @property
    def image(self):
        """Gets the image of this IdentResultAllOf.  # noqa: E501


        :return: The image of this IdentResultAllOf.  # noqa: E501
        :rtype: ImageData
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IdentResultAllOf.


        :param image: The image of this IdentResultAllOf.  # noqa: E501
        :type image: ImageData
        """

        self._image = image

    @property
    def etalon_image(self):
        """Gets the etalon_image of this IdentResultAllOf.  # noqa: E501


        :return: The etalon_image of this IdentResultAllOf.  # noqa: E501
        :rtype: ImageData
        """
        return self._etalon_image

    @etalon_image.setter
    def etalon_image(self, etalon_image):
        """Sets the etalon_image of this IdentResultAllOf.


        :param etalon_image: The etalon_image of this IdentResultAllOf.  # noqa: E501
        :type etalon_image: ImageData
        """

        self._etalon_image = etalon_image

    @property
    def percent_value(self):
        """Gets the percent_value of this IdentResultAllOf.  # noqa: E501

        Probability percent for IMAGE_PATTERN check or element's visibility for IR_VISIBILITY  # noqa: E501

        :return: The percent_value of this IdentResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._percent_value

    @percent_value.setter
    def percent_value(self, percent_value):
        """Sets the percent_value of this IdentResultAllOf.

        Probability percent for IMAGE_PATTERN check or element's visibility for IR_VISIBILITY  # noqa: E501

        :param percent_value: The percent_value of this IdentResultAllOf.  # noqa: E501
        :type percent_value: int
        """

        self._percent_value = percent_value

    @property
    def area_list(self):
        """Gets the area_list of this IdentResultAllOf.  # noqa: E501


        :return: The area_list of this IdentResultAllOf.  # noqa: E501
        :rtype: list[AreaContainer]
        """
        return self._area_list

    @area_list.setter
    def area_list(self, area_list):
        """Sets the area_list of this IdentResultAllOf.


        :param area_list: The area_list of this IdentResultAllOf.  # noqa: E501
        :type area_list: list[AreaContainer]
        """

        self._area_list = area_list

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
        if not isinstance(other, IdentResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
