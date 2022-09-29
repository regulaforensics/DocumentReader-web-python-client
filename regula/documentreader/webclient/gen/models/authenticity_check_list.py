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
class AuthenticityCheckList(object):
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
        'count': 'int',
        'list': 'list[AuthenticityCheckResult]'
    }

    attribute_map = {
        'count': 'Count',
        'list': 'List'
    }

    def __init__(self, count=None, list=None, local_vars_configuration=None):  # noqa: E501
        """AuthenticityCheckList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        self.list = list

    @property
    def count(self):
        """Gets the count of this AuthenticityCheckList.  # noqa: E501

        Count of items in List  # noqa: E501

        :return: The count of this AuthenticityCheckList.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AuthenticityCheckList.

        Count of items in List  # noqa: E501

        :param count: The count of this AuthenticityCheckList.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def list(self):
        """Gets the list of this AuthenticityCheckList.  # noqa: E501

        Authenticity Check  # noqa: E501

        :return: The list of this AuthenticityCheckList.  # noqa: E501
        :rtype: list[AuthenticityCheckResult]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this AuthenticityCheckList.

        Authenticity Check  # noqa: E501

        :param list: The list of this AuthenticityCheckList.  # noqa: E501
        :type list: list[AuthenticityCheckResult]
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
        if not isinstance(other, AuthenticityCheckList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticityCheckList):
            return True

        return self.to_dict() != other.to_dict()
