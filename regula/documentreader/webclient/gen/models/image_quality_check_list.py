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
class ImageQualityCheckList(object):
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
        'result': 'CheckResult',
        'list': 'list[ImageQualityCheck]'
    }

    attribute_map = {
        'result': 'result',
        'list': 'List'
    }

    def __init__(self, result=None, list=None, local_vars_configuration=None):  # noqa: E501
        """ImageQualityCheckList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._list = None
        self.discriminator = None

        self.result = result
        self.list = list

    @property
    def result(self):
        """Gets the result of this ImageQualityCheckList.  # noqa: E501


        :return: The result of this ImageQualityCheckList.  # noqa: E501
        :rtype: CheckResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ImageQualityCheckList.


        :param result: The result of this ImageQualityCheckList.  # noqa: E501
        :type result: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def list(self):
        """Gets the list of this ImageQualityCheckList.  # noqa: E501


        :return: The list of this ImageQualityCheckList.  # noqa: E501
        :rtype: list[ImageQualityCheck]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ImageQualityCheckList.


        :param list: The list of this ImageQualityCheckList.  # noqa: E501
        :type list: list[ImageQualityCheck]
        """
        if self.local_vars_configuration.client_side_validation and list is None:  # noqa: E501
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

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
        if not isinstance(other, ImageQualityCheckList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageQualityCheckList):
            return True

        return self.to_dict() != other.to_dict()