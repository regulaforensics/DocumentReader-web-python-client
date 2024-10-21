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
class TDocBinaryInfo(object):
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
        'rfid_binary_data': 'BinaryData'
    }

    attribute_map = {
        'rfid_binary_data': 'RFID_BINARY_DATA'
    }

    def __init__(self, rfid_binary_data=None, local_vars_configuration=None):  # noqa: E501
        """TDocBinaryInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rfid_binary_data = None
        self.discriminator = None

        self.rfid_binary_data = rfid_binary_data

    @property
    def rfid_binary_data(self):
        """Gets the rfid_binary_data of this TDocBinaryInfo.  # noqa: E501


        :return: The rfid_binary_data of this TDocBinaryInfo.  # noqa: E501
        :rtype: BinaryData
        """
        return self._rfid_binary_data

    @rfid_binary_data.setter
    def rfid_binary_data(self, rfid_binary_data):
        """Sets the rfid_binary_data of this TDocBinaryInfo.


        :param rfid_binary_data: The rfid_binary_data of this TDocBinaryInfo.  # noqa: E501
        :type rfid_binary_data: BinaryData
        """
        if self.local_vars_configuration.client_side_validation and rfid_binary_data is None:  # noqa: E501
            raise ValueError("Invalid value for `rfid_binary_data`, must not be `None`")  # noqa: E501

        self._rfid_binary_data = rfid_binary_data

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
        if not isinstance(other, TDocBinaryInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TDocBinaryInfo):
            return True

        return self.to_dict() != other.to_dict()