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
Structure is used to describe the contents of a single file of the LDS of electronic document and the analysis of its contents within the context of the communication session with electronic document
"""
class RfidDataFile(object):
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
        'file_id': 'str',
        'type': 'RfidDataFileType',
        'file_data': 'TrfFtBytes',
        'reading_status': 'RFIDErrorCodes',
        'reading_time': 'float',
        'pa_status': 'RFIDErrorCodes',
        'notifications': 'list[ParsingErrorCodes]',
        'doc_fields_text': 'list[TextFieldType]',
        'doc_fields_graphics': 'list[GraphicFieldType]',
        'doc_fields_originals': 'list[GraphicFieldType]'
    }

    attribute_map = {
        'file_id': 'FileID',
        'type': 'Type',
        'file_data': 'FileData',
        'reading_status': 'ReadingStatus',
        'reading_time': 'ReadingTime',
        'pa_status': 'PA_Status',
        'notifications': 'Notifications',
        'doc_fields_text': 'DocFields_Text',
        'doc_fields_graphics': 'DocFields_Graphics',
        'doc_fields_originals': 'DocFields_Originals'
    }

    def __init__(self, file_id=None, type=None, file_data=None, reading_status=None, reading_time=None, pa_status=None, notifications=None, doc_fields_text=None, doc_fields_graphics=None, doc_fields_originals=None, local_vars_configuration=None):  # noqa: E501
        """RfidDataFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._type = None
        self._file_data = None
        self._reading_status = None
        self._reading_time = None
        self._pa_status = None
        self._notifications = None
        self._doc_fields_text = None
        self._doc_fields_graphics = None
        self._doc_fields_originals = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        self.type = type
        if file_data is not None:
            self.file_data = file_data
        self.reading_status = reading_status
        self.reading_time = reading_time
        self.pa_status = pa_status
        self.notifications = notifications
        self.doc_fields_text = doc_fields_text
        self.doc_fields_graphics = doc_fields_graphics
        self.doc_fields_originals = doc_fields_originals

    @property
    def file_id(self):
        """Gets the file_id of this RfidDataFile.  # noqa: E501

        File identifier. Each byte of FileID represented by its hexadecimal value. The individual bytes are separated by spaces (e.g. 01 1E)  # noqa: E501

        :return: The file_id of this RfidDataFile.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this RfidDataFile.

        File identifier. Each byte of FileID represented by its hexadecimal value. The individual bytes are separated by spaces (e.g. 01 1E)  # noqa: E501

        :param file_id: The file_id of this RfidDataFile.  # noqa: E501
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def type(self):
        """Gets the type of this RfidDataFile.  # noqa: E501


        :return: The type of this RfidDataFile.  # noqa: E501
        :rtype: RfidDataFileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RfidDataFile.


        :param type: The type of this RfidDataFile.  # noqa: E501
        :type type: RfidDataFileType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def file_data(self):
        """Gets the file_data of this RfidDataFile.  # noqa: E501


        :return: The file_data of this RfidDataFile.  # noqa: E501
        :rtype: TrfFtBytes
        """
        return self._file_data

    @file_data.setter
    def file_data(self, file_data):
        """Sets the file_data of this RfidDataFile.


        :param file_data: The file_data of this RfidDataFile.  # noqa: E501
        :type file_data: TrfFtBytes
        """

        self._file_data = file_data

    @property
    def reading_status(self):
        """Gets the reading_status of this RfidDataFile.  # noqa: E501


        :return: The reading_status of this RfidDataFile.  # noqa: E501
        :rtype: RFIDErrorCodes
        """
        return self._reading_status

    @reading_status.setter
    def reading_status(self, reading_status):
        """Sets the reading_status of this RfidDataFile.


        :param reading_status: The reading_status of this RfidDataFile.  # noqa: E501
        :type reading_status: RFIDErrorCodes
        """
        if self.local_vars_configuration.client_side_validation and reading_status is None:  # noqa: E501
            raise ValueError("Invalid value for `reading_status`, must not be `None`")  # noqa: E501

        self._reading_status = reading_status

    @property
    def reading_time(self):
        """Gets the reading_time of this RfidDataFile.  # noqa: E501

        Time of reading, milliseconds  # noqa: E501

        :return: The reading_time of this RfidDataFile.  # noqa: E501
        :rtype: float
        """
        return self._reading_time

    @reading_time.setter
    def reading_time(self, reading_time):
        """Sets the reading_time of this RfidDataFile.

        Time of reading, milliseconds  # noqa: E501

        :param reading_time: The reading_time of this RfidDataFile.  # noqa: E501
        :type reading_time: float
        """
        if self.local_vars_configuration.client_side_validation and reading_time is None:  # noqa: E501
            raise ValueError("Invalid value for `reading_time`, must not be `None`")  # noqa: E501

        self._reading_time = reading_time

    @property
    def pa_status(self):
        """Gets the pa_status of this RfidDataFile.  # noqa: E501


        :return: The pa_status of this RfidDataFile.  # noqa: E501
        :rtype: RFIDErrorCodes
        """
        return self._pa_status

    @pa_status.setter
    def pa_status(self, pa_status):
        """Sets the pa_status of this RfidDataFile.


        :param pa_status: The pa_status of this RfidDataFile.  # noqa: E501
        :type pa_status: RFIDErrorCodes
        """
        if self.local_vars_configuration.client_side_validation and pa_status is None:  # noqa: E501
            raise ValueError("Invalid value for `pa_status`, must not be `None`")  # noqa: E501

        self._pa_status = pa_status

    @property
    def notifications(self):
        """Gets the notifications of this RfidDataFile.  # noqa: E501

        List of remarks arisen when reading data from the memory of the chip and analysing their ASN.1-structure.  # noqa: E501

        :return: The notifications of this RfidDataFile.  # noqa: E501
        :rtype: list[ParsingErrorCodes]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this RfidDataFile.

        List of remarks arisen when reading data from the memory of the chip and analysing their ASN.1-structure.  # noqa: E501

        :param notifications: The notifications of this RfidDataFile.  # noqa: E501
        :type notifications: list[ParsingErrorCodes]
        """
        if self.local_vars_configuration.client_side_validation and notifications is None:  # noqa: E501
            raise ValueError("Invalid value for `notifications`, must not be `None`")  # noqa: E501

        self._notifications = notifications

    @property
    def doc_fields_text(self):
        """Gets the doc_fields_text of this RfidDataFile.  # noqa: E501

        List of document text fields formed on the basis of the file contents  # noqa: E501

        :return: The doc_fields_text of this RfidDataFile.  # noqa: E501
        :rtype: list[TextFieldType]
        """
        return self._doc_fields_text

    @doc_fields_text.setter
    def doc_fields_text(self, doc_fields_text):
        """Sets the doc_fields_text of this RfidDataFile.

        List of document text fields formed on the basis of the file contents  # noqa: E501

        :param doc_fields_text: The doc_fields_text of this RfidDataFile.  # noqa: E501
        :type doc_fields_text: list[TextFieldType]
        """
        if self.local_vars_configuration.client_side_validation and doc_fields_text is None:  # noqa: E501
            raise ValueError("Invalid value for `doc_fields_text`, must not be `None`")  # noqa: E501

        self._doc_fields_text = doc_fields_text

    @property
    def doc_fields_graphics(self):
        """Gets the doc_fields_graphics of this RfidDataFile.  # noqa: E501

        List of document graphic fields formed on the basis of the file contents  # noqa: E501

        :return: The doc_fields_graphics of this RfidDataFile.  # noqa: E501
        :rtype: list[GraphicFieldType]
        """
        return self._doc_fields_graphics

    @doc_fields_graphics.setter
    def doc_fields_graphics(self, doc_fields_graphics):
        """Sets the doc_fields_graphics of this RfidDataFile.

        List of document graphic fields formed on the basis of the file contents  # noqa: E501

        :param doc_fields_graphics: The doc_fields_graphics of this RfidDataFile.  # noqa: E501
        :type doc_fields_graphics: list[GraphicFieldType]
        """
        if self.local_vars_configuration.client_side_validation and doc_fields_graphics is None:  # noqa: E501
            raise ValueError("Invalid value for `doc_fields_graphics`, must not be `None`")  # noqa: E501

        self._doc_fields_graphics = doc_fields_graphics

    @property
    def doc_fields_originals(self):
        """Gets the doc_fields_originals of this RfidDataFile.  # noqa: E501

        List of the original binary representation of graphic document fields formed on the basis of the file contents  # noqa: E501

        :return: The doc_fields_originals of this RfidDataFile.  # noqa: E501
        :rtype: list[GraphicFieldType]
        """
        return self._doc_fields_originals

    @doc_fields_originals.setter
    def doc_fields_originals(self, doc_fields_originals):
        """Sets the doc_fields_originals of this RfidDataFile.

        List of the original binary representation of graphic document fields formed on the basis of the file contents  # noqa: E501

        :param doc_fields_originals: The doc_fields_originals of this RfidDataFile.  # noqa: E501
        :type doc_fields_originals: list[GraphicFieldType]
        """
        if self.local_vars_configuration.client_side_validation and doc_fields_originals is None:  # noqa: E501
            raise ValueError("Invalid value for `doc_fields_originals`, must not be `None`")  # noqa: E501

        self._doc_fields_originals = doc_fields_originals

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
        if not isinstance(other, RfidDataFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RfidDataFile):
            return True

        return self.to_dict() != other.to_dict()