# coding: utf-8

# flake8: noqa

"""
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import apis into sdk package
from regula.documentreader.webclient.gen.api.healthcheck_api import HealthcheckApi
from regula.documentreader.webclient.gen.api.process_api import ProcessApi
from regula.documentreader.webclient.gen.api.transaction_api import TransactionApi

# import ApiClient
from regula.documentreader.webclient.gen.api_response import ApiResponse
from regula.documentreader.webclient.gen.api_client import ApiClient
from regula.documentreader.webclient.gen.configuration import Configuration
from regula.documentreader.webclient.gen.exceptions import OpenApiException
from regula.documentreader.webclient.gen.exceptions import ApiTypeError
from regula.documentreader.webclient.gen.exceptions import ApiValueError
from regula.documentreader.webclient.gen.exceptions import ApiKeyError
from regula.documentreader.webclient.gen.exceptions import ApiAttributeError
from regula.documentreader.webclient.gen.exceptions import ApiException

# import models into sdk package
from regula.documentreader.webclient.gen.models.area_array import AreaArray
from regula.documentreader.webclient.gen.models.area_container import AreaContainer
from regula.documentreader.webclient.gen.models.auth_params import AuthParams
from regula.documentreader.webclient.gen.models.authenticity_check_list import AuthenticityCheckList
from regula.documentreader.webclient.gen.models.authenticity_check_list_item import AuthenticityCheckListItem
from regula.documentreader.webclient.gen.models.authenticity_check_result import AuthenticityCheckResult
from regula.documentreader.webclient.gen.models.authenticity_check_result_item import AuthenticityCheckResultItem
from regula.documentreader.webclient.gen.models.authenticity_check_result_list_inner import AuthenticityCheckResultListInner
from regula.documentreader.webclient.gen.models.authenticity_result import AuthenticityResult
from regula.documentreader.webclient.gen.models.authenticity_result_type import AuthenticityResultType
from regula.documentreader.webclient.gen.models.bar_code_module_type import BarCodeModuleType
from regula.documentreader.webclient.gen.models.barcode_type import BarcodeType
from regula.documentreader.webclient.gen.models.bc_pdf417_info import BcPDF417INFO
from regula.documentreader.webclient.gen.models.bc_roidetect import BcROIDETECT
from regula.documentreader.webclient.gen.models.binary_data import BinaryData
from regula.documentreader.webclient.gen.models.byte_array_item import ByteArrayItem
from regula.documentreader.webclient.gen.models.byte_array_result import ByteArrayResult
from regula.documentreader.webclient.gen.models.candidates_list_item import CandidatesListItem
from regula.documentreader.webclient.gen.models.certificate_data import CertificateData
from regula.documentreader.webclient.gen.models.check_diagnose import CheckDiagnose
from regula.documentreader.webclient.gen.models.check_result import CheckResult
from regula.documentreader.webclient.gen.models.chosen_document_type import ChosenDocumentType
from regula.documentreader.webclient.gen.models.chosen_document_type_result import ChosenDocumentTypeResult
from regula.documentreader.webclient.gen.models.container_list import ContainerList
from regula.documentreader.webclient.gen.models.container_list_list_inner import ContainerListListInner
from regula.documentreader.webclient.gen.models.critical import Critical
from regula.documentreader.webclient.gen.models.cross_source_value_comparison import CrossSourceValueComparison
from regula.documentreader.webclient.gen.models.data_module import DataModule
from regula.documentreader.webclient.gen.models.details_optical import DetailsOptical
from regula.documentreader.webclient.gen.models.details_rfid import DetailsRFID
from regula.documentreader.webclient.gen.models.device_info import DeviceInfo
from regula.documentreader.webclient.gen.models.doc_bar_code_info import DocBarCodeInfo
from regula.documentreader.webclient.gen.models.doc_bar_code_info_fields_list import DocBarCodeInfoFieldsList
from regula.documentreader.webclient.gen.models.doc_bar_code_info_item import DocBarCodeInfoItem
from regula.documentreader.webclient.gen.models.doc_graphics_info_item import DocGraphicsInfoItem
from regula.documentreader.webclient.gen.models.doc_visual_extended_field import DocVisualExtendedField
from regula.documentreader.webclient.gen.models.doc_visual_extended_field_item import DocVisualExtendedFieldItem
from regula.documentreader.webclient.gen.models.doc_visual_extended_info import DocVisualExtendedInfo
from regula.documentreader.webclient.gen.models.doc_visual_extended_info_item import DocVisualExtendedInfoItem
from regula.documentreader.webclient.gen.models.document_binary_info_result import DocumentBinaryInfoResult
from regula.documentreader.webclient.gen.models.document_format import DocumentFormat
from regula.documentreader.webclient.gen.models.document_image import DocumentImage
from regula.documentreader.webclient.gen.models.document_image_result import DocumentImageResult
from regula.documentreader.webclient.gen.models.document_position import DocumentPosition
from regula.documentreader.webclient.gen.models.document_position_item import DocumentPositionItem
from regula.documentreader.webclient.gen.models.document_position_result import DocumentPositionResult
from regula.documentreader.webclient.gen.models.document_type import DocumentType
from regula.documentreader.webclient.gen.models.document_type_recognition_result import DocumentTypeRecognitionResult
from regula.documentreader.webclient.gen.models.document_types_candidates import DocumentTypesCandidates
from regula.documentreader.webclient.gen.models.document_types_candidates_list import DocumentTypesCandidatesList
from regula.documentreader.webclient.gen.models.document_types_candidates_result import DocumentTypesCandidatesResult
from regula.documentreader.webclient.gen.models.documents_database import DocumentsDatabase
from regula.documentreader.webclient.gen.models.encrypted_rcl_item import EncryptedRCLItem
from regula.documentreader.webclient.gen.models.encrypted_rcl_result import EncryptedRCLResult
from regula.documentreader.webclient.gen.models.error_coordinates import ErrorCoordinates
from regula.documentreader.webclient.gen.models.fdsid_list import FDSIDList
from regula.documentreader.webclient.gen.models.face_api import FaceApi
from regula.documentreader.webclient.gen.models.face_api_search import FaceApiSearch
from regula.documentreader.webclient.gen.models.face_detection import FaceDetection
from regula.documentreader.webclient.gen.models.face_detection_item import FaceDetectionItem
from regula.documentreader.webclient.gen.models.face_detection_result import FaceDetectionResult
from regula.documentreader.webclient.gen.models.face_item import FaceItem
from regula.documentreader.webclient.gen.models.fiber_item import FiberItem
from regula.documentreader.webclient.gen.models.fiber_result import FiberResult
from regula.documentreader.webclient.gen.models.field_item import FieldItem
from regula.documentreader.webclient.gen.models.file_image import FileImage
from regula.documentreader.webclient.gen.models.get_transactions_by_tag_response import GetTransactionsByTagResponse
from regula.documentreader.webclient.gen.models.graph_data import GraphData
from regula.documentreader.webclient.gen.models.graphic_field import GraphicField
from regula.documentreader.webclient.gen.models.graphic_field_type import GraphicFieldType
from regula.documentreader.webclient.gen.models.graphic_fields_list import GraphicFieldsList
from regula.documentreader.webclient.gen.models.graphics_result import GraphicsResult
from regula.documentreader.webclient.gen.models.healthcheck import Healthcheck
from regula.documentreader.webclient.gen.models.healthcheck_documents_database import HealthcheckDocumentsDatabase
from regula.documentreader.webclient.gen.models.ident_item import IdentItem
from regula.documentreader.webclient.gen.models.ident_result import IdentResult
from regula.documentreader.webclient.gen.models.image_data import ImageData
from regula.documentreader.webclient.gen.models.image_qa import ImageQA
from regula.documentreader.webclient.gen.models.image_quality_check import ImageQualityCheck
from regula.documentreader.webclient.gen.models.image_quality_check_list import ImageQualityCheckList
from regula.documentreader.webclient.gen.models.image_quality_check_list_item import ImageQualityCheckListItem
from regula.documentreader.webclient.gen.models.image_quality_check_type import ImageQualityCheckType
from regula.documentreader.webclient.gen.models.image_quality_result import ImageQualityResult
from regula.documentreader.webclient.gen.models.image_transaction_data import ImageTransactionData
from regula.documentreader.webclient.gen.models.images import Images
from regula.documentreader.webclient.gen.models.images_available_source import ImagesAvailableSource
from regula.documentreader.webclient.gen.models.images_field import ImagesField
from regula.documentreader.webclient.gen.models.images_field_value import ImagesFieldValue
from regula.documentreader.webclient.gen.models.images_item import ImagesItem
from regula.documentreader.webclient.gen.models.images_result import ImagesResult
from regula.documentreader.webclient.gen.models.in_data import InData
from regula.documentreader.webclient.gen.models.in_data_transaction_images_field_value import InDataTransactionImagesFieldValue
from regula.documentreader.webclient.gen.models.in_data_video import InDataVideo
from regula.documentreader.webclient.gen.models.input_barcode_type import InputBarcodeType
from regula.documentreader.webclient.gen.models.input_image_quality_checks import InputImageQualityChecks
from regula.documentreader.webclient.gen.models.lcid import LCID
from regula.documentreader.webclient.gen.models.lexical_analysis_result import LexicalAnalysisResult
from regula.documentreader.webclient.gen.models.license_item import LicenseItem
from regula.documentreader.webclient.gen.models.license_result import LicenseResult
from regula.documentreader.webclient.gen.models.light import Light
from regula.documentreader.webclient.gen.models.list_transactions_by_tag_response import ListTransactionsByTagResponse
from regula.documentreader.webclient.gen.models.list_verified_fields import ListVerifiedFields
from regula.documentreader.webclient.gen.models.list_verified_fields_item import ListVerifiedFieldsItem
from regula.documentreader.webclient.gen.models.liveness_params import LivenessParams
from regula.documentreader.webclient.gen.models.log_level import LogLevel
from regula.documentreader.webclient.gen.models.mrz_detector_result import MRZDetectorResult
from regula.documentreader.webclient.gen.models.mrz_format import MRZFormat
from regula.documentreader.webclient.gen.models.mrz_position_result import MRZPositionResult
from regula.documentreader.webclient.gen.models.mrz_rows_item import MRZRowsItem
from regula.documentreader.webclient.gen.models.mrz_test_quality import MRZTestQuality
from regula.documentreader.webclient.gen.models.mrz_test_quality_item import MRZTestQualityItem
from regula.documentreader.webclient.gen.models.mrz_test_quality_result import MRZTestQualityResult
from regula.documentreader.webclient.gen.models.measure_system import MeasureSystem
from regula.documentreader.webclient.gen.models.mrz_detect_mode_enum import MrzDetectModeEnum
from regula.documentreader.webclient.gen.models.mrz_position import MrzPosition
from regula.documentreader.webclient.gen.models.mrz_position_item import MrzPositionItem
from regula.documentreader.webclient.gen.models.ocr_security_text_item import OCRSecurityTextItem
from regula.documentreader.webclient.gen.models.ocr_security_text_result import OCRSecurityTextResult
from regula.documentreader.webclient.gen.models.one_candidate import OneCandidate
from regula.documentreader.webclient.gen.models.one_candidate_item import OneCandidateItem
from regula.documentreader.webclient.gen.models.original_symbol import OriginalSymbol
from regula.documentreader.webclient.gen.models.out_data import OutData
from regula.documentreader.webclient.gen.models.out_data_transaction_images_field_value import OutDataTransactionImagesFieldValue
from regula.documentreader.webclient.gen.models.p_array_field import PArrayField
from regula.documentreader.webclient.gen.models.parsed_data import ParsedData
from regula.documentreader.webclient.gen.models.parsing_notification_codes import ParsingNotificationCodes
from regula.documentreader.webclient.gen.models.per_document_config import PerDocumentConfig
from regula.documentreader.webclient.gen.models.photo_ident_item import PhotoIdentItem
from regula.documentreader.webclient.gen.models.photo_ident_result import PhotoIdentResult
from regula.documentreader.webclient.gen.models.point import Point
from regula.documentreader.webclient.gen.models.point_array import PointArray
from regula.documentreader.webclient.gen.models.points_container import PointsContainer
from regula.documentreader.webclient.gen.models.process_params import ProcessParams
from regula.documentreader.webclient.gen.models.process_params_rfid import ProcessParamsRfid
from regula.documentreader.webclient.gen.models.process_request import ProcessRequest
from regula.documentreader.webclient.gen.models.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.models.process_response import ProcessResponse
from regula.documentreader.webclient.gen.models.process_system_info import ProcessSystemInfo
from regula.documentreader.webclient.gen.models.processing_status import ProcessingStatus
from regula.documentreader.webclient.gen.models.rfid_doc_visual_extended_field import RFIDDocVisualExtendedField
from regula.documentreader.webclient.gen.models.rfid_doc_visual_extended_field_item import RFIDDocVisualExtendedFieldItem
from regula.documentreader.webclient.gen.models.rfid_doc_visual_extended_info import RFIDDocVisualExtendedInfo
from regula.documentreader.webclient.gen.models.rfid_doc_visual_extended_info_item import RFIDDocVisualExtendedInfoItem
from regula.documentreader.webclient.gen.models.rfid_error_codes import RFIDErrorCodes
from regula.documentreader.webclient.gen.models.rfid_graphics_info_result import RFIDGraphicsInfoResult
from regula.documentreader.webclient.gen.models.rfidpkd_resource_type import RFIDPKDResourceType
from regula.documentreader.webclient.gen.models.rfid_text_data_result import RFIDTextDataResult
from regula.documentreader.webclient.gen.models.raw_image_container_item import RawImageContainerItem
from regula.documentreader.webclient.gen.models.raw_image_container_list import RawImageContainerList
from regula.documentreader.webclient.gen.models.rectangle_coordinates import RectangleCoordinates
from regula.documentreader.webclient.gen.models.result import Result
from regula.documentreader.webclient.gen.models.result_item import ResultItem
from regula.documentreader.webclient.gen.models.result_mrz_detector import ResultMRZDetector
from regula.documentreader.webclient.gen.models.result_mrz_detector_item import ResultMRZDetectorItem
from regula.documentreader.webclient.gen.models.rfid_a_chip import RfidAChip
from regula.documentreader.webclient.gen.models.rfid_access_control_info import RfidAccessControlInfo
from regula.documentreader.webclient.gen.models.rfid_access_control_procedure_type import RfidAccessControlProcedureType
from regula.documentreader.webclient.gen.models.rfid_access_key import RfidAccessKey
from regula.documentreader.webclient.gen.models.rfid_application import RfidApplication
from regula.documentreader.webclient.gen.models.rfid_application_type import RfidApplicationType
from regula.documentreader.webclient.gen.models.rfid_attribute_data import RfidAttributeData
from regula.documentreader.webclient.gen.models.rfid_attribute_name import RfidAttributeName
from regula.documentreader.webclient.gen.models.rfid_authentication_procedure_type import RfidAuthenticationProcedureType
from regula.documentreader.webclient.gen.models.rfid_baud_rate import RfidBaudRate
from regula.documentreader.webclient.gen.models.rfid_card_properties_ext import RfidCardPropertiesExt
from regula.documentreader.webclient.gen.models.rfid_certificate_ex import RfidCertificateEx
from regula.documentreader.webclient.gen.models.rfid_certificate_origin import RfidCertificateOrigin
from regula.documentreader.webclient.gen.models.rfid_certificate_type import RfidCertificateType
from regula.documentreader.webclient.gen.models.rfid_dg1 import RfidDG1
from regula.documentreader.webclient.gen.models.rfid_data_file import RfidDataFile
from regula.documentreader.webclient.gen.models.rfid_data_file_type import RfidDataFileType
from regula.documentreader.webclient.gen.models.rfid_data_group_type_tag import RfidDataGroupTypeTag
from regula.documentreader.webclient.gen.models.rfid_distinguished_name import RfidDistinguishedName
from regula.documentreader.webclient.gen.models.rfid_location import RfidLocation
from regula.documentreader.webclient.gen.models.rfid_origin import RfidOrigin
from regula.documentreader.webclient.gen.models.rfid_password_type import RfidPasswordType
from regula.documentreader.webclient.gen.models.rfid_pki_extension import RfidPkiExtension
from regula.documentreader.webclient.gen.models.rfid_raw_data import RfidRawData
from regula.documentreader.webclient.gen.models.rfid_security_object import RfidSecurityObject
from regula.documentreader.webclient.gen.models.rfid_session_data import RfidSessionData
from regula.documentreader.webclient.gen.models.rfid_signer_info_ex import RfidSignerInfoEx
from regula.documentreader.webclient.gen.models.rfid_terminal import RfidTerminal
from regula.documentreader.webclient.gen.models.rfid_terminal_type import RfidTerminalType
from regula.documentreader.webclient.gen.models.rfid_type import RfidType
from regula.documentreader.webclient.gen.models.rfid_validity import RfidValidity
from regula.documentreader.webclient.gen.models.scenario import Scenario
from regula.documentreader.webclient.gen.models.security_feature_item import SecurityFeatureItem
from regula.documentreader.webclient.gen.models.security_feature_result import SecurityFeatureResult
from regula.documentreader.webclient.gen.models.security_feature_type import SecurityFeatureType
from regula.documentreader.webclient.gen.models.security_object_certificates import SecurityObjectCertificates
from regula.documentreader.webclient.gen.models.source import Source
from regula.documentreader.webclient.gen.models.source_validity import SourceValidity
from regula.documentreader.webclient.gen.models.status import Status
from regula.documentreader.webclient.gen.models.status_item import StatusItem
from regula.documentreader.webclient.gen.models.status_result import StatusResult
from regula.documentreader.webclient.gen.models.string_item import StringItem
from regula.documentreader.webclient.gen.models.string_recognition_result import StringRecognitionResult
from regula.documentreader.webclient.gen.models.symbol import Symbol
from regula.documentreader.webclient.gen.models.symbol_candidate import SymbolCandidate
from regula.documentreader.webclient.gen.models.symbol_estimation_item import SymbolEstimationItem
from regula.documentreader.webclient.gen.models.symbol_recognition_result import SymbolRecognitionResult
from regula.documentreader.webclient.gen.models.t_doc_binary_info import TDocBinaryInfo
from regula.documentreader.webclient.gen.models.t_doc_binary_info_item import TDocBinaryInfoItem
from regula.documentreader.webclient.gen.models.t_original_rfid_graphics_info import TOriginalRFIDGraphicsInfo
from regula.documentreader.webclient.gen.models.t_original_rfid_graphics_info_item import TOriginalRFIDGraphicsInfoItem
from regula.documentreader.webclient.gen.models.text import Text
from regula.documentreader.webclient.gen.models.text_available_source import TextAvailableSource
from regula.documentreader.webclient.gen.models.text_data_result import TextDataResult
from regula.documentreader.webclient.gen.models.text_field import TextField
from regula.documentreader.webclient.gen.models.text_field_type import TextFieldType
from regula.documentreader.webclient.gen.models.text_field_value import TextFieldValue
from regula.documentreader.webclient.gen.models.text_item import TextItem
from regula.documentreader.webclient.gen.models.text_post_processing import TextPostProcessing
from regula.documentreader.webclient.gen.models.text_result import TextResult
from regula.documentreader.webclient.gen.models.transaction_image import TransactionImage
from regula.documentreader.webclient.gen.models.transaction_info import TransactionInfo
from regula.documentreader.webclient.gen.models.transaction_process_get_response import TransactionProcessGetResponse
from regula.documentreader.webclient.gen.models.transaction_process_request import TransactionProcessRequest
from regula.documentreader.webclient.gen.models.transaction_process_result import TransactionProcessResult
from regula.documentreader.webclient.gen.models.trf_ft_bytes import TrfFtBytes
from regula.documentreader.webclient.gen.models.trf_ft_string import TrfFtString
from regula.documentreader.webclient.gen.models.verification_result import VerificationResult
from regula.documentreader.webclient.gen.models.verified_field_map import VerifiedFieldMap
from regula.documentreader.webclient.gen.models.visibility import Visibility
from regula.documentreader.webclient.gen.models.visual_extended_field_item import VisualExtendedFieldItem
