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


class CrossSourceValueComparison(object):
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
        'source_left': 'Source',
        'source_right': 'Source',
        'status': 'CheckResult'
    }

    attribute_map = {
        'source_left': 'sourceLeft',
        'source_right': 'sourceRight',
        'status': 'status'
    }

    def __init__(self, source_left=None, source_right=None, status=None, local_vars_configuration=None):  # noqa: E501
        """CrossSourceValueComparison - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_left = None
        self._source_right = None
        self._status = None
        self.discriminator = None

        self.source_left = source_left
        self.source_right = source_right
        self.status = status

    @property
    def source_left(self):
        """Gets the source_left of this CrossSourceValueComparison.  # noqa: E501


        :return: The source_left of this CrossSourceValueComparison.  # noqa: E501
        :rtype: Source
        """
        return self._source_left

    @source_left.setter
    def source_left(self, source_left):
        """Sets the source_left of this CrossSourceValueComparison.


        :param source_left: The source_left of this CrossSourceValueComparison.  # noqa: E501
        :type source_left: Source
        """
        if self.local_vars_configuration.client_side_validation and source_left is None:  # noqa: E501
            raise ValueError("Invalid value for `source_left`, must not be `None`")  # noqa: E501

        self._source_left = source_left

    @property
    def source_right(self):
        """Gets the source_right of this CrossSourceValueComparison.  # noqa: E501


        :return: The source_right of this CrossSourceValueComparison.  # noqa: E501
        :rtype: Source
        """
        return self._source_right

    @source_right.setter
    def source_right(self, source_right):
        """Sets the source_right of this CrossSourceValueComparison.


        :param source_right: The source_right of this CrossSourceValueComparison.  # noqa: E501
        :type source_right: Source
        """
        if self.local_vars_configuration.client_side_validation and source_right is None:  # noqa: E501
            raise ValueError("Invalid value for `source_right`, must not be `None`")  # noqa: E501

        self._source_right = source_right

    @property
    def status(self):
        """Gets the status of this CrossSourceValueComparison.  # noqa: E501


        :return: The status of this CrossSourceValueComparison.  # noqa: E501
        :rtype: CheckResult
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CrossSourceValueComparison.


        :param status: The status of this CrossSourceValueComparison.  # noqa: E501
        :type status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, CrossSourceValueComparison):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossSourceValueComparison):
            return True

        return self.to_dict() != other.to_dict()
