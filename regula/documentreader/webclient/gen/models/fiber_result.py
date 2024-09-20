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
class FiberResult(object):
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
        'type': 'int',
        'element_result': 'CheckResult',
        'element_diagnose': 'CheckDiagnose',
        'percent_value': 'int',
        'rect_count': 'int',
        'expected_count': 'int',
        'light_value': 'Light',
        'light_disp': 'int',
        'rect_array': 'list[RectangleCoordinates]',
        'width': 'list[int]',
        'length': 'list[int]',
        'area': 'list[int]',
        'color_values': 'list[int]'
    }

    attribute_map = {
        'type': 'Type',
        'element_result': 'ElementResult',
        'element_diagnose': 'ElementDiagnose',
        'percent_value': 'PercentValue',
        'rect_count': 'RectCount',
        'expected_count': 'ExpectedCount',
        'light_value': 'LightValue',
        'light_disp': 'LightDisp',
        'rect_array': 'RectArray',
        'width': 'Width',
        'length': 'Length',
        'area': 'Area',
        'color_values': 'ColorValues'
    }

    def __init__(self, type=0, element_result=None, element_diagnose=None, percent_value=None, rect_count=None, expected_count=None, light_value=None, light_disp=None, rect_array=None, width=None, length=None, area=None, color_values=None, local_vars_configuration=None):  # noqa: E501
        """FiberResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._element_result = None
        self._element_diagnose = None
        self._percent_value = None
        self._rect_count = None
        self._expected_count = None
        self._light_value = None
        self._light_disp = None
        self._rect_array = None
        self._width = None
        self._length = None
        self._area = None
        self._color_values = None
        self.discriminator = None

        self.type = type
        if element_result is not None:
            self.element_result = element_result
        if element_diagnose is not None:
            self.element_diagnose = element_diagnose
        if percent_value is not None:
            self.percent_value = percent_value
        if rect_count is not None:
            self.rect_count = rect_count
        if expected_count is not None:
            self.expected_count = expected_count
        if light_value is not None:
            self.light_value = light_value
        if light_disp is not None:
            self.light_disp = light_disp
        if rect_array is not None:
            self.rect_array = rect_array
        if width is not None:
            self.width = width
        if length is not None:
            self.length = length
        if area is not None:
            self.area = area
        if color_values is not None:
            self.color_values = color_values

    @property
    def type(self):
        """Gets the type of this FiberResult.  # noqa: E501

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.regulaforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :return: The type of this FiberResult.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FiberResult.

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.regulaforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :param type: The type of this FiberResult.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def element_result(self):
        """Gets the element_result of this FiberResult.  # noqa: E501


        :return: The element_result of this FiberResult.  # noqa: E501
        :rtype: CheckResult
        """
        return self._element_result

    @element_result.setter
    def element_result(self, element_result):
        """Sets the element_result of this FiberResult.


        :param element_result: The element_result of this FiberResult.  # noqa: E501
        :type element_result: CheckResult
        """

        self._element_result = element_result

    @property
    def element_diagnose(self):
        """Gets the element_diagnose of this FiberResult.  # noqa: E501


        :return: The element_diagnose of this FiberResult.  # noqa: E501
        :rtype: CheckDiagnose
        """
        return self._element_diagnose

    @element_diagnose.setter
    def element_diagnose(self, element_diagnose):
        """Sets the element_diagnose of this FiberResult.


        :param element_diagnose: The element_diagnose of this FiberResult.  # noqa: E501
        :type element_diagnose: CheckDiagnose
        """

        self._element_diagnose = element_diagnose

    @property
    def percent_value(self):
        """Gets the percent_value of this FiberResult.  # noqa: E501


        :return: The percent_value of this FiberResult.  # noqa: E501
        :rtype: int
        """
        return self._percent_value

    @percent_value.setter
    def percent_value(self, percent_value):
        """Sets the percent_value of this FiberResult.


        :param percent_value: The percent_value of this FiberResult.  # noqa: E501
        :type percent_value: int
        """

        self._percent_value = percent_value

    @property
    def rect_count(self):
        """Gets the rect_count of this FiberResult.  # noqa: E501

        For UV_Fibers authenticity result type  # noqa: E501

        :return: The rect_count of this FiberResult.  # noqa: E501
        :rtype: int
        """
        return self._rect_count

    @rect_count.setter
    def rect_count(self, rect_count):
        """Sets the rect_count of this FiberResult.

        For UV_Fibers authenticity result type  # noqa: E501

        :param rect_count: The rect_count of this FiberResult.  # noqa: E501
        :type rect_count: int
        """

        self._rect_count = rect_count

    @property
    def expected_count(self):
        """Gets the expected_count of this FiberResult.  # noqa: E501

        Expected fibers number. For UV_Fibers authentication result type  # noqa: E501

        :return: The expected_count of this FiberResult.  # noqa: E501
        :rtype: int
        """
        return self._expected_count

    @expected_count.setter
    def expected_count(self, expected_count):
        """Sets the expected_count of this FiberResult.

        Expected fibers number. For UV_Fibers authentication result type  # noqa: E501

        :param expected_count: The expected_count of this FiberResult.  # noqa: E501
        :type expected_count: int
        """

        self._expected_count = expected_count

    @property
    def light_value(self):
        """Gets the light_value of this FiberResult.  # noqa: E501


        :return: The light_value of this FiberResult.  # noqa: E501
        :rtype: Light
        """
        return self._light_value

    @light_value.setter
    def light_value(self, light_value):
        """Sets the light_value of this FiberResult.


        :param light_value: The light_value of this FiberResult.  # noqa: E501
        :type light_value: Light
        """

        self._light_value = light_value

    @property
    def light_disp(self):
        """Gets the light_disp of this FiberResult.  # noqa: E501

        For UV_Background authentication result type  # noqa: E501

        :return: The light_disp of this FiberResult.  # noqa: E501
        :rtype: int
        """
        return self._light_disp

    @light_disp.setter
    def light_disp(self, light_disp):
        """Sets the light_disp of this FiberResult.

        For UV_Background authentication result type  # noqa: E501

        :param light_disp: The light_disp of this FiberResult.  # noqa: E501
        :type light_disp: int
        """

        self._light_disp = light_disp

    @property
    def rect_array(self):
        """Gets the rect_array of this FiberResult.  # noqa: E501

        Coordinates of located areas for defined fibers type  # noqa: E501

        :return: The rect_array of this FiberResult.  # noqa: E501
        :rtype: list[RectangleCoordinates]
        """
        return self._rect_array

    @rect_array.setter
    def rect_array(self, rect_array):
        """Sets the rect_array of this FiberResult.

        Coordinates of located areas for defined fibers type  # noqa: E501

        :param rect_array: The rect_array of this FiberResult.  # noqa: E501
        :type rect_array: list[RectangleCoordinates]
        """

        self._rect_array = rect_array

    @property
    def width(self):
        """Gets the width of this FiberResult.  # noqa: E501

        Fibers width value for located areas (in pixels)  # noqa: E501

        :return: The width of this FiberResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FiberResult.

        Fibers width value for located areas (in pixels)  # noqa: E501

        :param width: The width of this FiberResult.  # noqa: E501
        :type width: list[int]
        """

        self._width = width

    @property
    def length(self):
        """Gets the length of this FiberResult.  # noqa: E501

        Fibers length value for located areas (in pixels)  # noqa: E501

        :return: The length of this FiberResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this FiberResult.

        Fibers length value for located areas (in pixels)  # noqa: E501

        :param length: The length of this FiberResult.  # noqa: E501
        :type length: list[int]
        """

        self._length = length

    @property
    def area(self):
        """Gets the area of this FiberResult.  # noqa: E501

        Fibers value for areas (in pixels)  # noqa: E501

        :return: The area of this FiberResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this FiberResult.

        Fibers value for areas (in pixels)  # noqa: E501

        :param area: The area of this FiberResult.  # noqa: E501
        :type area: list[int]
        """

        self._area = area

    @property
    def color_values(self):
        """Gets the color_values of this FiberResult.  # noqa: E501

        Fibers color value  # noqa: E501

        :return: The color_values of this FiberResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._color_values

    @color_values.setter
    def color_values(self, color_values):
        """Sets the color_values of this FiberResult.

        Fibers color value  # noqa: E501

        :param color_values: The color_values of this FiberResult.  # noqa: E501
        :type color_values: list[int]
        """

        self._color_values = color_values

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
        if not isinstance(other, FiberResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FiberResult):
            return True

        return self.to_dict() != other.to_dict()
