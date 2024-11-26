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
class DocVisualExtendedField(object):
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
        'field_type': 'object',
        'w_field_type': 'TextFieldType',
        'field_name': 'str',
        'strings_count': 'float',
        'strings_result': 'list[StringRecognitionResult]',
        'buf_length': 'float',
        'buf_text': 'str',
        'field_mask': 'object',
        'validity': 'object',
        'in_comparison': 'object',
        'reserved2': 'object',
        'reserved3': 'object'
    }

    attribute_map = {
        'field_type': 'FieldType',
        'w_field_type': 'wFieldType',
        'field_name': 'FieldName',
        'strings_count': 'StringsCount',
        'strings_result': 'StringsResult',
        'buf_length': 'Buf_Length',
        'buf_text': 'Buf_Text',
        'field_mask': 'FieldMask',
        'validity': 'Validity',
        'in_comparison': 'InComparison',
        'reserved2': 'Reserved2',
        'reserved3': 'Reserved3'
    }

    def __init__(self, field_type=None, w_field_type=None, field_name=None, strings_count=None, strings_result=None, buf_length=None, buf_text=None, field_mask=None, validity=None, in_comparison=None, reserved2=None, reserved3=None, local_vars_configuration=None):  # noqa: E501
        """DocVisualExtendedField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_type = None
        self._w_field_type = None
        self._field_name = None
        self._strings_count = None
        self._strings_result = None
        self._buf_length = None
        self._buf_text = None
        self._field_mask = None
        self._validity = None
        self._in_comparison = None
        self._reserved2 = None
        self._reserved3 = None
        self.discriminator = None

        self.field_type = field_type
        self.w_field_type = w_field_type
        self.field_name = field_name
        self.strings_count = strings_count
        self.strings_result = strings_result
        self.buf_length = buf_length
        self.buf_text = buf_text
        self.field_mask = field_mask
        self.validity = validity
        self.in_comparison = in_comparison
        self.reserved2 = reserved2
        self.reserved3 = reserved3

    @property
    def field_type(self):
        """Gets the field_type of this DocVisualExtendedField.  # noqa: E501


        :return: The field_type of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this DocVisualExtendedField.


        :param field_type: The field_type of this DocVisualExtendedField.  # noqa: E501
        :type field_type: object
        """

        self._field_type = field_type

    @property
    def w_field_type(self):
        """Gets the w_field_type of this DocVisualExtendedField.  # noqa: E501


        :return: The w_field_type of this DocVisualExtendedField.  # noqa: E501
        :rtype: TextFieldType
        """
        return self._w_field_type

    @w_field_type.setter
    def w_field_type(self, w_field_type):
        """Sets the w_field_type of this DocVisualExtendedField.


        :param w_field_type: The w_field_type of this DocVisualExtendedField.  # noqa: E501
        :type w_field_type: TextFieldType
        """
        if self.local_vars_configuration.client_side_validation and w_field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `w_field_type`, must not be `None`")  # noqa: E501

        self._w_field_type = w_field_type

    @property
    def field_name(self):
        """Gets the field_name of this DocVisualExtendedField.  # noqa: E501

        Field symbolic name (null-terminated string)  # noqa: E501

        :return: The field_name of this DocVisualExtendedField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this DocVisualExtendedField.

        Field symbolic name (null-terminated string)  # noqa: E501

        :param field_name: The field_name of this DocVisualExtendedField.  # noqa: E501
        :type field_name: str
        """
        if self.local_vars_configuration.client_side_validation and field_name is None:  # noqa: E501
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def strings_count(self):
        """Gets the strings_count of this DocVisualExtendedField.  # noqa: E501

        Number of StringsResult array elements  # noqa: E501

        :return: The strings_count of this DocVisualExtendedField.  # noqa: E501
        :rtype: float
        """
        return self._strings_count

    @strings_count.setter
    def strings_count(self, strings_count):
        """Sets the strings_count of this DocVisualExtendedField.

        Number of StringsResult array elements  # noqa: E501

        :param strings_count: The strings_count of this DocVisualExtendedField.  # noqa: E501
        :type strings_count: float
        """
        if self.local_vars_configuration.client_side_validation and strings_count is None:  # noqa: E501
            raise ValueError("Invalid value for `strings_count`, must not be `None`")  # noqa: E501

        self._strings_count = strings_count

    @property
    def strings_result(self):
        """Gets the strings_result of this DocVisualExtendedField.  # noqa: E501

        Array of recognizing probabilities for a each line of text field. Only for Result.VISUAL_TEXT and Result.MRZ_TEXT results.  # noqa: E501

        :return: The strings_result of this DocVisualExtendedField.  # noqa: E501
        :rtype: list[StringRecognitionResult]
        """
        return self._strings_result

    @strings_result.setter
    def strings_result(self, strings_result):
        """Sets the strings_result of this DocVisualExtendedField.

        Array of recognizing probabilities for a each line of text field. Only for Result.VISUAL_TEXT and Result.MRZ_TEXT results.  # noqa: E501

        :param strings_result: The strings_result of this DocVisualExtendedField.  # noqa: E501
        :type strings_result: list[StringRecognitionResult]
        """
        if self.local_vars_configuration.client_side_validation and strings_result is None:  # noqa: E501
            raise ValueError("Invalid value for `strings_result`, must not be `None`")  # noqa: E501

        self._strings_result = strings_result

    @property
    def buf_length(self):
        """Gets the buf_length of this DocVisualExtendedField.  # noqa: E501

        Buf_Text text string length  # noqa: E501

        :return: The buf_length of this DocVisualExtendedField.  # noqa: E501
        :rtype: float
        """
        return self._buf_length

    @buf_length.setter
    def buf_length(self, buf_length):
        """Sets the buf_length of this DocVisualExtendedField.

        Buf_Text text string length  # noqa: E501

        :param buf_length: The buf_length of this DocVisualExtendedField.  # noqa: E501
        :type buf_length: float
        """
        if self.local_vars_configuration.client_side_validation and buf_length is None:  # noqa: E501
            raise ValueError("Invalid value for `buf_length`, must not be `None`")  # noqa: E501

        self._buf_length = buf_length

    @property
    def buf_text(self):
        """Gets the buf_text of this DocVisualExtendedField.  # noqa: E501

        Text field data in UTF8 format. Results of reading different lines of a multi-line field are separated by '^'  # noqa: E501

        :return: The buf_text of this DocVisualExtendedField.  # noqa: E501
        :rtype: str
        """
        return self._buf_text

    @buf_text.setter
    def buf_text(self, buf_text):
        """Sets the buf_text of this DocVisualExtendedField.

        Text field data in UTF8 format. Results of reading different lines of a multi-line field are separated by '^'  # noqa: E501

        :param buf_text: The buf_text of this DocVisualExtendedField.  # noqa: E501
        :type buf_text: str
        """
        if self.local_vars_configuration.client_side_validation and buf_text is None:  # noqa: E501
            raise ValueError("Invalid value for `buf_text`, must not be `None`")  # noqa: E501

        self._buf_text = buf_text

    @property
    def field_mask(self):
        """Gets the field_mask of this DocVisualExtendedField.  # noqa: E501


        :return: The field_mask of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._field_mask

    @field_mask.setter
    def field_mask(self, field_mask):
        """Sets the field_mask of this DocVisualExtendedField.


        :param field_mask: The field_mask of this DocVisualExtendedField.  # noqa: E501
        :type field_mask: object
        """

        self._field_mask = field_mask

    @property
    def validity(self):
        """Gets the validity of this DocVisualExtendedField.  # noqa: E501


        :return: The validity of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this DocVisualExtendedField.


        :param validity: The validity of this DocVisualExtendedField.  # noqa: E501
        :type validity: object
        """

        self._validity = validity

    @property
    def in_comparison(self):
        """Gets the in_comparison of this DocVisualExtendedField.  # noqa: E501


        :return: The in_comparison of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._in_comparison

    @in_comparison.setter
    def in_comparison(self, in_comparison):
        """Sets the in_comparison of this DocVisualExtendedField.


        :param in_comparison: The in_comparison of this DocVisualExtendedField.  # noqa: E501
        :type in_comparison: object
        """

        self._in_comparison = in_comparison

    @property
    def reserved2(self):
        """Gets the reserved2 of this DocVisualExtendedField.  # noqa: E501


        :return: The reserved2 of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """Sets the reserved2 of this DocVisualExtendedField.


        :param reserved2: The reserved2 of this DocVisualExtendedField.  # noqa: E501
        :type reserved2: object
        """

        self._reserved2 = reserved2

    @property
    def reserved3(self):
        """Gets the reserved3 of this DocVisualExtendedField.  # noqa: E501


        :return: The reserved3 of this DocVisualExtendedField.  # noqa: E501
        :rtype: object
        """
        return self._reserved3

    @reserved3.setter
    def reserved3(self, reserved3):
        """Sets the reserved3 of this DocVisualExtendedField.


        :param reserved3: The reserved3 of this DocVisualExtendedField.  # noqa: E501
        :type reserved3: object
        """

        self._reserved3 = reserved3

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
        if not isinstance(other, DocVisualExtendedField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocVisualExtendedField):
            return True

        return self.to_dict() != other.to_dict()
