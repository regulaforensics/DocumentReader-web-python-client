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


class ProcessRequest(object):
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
        'process_param': 'ProcessParams',
        'list': 'list[ProcessRequestImage]',
        'system_info': 'ProcessSystemInfo'
    }

    attribute_map = {
        'process_param': 'processParam',
        'list': 'List',
        'system_info': 'systemInfo'
    }

    def __init__(self, process_param=None, list=None, system_info=None, local_vars_configuration=None):  # noqa: E501
        """ProcessRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._process_param = None
        self._list = None
        self._system_info = None
        self.discriminator = None

        self.process_param = process_param
        self.list = list
        if system_info is not None:
            self.system_info = system_info

    @property
    def process_param(self):
        """Gets the process_param of this ProcessRequest.  # noqa: E501


        :return: The process_param of this ProcessRequest.  # noqa: E501
        :rtype: ProcessParams
        """
        return self._process_param

    @process_param.setter
    def process_param(self, process_param):
        """Sets the process_param of this ProcessRequest.


        :param process_param: The process_param of this ProcessRequest.  # noqa: E501
        :type process_param: ProcessParams
        """
        if self.local_vars_configuration.client_side_validation and process_param is None:  # noqa: E501
            raise ValueError("Invalid value for `process_param`, must not be `None`")  # noqa: E501

        self._process_param = process_param

    @property
    def list(self):
        """Gets the list of this ProcessRequest.  # noqa: E501


        :return: The list of this ProcessRequest.  # noqa: E501
        :rtype: list[ProcessRequestImage]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ProcessRequest.


        :param list: The list of this ProcessRequest.  # noqa: E501
        :type list: list[ProcessRequestImage]
        """
        if self.local_vars_configuration.client_side_validation and list is None:  # noqa: E501
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

    @property
    def system_info(self):
        """Gets the system_info of this ProcessRequest.  # noqa: E501


        :return: The system_info of this ProcessRequest.  # noqa: E501
        :rtype: ProcessSystemInfo
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this ProcessRequest.


        :param system_info: The system_info of this ProcessRequest.  # noqa: E501
        :type system_info: ProcessSystemInfo
        """

        self._system_info = system_info

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
        if not isinstance(other, ProcessRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessRequest):
            return True

        return self.to_dict() != other.to_dict()
