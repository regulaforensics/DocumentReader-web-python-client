# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from regula.documentreader.webclient.gen.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from regula.documentreader.webclient.gen.model.check_result import CheckResult
from regula.documentreader.webclient.gen.model.chosen_document_type import ChosenDocumentType
from regula.documentreader.webclient.gen.model.chosen_document_type_result import ChosenDocumentTypeResult
from regula.documentreader.webclient.gen.model.chosen_document_type_result_all_of import ChosenDocumentTypeResultAllOf
from regula.documentreader.webclient.gen.model.comparison_matrix import ComparisonMatrix
from regula.documentreader.webclient.gen.model.container_list import ContainerList
from regula.documentreader.webclient.gen.model.cross_source_value_comparison import CrossSourceValueComparison
from regula.documentreader.webclient.gen.model.details_optical import DetailsOptical
from regula.documentreader.webclient.gen.model.details_rfid import DetailsRFID
from regula.documentreader.webclient.gen.model.device_info import DeviceInfo
from regula.documentreader.webclient.gen.model.doc_visual_extended_field import DocVisualExtendedField
from regula.documentreader.webclient.gen.model.doc_visual_extended_info import DocVisualExtendedInfo
from regula.documentreader.webclient.gen.model.document_format import DocumentFormat
from regula.documentreader.webclient.gen.model.document_image import DocumentImage
from regula.documentreader.webclient.gen.model.document_image_result import DocumentImageResult
from regula.documentreader.webclient.gen.model.document_image_result_all_of import DocumentImageResultAllOf
from regula.documentreader.webclient.gen.model.document_type import DocumentType
from regula.documentreader.webclient.gen.model.document_type_recognition_result import DocumentTypeRecognitionResult
from regula.documentreader.webclient.gen.model.document_types_candidates import DocumentTypesCandidates
from regula.documentreader.webclient.gen.model.document_types_candidates_list import DocumentTypesCandidatesList
from regula.documentreader.webclient.gen.model.document_types_candidates_result import DocumentTypesCandidatesResult
from regula.documentreader.webclient.gen.model.document_types_candidates_result_all_of import DocumentTypesCandidatesResultAllOf
from regula.documentreader.webclient.gen.model.fdsid_list import FDSIDList
from regula.documentreader.webclient.gen.model.graphic_field import GraphicField
from regula.documentreader.webclient.gen.model.graphic_field_type import GraphicFieldType
from regula.documentreader.webclient.gen.model.graphic_fields_list import GraphicFieldsList
from regula.documentreader.webclient.gen.model.graphics_result import GraphicsResult
from regula.documentreader.webclient.gen.model.graphics_result_all_of import GraphicsResultAllOf
from regula.documentreader.webclient.gen.model.image_data import ImageData
from regula.documentreader.webclient.gen.model.image_qa import ImageQA
from regula.documentreader.webclient.gen.model.images import Images
from regula.documentreader.webclient.gen.model.images_available_source import ImagesAvailableSource
from regula.documentreader.webclient.gen.model.images_field import ImagesField
from regula.documentreader.webclient.gen.model.images_field_value import ImagesFieldValue
from regula.documentreader.webclient.gen.model.images_result import ImagesResult
from regula.documentreader.webclient.gen.model.images_result_all_of import ImagesResultAllOf
from regula.documentreader.webclient.gen.model.lcid import LCID
from regula.documentreader.webclient.gen.model.lexical_analysis_result import LexicalAnalysisResult
from regula.documentreader.webclient.gen.model.lexical_analysis_result_all_of import LexicalAnalysisResultAllOf
from regula.documentreader.webclient.gen.model.light import Light
from regula.documentreader.webclient.gen.model.list_verified_fields import ListVerifiedFields
from regula.documentreader.webclient.gen.model.one_candidate import OneCandidate
from regula.documentreader.webclient.gen.model.original_symbol import OriginalSymbol
from regula.documentreader.webclient.gen.model.process_params import ProcessParams
from regula.documentreader.webclient.gen.model.process_request import ProcessRequest
from regula.documentreader.webclient.gen.model.process_request_image import ProcessRequestImage
from regula.documentreader.webclient.gen.model.process_response import ProcessResponse
from regula.documentreader.webclient.gen.model.process_system_info import ProcessSystemInfo
from regula.documentreader.webclient.gen.model.processing_status import ProcessingStatus
from regula.documentreader.webclient.gen.model.rectangle_coordinates import RectangleCoordinates
from regula.documentreader.webclient.gen.model.result import Result
from regula.documentreader.webclient.gen.model.result_item import ResultItem
from regula.documentreader.webclient.gen.model.rfid_location import RfidLocation
from regula.documentreader.webclient.gen.model.rfid_origin import RfidOrigin
from regula.documentreader.webclient.gen.model.scenario import Scenario
from regula.documentreader.webclient.gen.model.source import Source
from regula.documentreader.webclient.gen.model.source_validity import SourceValidity
from regula.documentreader.webclient.gen.model.status import Status
from regula.documentreader.webclient.gen.model.status_result import StatusResult
from regula.documentreader.webclient.gen.model.status_result_all_of import StatusResultAllOf
from regula.documentreader.webclient.gen.model.string_recognition_result import StringRecognitionResult
from regula.documentreader.webclient.gen.model.symbol_candidate import SymbolCandidate
from regula.documentreader.webclient.gen.model.symbol_recognition_result import SymbolRecognitionResult
from regula.documentreader.webclient.gen.model.text import Text
from regula.documentreader.webclient.gen.model.text_available_source import TextAvailableSource
from regula.documentreader.webclient.gen.model.text_data_result import TextDataResult
from regula.documentreader.webclient.gen.model.text_data_result_all_of import TextDataResultAllOf
from regula.documentreader.webclient.gen.model.text_field import TextField
from regula.documentreader.webclient.gen.model.text_field_type import TextFieldType
from regula.documentreader.webclient.gen.model.text_field_value import TextFieldValue
from regula.documentreader.webclient.gen.model.text_result import TextResult
from regula.documentreader.webclient.gen.model.text_result_all_of import TextResultAllOf
from regula.documentreader.webclient.gen.model.transaction_info import TransactionInfo
from regula.documentreader.webclient.gen.model.verification_result import VerificationResult
from regula.documentreader.webclient.gen.model.verified_field_map import VerifiedFieldMap
