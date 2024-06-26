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
class InlineResponse200(object):
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
        'out_data': 'OutData',
        'in_data': 'InData',
        'tag': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'out_data': 'OutData',
        'in_data': 'InData',
        'tag': 'tag',
        'transaction_id': 'transactionId'
    }

    def __init__(self, out_data=None, in_data=None, tag=None, transaction_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._out_data = None
        self._in_data = None
        self._tag = None
        self._transaction_id = None
        self.discriminator = None

        if out_data is not None:
            self.out_data = out_data
        if in_data is not None:
            self.in_data = in_data
        if tag is not None:
            self.tag = tag
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def out_data(self):
        """Gets the out_data of this InlineResponse200.  # noqa: E501


        :return: The out_data of this InlineResponse200.  # noqa: E501
        :rtype: OutData
        """
        return self._out_data

    @out_data.setter
    def out_data(self, out_data):
        """Sets the out_data of this InlineResponse200.


        :param out_data: The out_data of this InlineResponse200.  # noqa: E501
        :type out_data: OutData
        """

        self._out_data = out_data

    @property
    def in_data(self):
        """Gets the in_data of this InlineResponse200.  # noqa: E501


        :return: The in_data of this InlineResponse200.  # noqa: E501
        :rtype: InData
        """
        return self._in_data

    @in_data.setter
    def in_data(self, in_data):
        """Sets the in_data of this InlineResponse200.


        :param in_data: The in_data of this InlineResponse200.  # noqa: E501
        :type in_data: InData
        """

        self._in_data = in_data

    @property
    def tag(self):
        """Gets the tag of this InlineResponse200.  # noqa: E501


        :return: The tag of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this InlineResponse200.


        :param tag: The tag of this InlineResponse200.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InlineResponse200.  # noqa: E501


        :return: The transaction_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InlineResponse200.


        :param transaction_id: The transaction_id of this InlineResponse200.  # noqa: E501
        :type transaction_id: str
        """

        self._transaction_id = transaction_id

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()
