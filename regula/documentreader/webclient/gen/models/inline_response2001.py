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
class InlineResponse2001(object):
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
        'transaction_info': 'TransactionInfo',
        'log': 'str',
        'pass_back_object': 'dict(str, object)',
        'more_pages_available': 'int',
        'elapsed_time': 'int'
    }

    attribute_map = {
        'chip_page': 'ChipPage',
        'processing_finished': 'ProcessingFinished',
        'container_list': 'ContainerList',
        'transaction_info': 'TransactionInfo',
        'log': 'log',
        'pass_back_object': 'passBackObject',
        'more_pages_available': 'morePagesAvailable',
        'elapsed_time': 'elapsedTime'
    }

    def __init__(self, chip_page=None, processing_finished=None, container_list=None, transaction_info=None, log=None, pass_back_object=None, more_pages_available=None, elapsed_time=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chip_page = None
        self._processing_finished = None
        self._container_list = None
        self._transaction_info = None
        self._log = None
        self._pass_back_object = None
        self._more_pages_available = None
        self._elapsed_time = None
        self.discriminator = None

        if chip_page is not None:
            self.chip_page = chip_page
        if processing_finished is not None:
            self.processing_finished = processing_finished
        if container_list is not None:
            self.container_list = container_list
        if transaction_info is not None:
            self.transaction_info = transaction_info
        if log is not None:
            self.log = log
        if pass_back_object is not None:
            self.pass_back_object = pass_back_object
        if more_pages_available is not None:
            self.more_pages_available = more_pages_available
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time

    @property
    def chip_page(self):
        """Gets the chip_page of this InlineResponse2001.  # noqa: E501


        :return: The chip_page of this InlineResponse2001.  # noqa: E501
        :rtype: RfidLocation
        """
        return self._chip_page

    @chip_page.setter
    def chip_page(self, chip_page):
        """Sets the chip_page of this InlineResponse2001.


        :param chip_page: The chip_page of this InlineResponse2001.  # noqa: E501
        :type chip_page: RfidLocation
        """

        self._chip_page = chip_page

    @property
    def processing_finished(self):
        """Gets the processing_finished of this InlineResponse2001.  # noqa: E501


        :return: The processing_finished of this InlineResponse2001.  # noqa: E501
        :rtype: ProcessingStatus
        """
        return self._processing_finished

    @processing_finished.setter
    def processing_finished(self, processing_finished):
        """Sets the processing_finished of this InlineResponse2001.


        :param processing_finished: The processing_finished of this InlineResponse2001.  # noqa: E501
        :type processing_finished: ProcessingStatus
        """

        self._processing_finished = processing_finished

    @property
    def container_list(self):
        """Gets the container_list of this InlineResponse2001.  # noqa: E501


        :return: The container_list of this InlineResponse2001.  # noqa: E501
        :rtype: ContainerList
        """
        return self._container_list

    @container_list.setter
    def container_list(self, container_list):
        """Sets the container_list of this InlineResponse2001.


        :param container_list: The container_list of this InlineResponse2001.  # noqa: E501
        :type container_list: ContainerList
        """

        self._container_list = container_list

    @property
    def transaction_info(self):
        """Gets the transaction_info of this InlineResponse2001.  # noqa: E501


        :return: The transaction_info of this InlineResponse2001.  # noqa: E501
        :rtype: TransactionInfo
        """
        return self._transaction_info

    @transaction_info.setter
    def transaction_info(self, transaction_info):
        """Sets the transaction_info of this InlineResponse2001.


        :param transaction_info: The transaction_info of this InlineResponse2001.  # noqa: E501
        :type transaction_info: TransactionInfo
        """

        self._transaction_info = transaction_info

    @property
    def log(self):
        """Gets the log of this InlineResponse2001.  # noqa: E501

        Base64 encoded transaction processing log  # noqa: E501

        :return: The log of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this InlineResponse2001.

        Base64 encoded transaction processing log  # noqa: E501

        :param log: The log of this InlineResponse2001.  # noqa: E501
        :type log: str
        """

        self._log = log

    @property
    def pass_back_object(self):
        """Gets the pass_back_object of this InlineResponse2001.  # noqa: E501

        Free-form object provided in request. See passBackObject property of ProcessRequest.  # noqa: E501

        :return: The pass_back_object of this InlineResponse2001.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._pass_back_object

    @pass_back_object.setter
    def pass_back_object(self, pass_back_object):
        """Sets the pass_back_object of this InlineResponse2001.

        Free-form object provided in request. See passBackObject property of ProcessRequest.  # noqa: E501

        :param pass_back_object: The pass_back_object of this InlineResponse2001.  # noqa: E501
        :type pass_back_object: dict(str, object)
        """

        self._pass_back_object = pass_back_object

    @property
    def more_pages_available(self):
        """Gets the more_pages_available of this InlineResponse2001.  # noqa: E501


        :return: The more_pages_available of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._more_pages_available

    @more_pages_available.setter
    def more_pages_available(self, more_pages_available):
        """Sets the more_pages_available of this InlineResponse2001.


        :param more_pages_available: The more_pages_available of this InlineResponse2001.  # noqa: E501
        :type more_pages_available: int
        """

        self._more_pages_available = more_pages_available

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this InlineResponse2001.  # noqa: E501

        Time the document processing has taken, ms.  # noqa: E501

        :return: The elapsed_time of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this InlineResponse2001.

        Time the document processing has taken, ms.  # noqa: E501

        :param elapsed_time: The elapsed_time of this InlineResponse2001.  # noqa: E501
        :type elapsed_time: int
        """

        self._elapsed_time = elapsed_time

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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001):
            return True

        return self.to_dict() != other.to_dict()
