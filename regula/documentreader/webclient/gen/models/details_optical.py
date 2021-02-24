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
class DetailsOptical(object):
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
        'overall_status': 'CheckResult',
        'doc_type': 'CheckResult',
        'expiry': 'CheckResult',
        'image_qa': 'CheckResult',
        'mrz': 'CheckResult',
        'pages_count': 'int',
        'security': 'CheckResult',
        'text': 'CheckResult'
    }

    attribute_map = {
        'overall_status': 'overallStatus',
        'doc_type': 'docType',
        'expiry': 'expiry',
        'image_qa': 'imageQA',
        'mrz': 'mrz',
        'pages_count': 'pagesCount',
        'security': 'security',
        'text': 'text'
    }

    def __init__(self, overall_status=None, doc_type=None, expiry=None, image_qa=None, mrz=None, pages_count=None, security=None, text=None, local_vars_configuration=None):  # noqa: E501
        """DetailsOptical - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_status = None
        self._doc_type = None
        self._expiry = None
        self._image_qa = None
        self._mrz = None
        self._pages_count = None
        self._security = None
        self._text = None
        self.discriminator = None

        self.overall_status = overall_status
        self.doc_type = doc_type
        self.expiry = expiry
        self.image_qa = image_qa
        self.mrz = mrz
        self.pages_count = pages_count
        self.security = security
        self.text = text

    @property
    def overall_status(self):
        """Gets the overall_status of this DetailsOptical.  # noqa: E501


        :return: The overall_status of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this DetailsOptical.


        :param overall_status: The overall_status of this DetailsOptical.  # noqa: E501
        :type overall_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and overall_status is None:  # noqa: E501
            raise ValueError("Invalid value for `overall_status`, must not be `None`")  # noqa: E501

        self._overall_status = overall_status

    @property
    def doc_type(self):
        """Gets the doc_type of this DetailsOptical.  # noqa: E501


        :return: The doc_type of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this DetailsOptical.


        :param doc_type: The doc_type of this DetailsOptical.  # noqa: E501
        :type doc_type: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and doc_type is None:  # noqa: E501
            raise ValueError("Invalid value for `doc_type`, must not be `None`")  # noqa: E501

        self._doc_type = doc_type

    @property
    def expiry(self):
        """Gets the expiry of this DetailsOptical.  # noqa: E501


        :return: The expiry of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this DetailsOptical.


        :param expiry: The expiry of this DetailsOptical.  # noqa: E501
        :type expiry: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and expiry is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must not be `None`")  # noqa: E501

        self._expiry = expiry

    @property
    def image_qa(self):
        """Gets the image_qa of this DetailsOptical.  # noqa: E501


        :return: The image_qa of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._image_qa

    @image_qa.setter
    def image_qa(self, image_qa):
        """Sets the image_qa of this DetailsOptical.


        :param image_qa: The image_qa of this DetailsOptical.  # noqa: E501
        :type image_qa: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and image_qa is None:  # noqa: E501
            raise ValueError("Invalid value for `image_qa`, must not be `None`")  # noqa: E501

        self._image_qa = image_qa

    @property
    def mrz(self):
        """Gets the mrz of this DetailsOptical.  # noqa: E501


        :return: The mrz of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._mrz

    @mrz.setter
    def mrz(self, mrz):
        """Sets the mrz of this DetailsOptical.


        :param mrz: The mrz of this DetailsOptical.  # noqa: E501
        :type mrz: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and mrz is None:  # noqa: E501
            raise ValueError("Invalid value for `mrz`, must not be `None`")  # noqa: E501

        self._mrz = mrz

    @property
    def pages_count(self):
        """Gets the pages_count of this DetailsOptical.  # noqa: E501

        Number of processed pages in the document  # noqa: E501

        :return: The pages_count of this DetailsOptical.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this DetailsOptical.

        Number of processed pages in the document  # noqa: E501

        :param pages_count: The pages_count of this DetailsOptical.  # noqa: E501
        :type pages_count: int
        """
        if self.local_vars_configuration.client_side_validation and pages_count is None:  # noqa: E501
            raise ValueError("Invalid value for `pages_count`, must not be `None`")  # noqa: E501

        self._pages_count = pages_count

    @property
    def security(self):
        """Gets the security of this DetailsOptical.  # noqa: E501


        :return: The security of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this DetailsOptical.


        :param security: The security of this DetailsOptical.  # noqa: E501
        :type security: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and security is None:  # noqa: E501
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501

        self._security = security

    @property
    def text(self):
        """Gets the text of this DetailsOptical.  # noqa: E501


        :return: The text of this DetailsOptical.  # noqa: E501
        :rtype: CheckResult
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DetailsOptical.


        :param text: The text of this DetailsOptical.  # noqa: E501
        :type text: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if not isinstance(other, DetailsOptical):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailsOptical):
            return True

        return self.to_dict() != other.to_dict()
