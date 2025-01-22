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
Structure is used to describe the contents of a single copy of digital signature of the document security object and the results of its check within the context of the communication session with electronic document
"""
class RfidSignerInfoEx(object):
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
        'version': 'float',
        'issuer': 'RfidDistinguishedName',
        'serial_number': 'TrfFtBytes',
        'subject_key_identifier': 'TrfFtBytes',
        'digest_algorithm': 'str',
        'signed_attributes': 'list[RfidAttributeData]',
        'signature_algorithm': 'str',
        'signature': 'TrfFtBytes',
        'pa_status': 'RFIDErrorCodes',
        'certificate_chain': 'list[RfidCertificateEx]',
        'data_to_hash': 'str',
        'notifications': 'ParsingErrorCodes'
    }

    attribute_map = {
        'version': 'Version',
        'issuer': 'Issuer',
        'serial_number': 'SerialNumber',
        'subject_key_identifier': 'SubjectKeyIdentifier',
        'digest_algorithm': 'DigestAlgorithm',
        'signed_attributes': 'SignedAttributes',
        'signature_algorithm': 'SignatureAlgorithm',
        'signature': 'Signature',
        'pa_status': 'PA_Status',
        'certificate_chain': 'CertificateChain',
        'data_to_hash': 'DataToHash',
        'notifications': 'Notifications'
    }

    def __init__(self, version=None, issuer=None, serial_number=None, subject_key_identifier=None, digest_algorithm=None, signed_attributes=None, signature_algorithm=None, signature=None, pa_status=None, certificate_chain=None, data_to_hash=None, notifications=None, local_vars_configuration=None):  # noqa: E501
        """RfidSignerInfoEx - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._issuer = None
        self._serial_number = None
        self._subject_key_identifier = None
        self._digest_algorithm = None
        self._signed_attributes = None
        self._signature_algorithm = None
        self._signature = None
        self._pa_status = None
        self._certificate_chain = None
        self._data_to_hash = None
        self._notifications = None
        self.discriminator = None

        self.version = version
        self.issuer = issuer
        self.serial_number = serial_number
        self.subject_key_identifier = subject_key_identifier
        self.digest_algorithm = digest_algorithm
        self.signed_attributes = signed_attributes
        self.signature_algorithm = signature_algorithm
        self.signature = signature
        self.pa_status = pa_status
        self.certificate_chain = certificate_chain
        self.data_to_hash = data_to_hash
        self.notifications = notifications

    @property
    def version(self):
        """Gets the version of this RfidSignerInfoEx.  # noqa: E501

        Version of SignerInfo ASN.1 structure  # noqa: E501

        :return: The version of this RfidSignerInfoEx.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RfidSignerInfoEx.

        Version of SignerInfo ASN.1 structure  # noqa: E501

        :param version: The version of this RfidSignerInfoEx.  # noqa: E501
        :type version: float
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def issuer(self):
        """Gets the issuer of this RfidSignerInfoEx.  # noqa: E501


        :return: The issuer of this RfidSignerInfoEx.  # noqa: E501
        :rtype: RfidDistinguishedName
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this RfidSignerInfoEx.


        :param issuer: The issuer of this RfidSignerInfoEx.  # noqa: E501
        :type issuer: RfidDistinguishedName
        """
        if self.local_vars_configuration.client_side_validation and issuer is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def serial_number(self):
        """Gets the serial_number of this RfidSignerInfoEx.  # noqa: E501


        :return: The serial_number of this RfidSignerInfoEx.  # noqa: E501
        :rtype: TrfFtBytes
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this RfidSignerInfoEx.


        :param serial_number: The serial_number of this RfidSignerInfoEx.  # noqa: E501
        :type serial_number: TrfFtBytes
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def subject_key_identifier(self):
        """Gets the subject_key_identifier of this RfidSignerInfoEx.  # noqa: E501


        :return: The subject_key_identifier of this RfidSignerInfoEx.  # noqa: E501
        :rtype: TrfFtBytes
        """
        return self._subject_key_identifier

    @subject_key_identifier.setter
    def subject_key_identifier(self, subject_key_identifier):
        """Sets the subject_key_identifier of this RfidSignerInfoEx.


        :param subject_key_identifier: The subject_key_identifier of this RfidSignerInfoEx.  # noqa: E501
        :type subject_key_identifier: TrfFtBytes
        """
        if self.local_vars_configuration.client_side_validation and subject_key_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `subject_key_identifier`, must not be `None`")  # noqa: E501

        self._subject_key_identifier = subject_key_identifier

    @property
    def digest_algorithm(self):
        """Gets the digest_algorithm of this RfidSignerInfoEx.  # noqa: E501

        Hash algorithm identifier (OID) for digital signature generation  # noqa: E501

        :return: The digest_algorithm of this RfidSignerInfoEx.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        """Sets the digest_algorithm of this RfidSignerInfoEx.

        Hash algorithm identifier (OID) for digital signature generation  # noqa: E501

        :param digest_algorithm: The digest_algorithm of this RfidSignerInfoEx.  # noqa: E501
        :type digest_algorithm: str
        """
        if self.local_vars_configuration.client_side_validation and digest_algorithm is None:  # noqa: E501
            raise ValueError("Invalid value for `digest_algorithm`, must not be `None`")  # noqa: E501

        self._digest_algorithm = digest_algorithm

    @property
    def signed_attributes(self):
        """Gets the signed_attributes of this RfidSignerInfoEx.  # noqa: E501

        List of the signed attributes  # noqa: E501

        :return: The signed_attributes of this RfidSignerInfoEx.  # noqa: E501
        :rtype: list[RfidAttributeData]
        """
        return self._signed_attributes

    @signed_attributes.setter
    def signed_attributes(self, signed_attributes):
        """Sets the signed_attributes of this RfidSignerInfoEx.

        List of the signed attributes  # noqa: E501

        :param signed_attributes: The signed_attributes of this RfidSignerInfoEx.  # noqa: E501
        :type signed_attributes: list[RfidAttributeData]
        """
        if self.local_vars_configuration.client_side_validation and signed_attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `signed_attributes`, must not be `None`")  # noqa: E501

        self._signed_attributes = signed_attributes

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this RfidSignerInfoEx.  # noqa: E501

        Digital signature algorithm identifier (OID)  # noqa: E501

        :return: The signature_algorithm of this RfidSignerInfoEx.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this RfidSignerInfoEx.

        Digital signature algorithm identifier (OID)  # noqa: E501

        :param signature_algorithm: The signature_algorithm of this RfidSignerInfoEx.  # noqa: E501
        :type signature_algorithm: str
        """
        if self.local_vars_configuration.client_side_validation and signature_algorithm is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_algorithm`, must not be `None`")  # noqa: E501

        self._signature_algorithm = signature_algorithm

    @property
    def signature(self):
        """Gets the signature of this RfidSignerInfoEx.  # noqa: E501


        :return: The signature of this RfidSignerInfoEx.  # noqa: E501
        :rtype: TrfFtBytes
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this RfidSignerInfoEx.


        :param signature: The signature of this RfidSignerInfoEx.  # noqa: E501
        :type signature: TrfFtBytes
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def pa_status(self):
        """Gets the pa_status of this RfidSignerInfoEx.  # noqa: E501


        :return: The pa_status of this RfidSignerInfoEx.  # noqa: E501
        :rtype: RFIDErrorCodes
        """
        return self._pa_status

    @pa_status.setter
    def pa_status(self, pa_status):
        """Sets the pa_status of this RfidSignerInfoEx.


        :param pa_status: The pa_status of this RfidSignerInfoEx.  # noqa: E501
        :type pa_status: RFIDErrorCodes
        """
        if self.local_vars_configuration.client_side_validation and pa_status is None:  # noqa: E501
            raise ValueError("Invalid value for `pa_status`, must not be `None`")  # noqa: E501

        self._pa_status = pa_status

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this RfidSignerInfoEx.  # noqa: E501

        Certificate chain, used for the digital signature verification.  # noqa: E501

        :return: The certificate_chain of this RfidSignerInfoEx.  # noqa: E501
        :rtype: list[RfidCertificateEx]
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this RfidSignerInfoEx.

        Certificate chain, used for the digital signature verification.  # noqa: E501

        :param certificate_chain: The certificate_chain of this RfidSignerInfoEx.  # noqa: E501
        :type certificate_chain: list[RfidCertificateEx]
        """
        if self.local_vars_configuration.client_side_validation and certificate_chain is None:  # noqa: E501
            raise ValueError("Invalid value for `certificate_chain`, must not be `None`")  # noqa: E501

        self._certificate_chain = certificate_chain

    @property
    def data_to_hash(self):
        """Gets the data_to_hash of this RfidSignerInfoEx.  # noqa: E501

        Binary data array used to calculate the hash value for digital signature verification. Base64 encoded.  # noqa: E501

        :return: The data_to_hash of this RfidSignerInfoEx.  # noqa: E501
        :rtype: str
        """
        return self._data_to_hash

    @data_to_hash.setter
    def data_to_hash(self, data_to_hash):
        """Sets the data_to_hash of this RfidSignerInfoEx.

        Binary data array used to calculate the hash value for digital signature verification. Base64 encoded.  # noqa: E501

        :param data_to_hash: The data_to_hash of this RfidSignerInfoEx.  # noqa: E501
        :type data_to_hash: str
        """
        if self.local_vars_configuration.client_side_validation and data_to_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `data_to_hash`, must not be `None`")  # noqa: E501

        self._data_to_hash = data_to_hash

    @property
    def notifications(self):
        """Gets the notifications of this RfidSignerInfoEx.  # noqa: E501


        :return: The notifications of this RfidSignerInfoEx.  # noqa: E501
        :rtype: ParsingErrorCodes
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this RfidSignerInfoEx.


        :param notifications: The notifications of this RfidSignerInfoEx.  # noqa: E501
        :type notifications: ParsingErrorCodes
        """
        if self.local_vars_configuration.client_side_validation and notifications is None:  # noqa: E501
            raise ValueError("Invalid value for `notifications`, must not be `None`")  # noqa: E501

        self._notifications = notifications

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
        if not isinstance(other, RfidSignerInfoEx):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RfidSignerInfoEx):
            return True

        return self.to_dict() != other.to_dict()
