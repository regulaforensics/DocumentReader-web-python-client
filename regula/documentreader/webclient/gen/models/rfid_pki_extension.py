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
Extension identifier (OID, ASCII string); Contents of the identifier in the format S1 (S2), where S1 – attribute name, S2 – identifier (OID string)
"""
class RfidPkiExtension(object):
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
        'type': 'str',
        'data': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'data': 'Data'
    }

    def __init__(self, type=None, data=None, local_vars_configuration=None):  # noqa: E501
        """RfidPkiExtension - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._data = None
        self.discriminator = None

        self.type = type
        self.data = data

    @property
    def type(self):
        """Gets the type of this RfidPkiExtension.  # noqa: E501

        Extension identifier (OID, ASCII string); Contents of the identifier in the format S1 (S2), where S1 – attribute name, S2 – identifier (OID string)  # noqa: E501

        :return: The type of this RfidPkiExtension.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RfidPkiExtension.

        Extension identifier (OID, ASCII string); Contents of the identifier in the format S1 (S2), where S1 – attribute name, S2 – identifier (OID string)  # noqa: E501

        :param type: The type of this RfidPkiExtension.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def data(self):
        """Gets the data of this RfidPkiExtension.  # noqa: E501

        Extension binary data. Base64 encoded.  # noqa: E501

        :return: The data of this RfidPkiExtension.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RfidPkiExtension.

        Extension binary data. Base64 encoded.  # noqa: E501

        :param data: The data of this RfidPkiExtension.  # noqa: E501
        :type data: str
        """

        self._data = data

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
        if not isinstance(other, RfidPkiExtension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RfidPkiExtension):
            return True

        return self.to_dict() != other.to_dict()
