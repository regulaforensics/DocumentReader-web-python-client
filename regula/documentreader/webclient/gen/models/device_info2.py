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
class DeviceInfo2(object):
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
        'app': 'str',
        'license_id': 'str',
        'license_type': 'str',
        'license_serial': 'str',
        'license_valid_until': 'datetime',
        'scenarios': 'list[str]',
        'version': 'str',
        'documents_database': 'DeviceInfo2DocumentsDatabase'
    }

    attribute_map = {
        'app': 'app',
        'license_id': 'licenseId',
        'license_type': 'licenseType',
        'license_serial': 'licenseSerial',
        'license_valid_until': 'licenseValidUntil',
        'scenarios': 'scenarios',
        'version': 'version',
        'documents_database': 'documentsDatabase'
    }

    def __init__(self, app=None, license_id=None, license_type=None, license_serial=None, license_valid_until=None, scenarios=None, version=None, documents_database=None, local_vars_configuration=None):  # noqa: E501
        """DeviceInfo2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app = None
        self._license_id = None
        self._license_type = None
        self._license_serial = None
        self._license_valid_until = None
        self._scenarios = None
        self._version = None
        self._documents_database = None
        self.discriminator = None

        self.app = app
        self.license_id = license_id
        self.license_type = license_type
        self.license_serial = license_serial
        self.license_valid_until = license_valid_until
        self.scenarios = scenarios
        self.version = version
        if documents_database is not None:
            self.documents_database = documents_database

    @property
    def app(self):
        """Gets the app of this DeviceInfo2.  # noqa: E501

        Application name.  # noqa: E501

        :return: The app of this DeviceInfo2.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this DeviceInfo2.

        Application name.  # noqa: E501

        :param app: The app of this DeviceInfo2.  # noqa: E501
        :type app: str
        """
        if self.local_vars_configuration.client_side_validation and app is None:  # noqa: E501
            raise ValueError("Invalid value for `app`, must not be `None`")  # noqa: E501

        self._app = app

    @property
    def license_id(self):
        """Gets the license_id of this DeviceInfo2.  # noqa: E501

        Unique license identifier.  # noqa: E501

        :return: The license_id of this DeviceInfo2.  # noqa: E501
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this DeviceInfo2.

        Unique license identifier.  # noqa: E501

        :param license_id: The license_id of this DeviceInfo2.  # noqa: E501
        :type license_id: str
        """

        self._license_id = license_id

    @property
    def license_type(self):
        """Gets the license_type of this DeviceInfo2.  # noqa: E501

        License type.  # noqa: E501

        :return: The license_type of this DeviceInfo2.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this DeviceInfo2.

        License type.  # noqa: E501

        :param license_type: The license_type of this DeviceInfo2.  # noqa: E501
        :type license_type: str
        """

        self._license_type = license_type

    @property
    def license_serial(self):
        """Gets the license_serial of this DeviceInfo2.  # noqa: E501

        License serial number.  # noqa: E501

        :return: The license_serial of this DeviceInfo2.  # noqa: E501
        :rtype: str
        """
        return self._license_serial

    @license_serial.setter
    def license_serial(self, license_serial):
        """Sets the license_serial of this DeviceInfo2.

        License serial number.  # noqa: E501

        :param license_serial: The license_serial of this DeviceInfo2.  # noqa: E501
        :type license_serial: str
        """

        self._license_serial = license_serial

    @property
    def license_valid_until(self):
        """Gets the license_valid_until of this DeviceInfo2.  # noqa: E501

        License validity date.  # noqa: E501

        :return: The license_valid_until of this DeviceInfo2.  # noqa: E501
        :rtype: datetime
        """
        return self._license_valid_until

    @license_valid_until.setter
    def license_valid_until(self, license_valid_until):
        """Sets the license_valid_until of this DeviceInfo2.

        License validity date.  # noqa: E501

        :param license_valid_until: The license_valid_until of this DeviceInfo2.  # noqa: E501
        :type license_valid_until: datetime
        """

        self._license_valid_until = license_valid_until

    @property
    def scenarios(self):
        """Gets the scenarios of this DeviceInfo2.  # noqa: E501

        List of supported scenarios.  # noqa: E501

        :return: The scenarios of this DeviceInfo2.  # noqa: E501
        :rtype: list[str]
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        """Sets the scenarios of this DeviceInfo2.

        List of supported scenarios.  # noqa: E501

        :param scenarios: The scenarios of this DeviceInfo2.  # noqa: E501
        :type scenarios: list[str]
        """

        self._scenarios = scenarios

    @property
    def version(self):
        """Gets the version of this DeviceInfo2.  # noqa: E501

        Product version.  # noqa: E501

        :return: The version of this DeviceInfo2.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceInfo2.

        Product version.  # noqa: E501

        :param version: The version of this DeviceInfo2.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def documents_database(self):
        """Gets the documents_database of this DeviceInfo2.  # noqa: E501


        :return: The documents_database of this DeviceInfo2.  # noqa: E501
        :rtype: DeviceInfo2DocumentsDatabase
        """
        return self._documents_database

    @documents_database.setter
    def documents_database(self, documents_database):
        """Sets the documents_database of this DeviceInfo2.


        :param documents_database: The documents_database of this DeviceInfo2.  # noqa: E501
        :type documents_database: DeviceInfo2DocumentsDatabase
        """

        self._documents_database = documents_database

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
        if not isinstance(other, DeviceInfo2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceInfo2):
            return True

        return self.to_dict() != other.to_dict()
