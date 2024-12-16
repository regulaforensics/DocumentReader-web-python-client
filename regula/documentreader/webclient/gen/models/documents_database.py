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
Document database information
"""
class DocumentsDatabase(object):
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
        'description': 'str',
        'export_date': 'str',
        'id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'export_date': 'ExportDate',
        'id': 'ID',
        'version': 'Version'
    }

    def __init__(self, description=None, export_date=None, id=None, version=None, local_vars_configuration=None):  # noqa: E501
        """DocumentsDatabase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._export_date = None
        self._id = None
        self._version = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if export_date is not None:
            self.export_date = export_date
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version

    @property
    def description(self):
        """Gets the description of this DocumentsDatabase.  # noqa: E501

        Document database description  # noqa: E501

        :return: The description of this DocumentsDatabase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentsDatabase.

        Document database description  # noqa: E501

        :param description: The description of this DocumentsDatabase.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def export_date(self):
        """Gets the export_date of this DocumentsDatabase.  # noqa: E501

        Date the document database was created  # noqa: E501

        :return: The export_date of this DocumentsDatabase.  # noqa: E501
        :rtype: str
        """
        return self._export_date

    @export_date.setter
    def export_date(self, export_date):
        """Sets the export_date of this DocumentsDatabase.

        Date the document database was created  # noqa: E501

        :param export_date: The export_date of this DocumentsDatabase.  # noqa: E501
        :type export_date: str
        """

        self._export_date = export_date

    @property
    def id(self):
        """Gets the id of this DocumentsDatabase.  # noqa: E501

        Document database identifier  # noqa: E501

        :return: The id of this DocumentsDatabase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsDatabase.

        Document database identifier  # noqa: E501

        :param id: The id of this DocumentsDatabase.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this DocumentsDatabase.  # noqa: E501

        Document database version  # noqa: E501

        :return: The version of this DocumentsDatabase.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DocumentsDatabase.

        Document database version  # noqa: E501

        :param version: The version of this DocumentsDatabase.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, DocumentsDatabase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentsDatabase):
            return True

        return self.to_dict() != other.to_dict()
