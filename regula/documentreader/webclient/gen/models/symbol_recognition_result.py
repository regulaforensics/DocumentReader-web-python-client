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
Describes a single character recognition results in the text field line
"""
class SymbolRecognitionResult(object):
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
        'symbol_rect': 'RectangleCoordinates',
        'list_of_candidates': 'list[SymbolCandidate]'
    }

    attribute_map = {
        'symbol_rect': 'SymbolRect',
        'list_of_candidates': 'ListOfCandidates'
    }

    def __init__(self, symbol_rect=None, list_of_candidates=None, local_vars_configuration=None):  # noqa: E501
        """SymbolRecognitionResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol_rect = None
        self._list_of_candidates = None
        self.discriminator = None

        self.symbol_rect = symbol_rect
        self.list_of_candidates = list_of_candidates

    @property
    def symbol_rect(self):
        """Gets the symbol_rect of this SymbolRecognitionResult.  # noqa: E501


        :return: The symbol_rect of this SymbolRecognitionResult.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._symbol_rect

    @symbol_rect.setter
    def symbol_rect(self, symbol_rect):
        """Sets the symbol_rect of this SymbolRecognitionResult.


        :param symbol_rect: The symbol_rect of this SymbolRecognitionResult.  # noqa: E501
        :type symbol_rect: RectangleCoordinates
        """
        if self.local_vars_configuration.client_side_validation and symbol_rect is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol_rect`, must not be `None`")  # noqa: E501

        self._symbol_rect = symbol_rect

    @property
    def list_of_candidates(self):
        """Gets the list_of_candidates of this SymbolRecognitionResult.  # noqa: E501

        Array of candidate characters. Sorted in descending order of recognition probabilities (the first element has highest probability)  # noqa: E501

        :return: The list_of_candidates of this SymbolRecognitionResult.  # noqa: E501
        :rtype: list[SymbolCandidate]
        """
        return self._list_of_candidates

    @list_of_candidates.setter
    def list_of_candidates(self, list_of_candidates):
        """Sets the list_of_candidates of this SymbolRecognitionResult.

        Array of candidate characters. Sorted in descending order of recognition probabilities (the first element has highest probability)  # noqa: E501

        :param list_of_candidates: The list_of_candidates of this SymbolRecognitionResult.  # noqa: E501
        :type list_of_candidates: list[SymbolCandidate]
        """
        if self.local_vars_configuration.client_side_validation and list_of_candidates is None:  # noqa: E501
            raise ValueError("Invalid value for `list_of_candidates`, must not be `None`")  # noqa: E501

        self._list_of_candidates = list_of_candidates

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
        if not isinstance(other, SymbolRecognitionResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SymbolRecognitionResult):
            return True

        return self.to_dict() != other.to_dict()
