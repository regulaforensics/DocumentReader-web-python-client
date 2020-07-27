# coding: utf-8

"""
    Regula Document Reader Web API

    Regula Document Reader Web API  # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.configuration import Configuration


class RfidOrigin(object):
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
        'dg': 'int',
        'dg_tag': 'int',
        'tag_entry': 'int',
        'entry_view': 'int'
    }

    attribute_map = {
        'dg': 'dg',
        'dg_tag': 'dgTag',
        'tag_entry': 'tagEntry',
        'entry_view': 'entryView'
    }

    def __init__(self, dg=None, dg_tag=None, tag_entry=None, entry_view=None, local_vars_configuration=None):  # noqa: E501
        """RfidOrigin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dg = None
        self._dg_tag = None
        self._tag_entry = None
        self._entry_view = None
        self.discriminator = None

        self.dg = dg
        if dg_tag is not None:
            self.dg_tag = dg_tag
        if tag_entry is not None:
            self.tag_entry = tag_entry
        if entry_view is not None:
            self.entry_view = entry_view

    @property
    def dg(self):
        """Gets the dg of this RfidOrigin.  # noqa: E501

        Source data group file  # noqa: E501

        :return: The dg of this RfidOrigin.  # noqa: E501
        :rtype: int
        """
        return self._dg

    @dg.setter
    def dg(self, dg):
        """Sets the dg of this RfidOrigin.

        Source data group file  # noqa: E501

        :param dg: The dg of this RfidOrigin.  # noqa: E501
        :type dg: int
        """
        if self.local_vars_configuration.client_side_validation and dg is None:  # noqa: E501
            raise ValueError("Invalid value for `dg`, must not be `None`")  # noqa: E501

        self._dg = dg

    @property
    def dg_tag(self):
        """Gets the dg_tag of this RfidOrigin.  # noqa: E501

        Index of the source record of the image with biometric information in the information data group  # noqa: E501

        :return: The dg_tag of this RfidOrigin.  # noqa: E501
        :rtype: int
        """
        return self._dg_tag

    @dg_tag.setter
    def dg_tag(self, dg_tag):
        """Sets the dg_tag of this RfidOrigin.

        Index of the source record of the image with biometric information in the information data group  # noqa: E501

        :param dg_tag: The dg_tag of this RfidOrigin.  # noqa: E501
        :type dg_tag: int
        """

        self._dg_tag = dg_tag

    @property
    def tag_entry(self):
        """Gets the tag_entry of this RfidOrigin.  # noqa: E501

        Index of the template in the record with biometric data  # noqa: E501

        :return: The tag_entry of this RfidOrigin.  # noqa: E501
        :rtype: int
        """
        return self._tag_entry

    @tag_entry.setter
    def tag_entry(self, tag_entry):
        """Sets the tag_entry of this RfidOrigin.

        Index of the template in the record with biometric data  # noqa: E501

        :param tag_entry: The tag_entry of this RfidOrigin.  # noqa: E501
        :type tag_entry: int
        """

        self._tag_entry = tag_entry

    @property
    def entry_view(self):
        """Gets the entry_view of this RfidOrigin.  # noqa: E501

        Index of the variant of the biometric data template  # noqa: E501

        :return: The entry_view of this RfidOrigin.  # noqa: E501
        :rtype: int
        """
        return self._entry_view

    @entry_view.setter
    def entry_view(self, entry_view):
        """Sets the entry_view of this RfidOrigin.

        Index of the variant of the biometric data template  # noqa: E501

        :param entry_view: The entry_view of this RfidOrigin.  # noqa: E501
        :type entry_view: int
        """

        self._entry_view = entry_view

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
        if not isinstance(other, RfidOrigin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RfidOrigin):
            return True

        return self.to_dict() != other.to_dict()
