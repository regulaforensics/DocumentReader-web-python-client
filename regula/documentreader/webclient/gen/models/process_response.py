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


class ProcessResponse(object):
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
        'chip_page': 'RfidLocation',
        'processing_finished': 'ProcessingStatus',
        'container_list': 'ContainerList',
        'transaction_info': 'TransactionInfo'
    }

    attribute_map = {
        'chip_page': 'ChipPage',
        'processing_finished': 'ProcessingFinished',
        'container_list': 'ContainerList',
        'transaction_info': 'TransactionInfo'
    }

    def __init__(self, chip_page=None, processing_finished=None, container_list=None, transaction_info=None, local_vars_configuration=None):  # noqa: E501
        """ProcessResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chip_page = None
        self._processing_finished = None
        self._container_list = None
        self._transaction_info = None
        self.discriminator = None

        self.chip_page = chip_page
        self.processing_finished = processing_finished
        self.container_list = container_list
        self.transaction_info = transaction_info

    @property
    def chip_page(self):
        """Gets the chip_page of this ProcessResponse.  # noqa: E501


        :return: The chip_page of this ProcessResponse.  # noqa: E501
        :rtype: RfidLocation
        """
        return self._chip_page

    @chip_page.setter
    def chip_page(self, chip_page):
        """Sets the chip_page of this ProcessResponse.


        :param chip_page: The chip_page of this ProcessResponse.  # noqa: E501
        :type chip_page: RfidLocation
        """
        if self.local_vars_configuration.client_side_validation and chip_page is None:  # noqa: E501
            raise ValueError("Invalid value for `chip_page`, must not be `None`")  # noqa: E501

        self._chip_page = chip_page

    @property
    def processing_finished(self):
        """Gets the processing_finished of this ProcessResponse.  # noqa: E501


        :return: The processing_finished of this ProcessResponse.  # noqa: E501
        :rtype: ProcessingStatus
        """
        return self._processing_finished

    @processing_finished.setter
    def processing_finished(self, processing_finished):
        """Sets the processing_finished of this ProcessResponse.


        :param processing_finished: The processing_finished of this ProcessResponse.  # noqa: E501
        :type processing_finished: ProcessingStatus
        """
        if self.local_vars_configuration.client_side_validation and processing_finished is None:  # noqa: E501
            raise ValueError("Invalid value for `processing_finished`, must not be `None`")  # noqa: E501

        self._processing_finished = processing_finished

    @property
    def container_list(self):
        """Gets the container_list of this ProcessResponse.  # noqa: E501


        :return: The container_list of this ProcessResponse.  # noqa: E501
        :rtype: ContainerList
        """
        return self._container_list

    @container_list.setter
    def container_list(self, container_list):
        """Sets the container_list of this ProcessResponse.


        :param container_list: The container_list of this ProcessResponse.  # noqa: E501
        :type container_list: ContainerList
        """
        if self.local_vars_configuration.client_side_validation and container_list is None:  # noqa: E501
            raise ValueError("Invalid value for `container_list`, must not be `None`")  # noqa: E501

        self._container_list = container_list

    @property
    def transaction_info(self):
        """Gets the transaction_info of this ProcessResponse.  # noqa: E501


        :return: The transaction_info of this ProcessResponse.  # noqa: E501
        :rtype: TransactionInfo
        """
        return self._transaction_info

    @transaction_info.setter
    def transaction_info(self, transaction_info):
        """Sets the transaction_info of this ProcessResponse.


        :param transaction_info: The transaction_info of this ProcessResponse.  # noqa: E501
        :type transaction_info: TransactionInfo
        """
        if self.local_vars_configuration.client_side_validation and transaction_info is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_info`, must not be `None`")  # noqa: E501

        self._transaction_info = transaction_info

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
        if not isinstance(other, ProcessResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessResponse):
            return True

        return self.to_dict() != other.to_dict()
