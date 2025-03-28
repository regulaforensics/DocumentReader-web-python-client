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
class TextFieldType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    DOCUMENT_CLASS_CODE = int("0")

    ISSUING_STATE_CODE = int("1")

    DOCUMENT_NUMBER = int("2")

    DATE_OF_EXPIRY = int("3")

    DATE_OF_ISSUE = int("4")

    DATE_OF_BIRTH = int("5")

    PLACE_OF_BIRTH = int("6")

    PERSONAL_NUMBER = int("7")

    SURNAME = int("8")

    GIVEN_NAMES = int("9")

    MOTHERS_NAME = int("10")

    NATIONALITY = int("11")

    SEX = int("12")

    HEIGHT = int("13")

    WEIGHT = int("14")

    EYES_COLOR = int("15")

    HAIR_COLOR = int("16")

    ADDRESS = int("17")

    DONOR = int("18")

    SOCIAL_SECURITY_NUMBER = int("19")

    DL_CLASS = int("20")

    DL_ENDORSED = int("21")

    DL_RESTRICTION_CODE = int("22")

    DL_UNDER_21_DATE = int("23")

    AUTHORITY = int("24")

    SURNAME_AND_GIVEN_NAMES = int("25")

    NATIONALITY_CODE = int("26")

    PASSPORT_NUMBER = int("27")

    INVITATION_NUMBER = int("28")

    VISA_ID = int("29")

    VISA_CLASS = int("30")

    VISA_SUBCLASS = int("31")

    MRZ_TYPE = int("35")

    OPTIONAL_DATA = int("36")

    DOCUMENT_CLASS_NAME = int("37")

    ISSUING_STATE_NAME = int("38")

    PLACE_OF_ISSUE = int("39")

    DOCUMENT_NUMBER_CHECKSUM = int("40")

    DATE_OF_BIRTH_CHECKSUM = int("41")

    DATE_OF_EXPIRY_CHECKSUM = int("42")

    PERSONAL_NUMBER_CHECKSUM = int("43")

    FINAL_CHECKSUM = int("44")

    PASSPORT_NUMBER_CHECKSUM = int("45")

    INVITATION_NUMBER_CHECKSUM = int("46")

    VISA_ID_CHECKSUM = int("47")

    SURNAME_AND_GIVEN_NAMES_CHECKSUM = int("48")

    VISA_VALID_UNTIL_CHECKSUM = int("49")

    OTHER = int("50")

    MRZ_STRINGS = int("51")

    NAME_SUFFIX = int("52")

    NAME_PREFIX = int("53")

    DATE_OF_ISSUE_CHECKSUM = int("54")

    DATE_OF_ISSUE_CHECK_DIGIT = int("55")

    DOCUMENT_SERIES = int("56")

    REG_CERT_REG_NUMBER = int("57")

    REG_CERT_CAR_MODEL = int("58")

    REG_CERT_CAR_COLOR = int("59")

    REG_CERT_BODY_NUMBER = int("60")

    REG_CERT_CAR_TYPE = int("61")

    REG_CERT_MAX_WEIGHT = int("62")

    REG_CERT_WEIGHT = int("63")

    ADDRESS_AREA = int("64")

    ADDRESS_STATE = int("65")

    ADDRESS_BUILDING = int("66")

    ADDRESS_HOUSE = int("67")

    ADDRESS_FLAT = int("68")

    PLACE_OF_REGISTRATION = int("69")

    DATE_OF_REGISTRATION = int("70")

    RESIDENT_FROM = int("71")

    RESIDENT_UNTIL = int("72")

    AUTHORITY_CODE = int("73")

    PLACE_OF_BIRTH_AREA = int("74")

    PLACE_OF_BIRTH_STATE_CODE = int("75")

    ADDRESS_STREET = int("76")

    ADDRESS_CITY = int("77")

    ADDRESS_JURISDICTION_CODE = int("78")

    ADDRESS_POSTAL_CODE = int("79")

    DOCUMENT_NUMBER_CHECK_DIGIT = int("80")

    DATE_OF_BIRTH_CHECK_DIGIT = int("81")

    DATE_OF_EXPIRY_CHECK_DIGIT = int("82")

    PERSONAL_NUMBER_CHECK_DIGIT = int("83")

    FINAL_CHECK_DIGIT = int("84")

    PASSPORT_NUMBER_CHECK_DIGIT = int("85")

    INVITATION_NUMBER_CHECK_DIGIT = int("86")

    VISA_ID_CHECK_DIGIT = int("87")

    SURNAME_AND_GIVEN_NAMES_CHECK_DIGIT = int("88")

    VISA_VALID_UNTIL_CHECK_DIGIT = int("89")

    PERMIT_DL_CLASS = int("90")

    PERMIT_DATE_OF_EXPIRY = int("91")

    PERMIT_IDENTIFIER = int("92")

    PERMIT_DATE_OF_ISSUE = int("93")

    PERMIT_RESTRICTION_CODE = int("94")

    PERMIT_ENDORSED = int("95")

    ISSUE_TIMESTAMP = int("96")

    NUMBER_OF_DUPLICATES = int("97")

    MEDICAL_INDICATOR_CODES = int("98")

    NON_RESIDENT_INDICATOR = int("99")

    VISA_TYPE = int("100")

    VISA_VALID_FROM = int("101")

    VISA_VALID_UNTIL = int("102")

    DURATION_OF_STAY = int("103")

    NUMBER_OF_ENTRIES = int("104")

    DAY = int("105")

    MONTH = int("106")

    YEAR = int("107")

    UNIQUE_CUSTOMER_IDENTIFIER = int("108")

    COMMERCIAL_VEHICLE_CODES = int("109")

    AKA_DATE_OF_BIRTH = int("110")

    AKA_SOCIAL_SECURITY_NUMBER = int("111")

    AKA_SURNAME = int("112")

    AKA_GIVEN_NAMES = int("113")

    AKA_NAME_SUFFIX = int("114")

    AKA_NAME_PREFIX = int("115")

    MAILING_ADDRESS_STREET = int("116")

    MAILING_ADDRESS_CITY = int("117")

    MAILING_ADDRESS_JURISDICTION_CODE = int("118")

    MAILING_ADDRESS_POSTAL_CODE = int("119")

    AUDIT_INFORMATION = int("120")

    INVENTORY_NUMBER = int("121")

    RACE_ETHNICITY = int("122")

    JURISDICTION_VEHICLE_CLASS = int("123")

    JURISDICTION_ENDORSEMENT_CODE = int("124")

    JURISDICTION_RESTRICTION_CODE = int("125")

    FAMILY_NAME = int("126")

    GIVEN_NAMES_RUS = int("127")

    VISA_ID_RUS = int("128")

    FATHERS_NAME = int("129")

    FATHERS_NAME_RUS = int("130")

    SURNAME_AND_GIVEN_NAMES_RUS = int("131")

    PLACE_OF_BIRTH_RUS = int("132")

    AUTHORITY_RUS = int("133")

    ISSUING_STATE_CODE_NUMERIC = int("134")

    NATIONALITY_CODE_NUMERIC = int("135")

    ENGINE_POWER = int("136")

    ENGINE_VOLUME = int("137")

    CHASSIS_NUMBER = int("138")

    ENGINE_NUMBER = int("139")

    ENGINE_MODEL = int("140")

    VEHICLE_CATEGORY = int("141")

    IDENTITY_CARD_NUMBER = int("142")

    CONTROL_NUMBER = int("143")

    PARENTS_GIVEN_NAMES = int("144")

    SECOND_SURNAME = int("145")

    MIDDLE_NAME = int("146")

    REG_CERT_VIN = int("147")

    REG_CERT_VIN_CHECK_DIGIT = int("148")

    REG_CERT_VIN_CHECKSUM = int("149")

    LINE_1_CHECK_DIGIT = int("150")

    LINE_2_CHECK_DIGIT = int("151")

    LINE_3_CHECK_DIGIT = int("152")

    LINE_1_CHECKSUM = int("153")

    LINE_2_CHECKSUM = int("154")

    LINE_3_CHECKSUM = int("155")

    REG_CERT_REG_NUMBER_CHECK_DIGIT = int("156")

    REG_CERT_REG_NUMBER_CHECKSUM = int("157")

    REG_CERT_VEHICLE_ITS_CODE = int("158")

    CARD_ACCESS_NUMBER = int("159")

    MARITAL_STATUS = int("160")

    COMPANY_NAME = int("161")

    SPECIAL_NOTES = int("162")

    SURNAME_OF_SPOUSE = int("163")

    TRACKING_NUMBER = int("164")

    BOOKLET_NUMBER = int("165")

    CHILDREN = int("166")

    COPY = int("167")

    SERIAL_NUMBER = int("168")

    DOSSIER_NUMBER = int("169")

    AKA_SURNAME_AND_GIVEN_NAMES = int("170")

    TERRITORIAL_VALIDITY = int("171")

    MRZ_STRINGS_WITH_CORRECT_CHECK_SUMS = int("172")

    DL_CDL_RESTRICTION_CODE = int("173")

    DL_UNDER_18_DATE = int("174")

    DL_RECORD_CREATED = int("175")

    DL_DUPLICATE_DATE = int("176")

    DL_ISSUE_TYPE = int("177")

    MILITARY_BOOK_NUMBER = int("178")

    DESTINATION = int("179")

    BLOOD_GROUP = int("180")

    SEQUENCE_NUMBER = int("181")

    REG_CERT_BODY_TYPE = int("182")

    REG_CERT_CAR_MARK = int("183")

    TRANSACTION_NUMBER = int("184")

    AGE = int("185")

    FOLIO_NUMBER = int("186")

    VOTER_KEY = int("187")

    ADDRESS_MUNICIPALITY = int("188")

    ADDRESS_LOCATION = int("189")

    SECTION = int("190")

    OCR_NUMBER = int("191")

    FEDERAL_ELECTIONS = int("192")

    REFERENCE_NUMBER = int("193")

    OPTIONAL_DATA_CHECKSUM = int("194")

    OPTIONAL_DATA_CHECK_DIGIT = int("195")

    VISA_NUMBER = int("196")

    VISA_NUMBER_CHECKSUM = int("197")

    VISA_NUMBER_CHECK_DIGIT = int("198")

    VOTER = int("199")

    PREVIOUS_TYPE = int("200")

    FIELD_FROM_MRZ = int("220")

    CURRENT_DATE = int("221")

    STATUS_DATE_OF_EXPIRY = int("251")

    BANKNOTE_NUMBER = int("252")

    CSC_CODE = int("253")

    ARTISTIC_NAME = int("254")

    ACADEMIC_TITLE = int("255")

    ADDRESS_COUNTRY = int("256")

    ADDRESS_ZIP_CODE = int("257")

    E_ID_RESIDENCE_PERMIT_1 = int("258")

    E_ID_RESIDENCE_PERMIT_2 = int("259")

    E_ID_PLACE_OF_BIRTH_STREET = int("260")

    E_ID_PLACE_OF_BIRTH_CITY = int("261")

    E_ID_PLACE_OF_BIRTH_STATE = int("262")

    E_ID_PLACE_OF_BIRTH_COUNTRY = int("263")

    E_ID_PLACE_OF_BIRTH_ZIP_CODE = int("264")

    CDL_CLASS = int("265")

    DL_UNDER_19_DATE = int("266")

    WEIGHT_POUNDS = int("267")

    LIMITED_DURATION_DOCUMENT_INDICATOR = int("268")

    ENDORSEMENT_EXPIRATION_DATE = int("269")

    REVISION_DATE = int("270")

    COMPLIANCE_TYPE = int("271")

    FAMILY_NAME_TRUNCATION = int("272")

    FIRST_NAME_TRUNCATION = int("273")

    MIDDLE_NAME_TRUNCATION = int("274")

    EXAM_DATE = int("275")

    ORGANIZATION = int("276")

    DEPARTMENT = int("277")

    PAY_GRADE = int("278")

    RANK = int("279")

    BENEFITS_NUMBER = int("280")

    SPONSOR_SERVICE = int("281")

    SPONSOR_STATUS = int("282")

    SPONSOR = int("283")

    RELATIONSHIP = int("284")

    USCIS = int("285")

    CATEGORY = int("286")

    CONDITIONS = int("287")

    IDENTIFIER = int("288")

    CONFIGURATION = int("289")

    DISCRETIONARY_DATA = int("290")

    LINE_1_OPTIONAL_DATA = int("291")

    LINE_2_OPTIONAL_DATA = int("292")

    LINE_3_OPTIONAL_DATA = int("293")

    EQV_CODE = int("294")

    ALT_CODE = int("295")

    BINARY_CODE = int("296")

    PSEUDO_CODE = int("297")

    FEE = int("298")

    STAMP_NUMBER = int("299")

    SBH_SECURITY_OPTIONS = int("300")

    SBH_INTEGRITY_OPTIONS = int("301")

    DATE_OF_CREATION = int("302")

    VALIDITY_PERIOD = int("303")

    PATRON_HEADER_VERSION = int("304")

    BDB_TYPE = int("305")

    BIOMETRIC_TYPE = int("306")

    BIOMETRIC_SUBTYPE = int("307")

    BIOMETRIC_PRODUCT_ID = int("308")

    BIOMETRIC_FORMAT_OWNER = int("309")

    BIOMETRIC_FORMAT_TYPE = int("310")

    PHONE = int("311")

    PROFESSION = int("312")

    TITLE = int("313")

    PERSONAL_SUMMARY = int("314")

    OTHER_VALID_ID = int("315")

    CUSTODY_INFO = int("316")

    OTHER_NAME = int("317")

    OBSERVATIONS = int("318")

    TAX = int("319")

    DATE_OF_PERSONALIZATION = int("320")

    PERSONALIZATION_SN = int("321")

    OTHER_PERSON_NAME = int("322")

    PERSON_TO_NOTIFY_DATE_OF_RECORD = int("323")

    PERSON_TO_NOTIFY_NAME = int("324")

    PERSON_TO_NOTIFY_PHONE = int("325")

    PERSON_TO_NOTIFY_ADDRESS = int("326")

    DS_CERTIFICATE_ISSUER = int("327")

    DS_CERTIFICATE_SUBJECT = int("328")

    DS_CERTIFICATE_VALID_FROM = int("329")

    DS_CERTIFICATE_VALID_TO = int("330")

    VRC_DATA_OBJECT_ENTRY = int("331")

    TYPE_APPROVAL_NUMBER = int("332")

    ADMINISTRATIVE_NUMBER = int("333")

    DOCUMENT_DISCRIMINATOR = int("334")

    DATA_DISCRIMINATOR = int("335")

    ISO_ISSUER_ID_NUMBER = int("336")

    DTC_VERSION = int("337")

    DTC_ID = int("338")

    DTC_DATE_OF_EXPIRY = int("339")

    GNIB_NUMBER = int("340")

    DEPT_NUMBER = int("341")

    TELEX_CODE = int("342")

    ALLERGIES = int("343")

    SP_CODE = int("344")

    COURT_CODE = int("345")

    CTY = int("346")

    SPONSOR_SSN = int("347")

    DOD_NUMBER = int("348")

    MC_NOVICE_DATE = int("349")

    DUF_NUMBER = int("350")

    AGY = int("351")

    PNR_CODE = int("352")

    FROM_AIRPORT_CODE = int("353")

    TO_AIRPORT_CODE = int("354")

    FLIGHT_NUMBER = int("355")

    DATE_OF_FLIGHT = int("356")

    SEAT_NUMBER = int("357")

    DATE_OF_ISSUE_BOARDING_PASS = int("358")

    CCW_UNTIL = int("359")

    REFERENCE_NUMBER_CHECKSUM = int("360")

    REFERENCE_NUMBER_CHECK_DIGIT = int("361")

    ROOM_NUMBER = int("362")

    RELIGION = int("363")

    REMAINDER_TERM = int("364")

    ELECTRONIC_TICKET_INDICATOR = int("365")

    COMPARTMENT_CODE = int("366")

    CHECK_IN_SEQUENCE_NUMBER = int("367")

    AIRLINE_DESIGNATOR_OF_BOARDING_PASS_ISSUER = int("368")

    AIRLINE_NUMERIC_CODE = int("369")

    TICKET_NUMBER = int("370")

    FREQUENT_FLYER_AIRLINE_DESIGNATOR = int("371")

    FREQUENT_FLYER_NUMBER = int("372")

    FREE_BAGGAGE_ALLOWANCE = int("373")

    PDF417_CODEC = int("374")

    IDENTITY_CARD_NUMBER_CHECKSUM = int("375")

    IDENTITY_CARD_NUMBER_CHECK_DIGIT = int("376")

    VETERAN = int("377")

    DL_CLASS_CODE_A1_FROM = int("378")

    DL_CLASS_CODE_A1_TO = int("379")

    DL_CLASS_CODE_A1_NOTES = int("380")

    DL_CLASS_CODE_A_FROM = int("381")

    DL_CLASS_CODE_A_TO = int("382")

    DL_CLASS_CODE_A_NOTES = int("383")

    DL_CLASS_CODE_B_FROM = int("384")

    DL_CLASS_CODE_B_TO = int("385")

    DL_CLASS_CODE_B_NOTES = int("386")

    DL_CLASS_CODE_C1_FROM = int("387")

    DL_CLASS_CODE_C1_TO = int("388")

    DL_CLASS_CODE_C1_NOTES = int("389")

    DL_CLASS_CODE_C_FROM = int("390")

    DL_CLASS_CODE_C_TO = int("391")

    DL_CLASS_CODE_C_NOTES = int("392")

    DL_CLASS_CODE_D1_FROM = int("393")

    DL_CLASS_CODE_D1_TO = int("394")

    DL_CLASS_CODE_D1_NOTES = int("395")

    DL_CLASS_CODE_D_FROM = int("396")

    DL_CLASS_CODE_D_TO = int("397")

    DL_CLASS_CODE_D_NOTES = int("398")

    DL_CLASS_CODE_BE_FROM = int("399")

    DL_CLASS_CODE_BE_TO = int("400")

    DL_CLASS_CODE_BE_NOTES = int("401")

    DL_CLASS_CODE_C1E_FROM = int("402")

    DL_CLASS_CODE_C1E_TO = int("403")

    DL_CLASS_CODE_C1E_NOTES = int("404")

    DL_CLASS_CODE_CE_FROM = int("405")

    DL_CLASS_CODE_CE_TO = int("406")

    DL_CLASS_CODE_CE_NOTES = int("407")

    DL_CLASS_CODE_D1E_FROM = int("408")

    DL_CLASS_CODE_D1E_TO = int("409")

    DL_CLASS_CODE_D1E_NOTES = int("410")

    DL_CLASS_CODE_DE_FROM = int("411")

    DL_CLASS_CODE_DE_TO = int("412")

    DL_CLASS_CODE_DE_NOTES = int("413")

    DL_CLASS_CODE_M_FROM = int("414")

    DL_CLASS_CODE_M_TO = int("415")

    DL_CLASS_CODE_M_NOTES = int("416")

    DL_CLASS_CODE_L_FROM = int("417")

    DL_CLASS_CODE_L_TO = int("418")

    DL_CLASS_CODE_L_NOTES = int("419")

    DL_CLASS_CODE_T_FROM = int("420")

    DL_CLASS_CODE_T_TO = int("421")

    DL_CLASS_CODE_T_NOTES = int("422")

    DL_CLASS_CODE_AM_FROM = int("423")

    DL_CLASS_CODE_AM_TO = int("424")

    DL_CLASS_CODE_AM_NOTES = int("425")

    DL_CLASS_CODE_A2_FROM = int("426")

    DL_CLASS_CODE_A2_TO = int("427")

    DL_CLASS_CODE_A2_NOTES = int("428")

    DL_CLASS_CODE_B1_FROM = int("429")

    DL_CLASS_CODE_B1_TO = int("430")

    DL_CLASS_CODE_B1_NOTES = int("431")

    SURNAME_AT_BIRTH = int("432")

    CIVIL_STATUS = int("433")

    NUMBER_OF_SEATS = int("434")

    NUMBER_OF_STANDING_PLACES = int("435")

    MAX_SPEED = int("436")

    FUEL_TYPE = int("437")

    EC_ENVIRONMENTAL_TYPE = int("438")

    POWER_WEIGHT_RATIO = int("439")

    MAX_MASS_OF_TRAILER_BRAKED = int("440")

    MAX_MASS_OF_TRAILER_UNBRAKED = int("441")

    TRANSMISSION_TYPE = int("442")

    TRAILER_HITCH = int("443")

    ACCOMPANIED_BY = int("444")

    POLICE_DISTRICT = int("445")

    FIRST_ISSUE_DATE = int("446")

    PAYLOAD_CAPACITY = int("447")

    NUMBER_OF_AXLES = int("448")

    PERMISSIBLE_AXLE_LOAD = int("449")

    PRECINCT = int("450")

    INVITED_BY = int("451")

    PURPOSE_OF_ENTRY = int("452")

    SKIN_COLOR = int("453")

    COMPLEXION = int("454")

    AIRPORT_FROM = int("455")

    AIRPORT_TO = int("456")

    AIRLINE_NAME = int("457")

    AIRLINE_NAME_FREQUENT_FLYER = int("458")

    LICENSE_NUMBER = int("459")

    IN_TANKS = int("460")

    EXCEPT_IN_TANKS = int("461")

    FAST_TRACK = int("462")

    OWNER = int("463")

    MRZ_STRINGS_ICAO_RFID = int("464")

    NUMBER_OF_CARD_ISSUANCE = int("465")

    NUMBER_OF_CARD_ISSUANCE_CHECKSUM = int("466")

    NUMBER_OF_CARD_ISSUANCE_CHECK_DIGIT = int("467")

    CENTURY_DATE_OF_BIRTH = int("468")

    DL_CLASS_CODE_A3_FROM = int("469")

    DL_CLASS_CODE_A3_TO = int("470")

    DL_CLASS_CODE_A3_NOTES = int("471")

    DL_CLASS_CODE_C2_FROM = int("472")

    DL_CLASS_CODE_C2_TO = int("473")

    DL_CLASS_CODE_C2_NOTES = int("474")

    DL_CLASS_CODE_B2_FROM = int("475")

    DL_CLASS_CODE_B2_TO = int("476")

    DL_CLASS_CODE_B2_NOTES = int("477")

    DL_CLASS_CODE_D2_FROM = int("478")

    DL_CLASS_CODE_D2_TO = int("479")

    DL_CLASS_CODE_D2_NOTES = int("480")

    DL_CLASS_CODE_B2E_FROM = int("481")

    DL_CLASS_CODE_B2E_TO = int("482")

    DL_CLASS_CODE_B2E_NOTES = int("483")

    DL_CLASS_CODE_G_FROM = int("484")

    DL_CLASS_CODE_G_TO = int("485")

    DL_CLASS_CODE_G_NOTES = int("486")

    DL_CLASS_CODE_J_FROM = int("487")

    DL_CLASS_CODE_J_TO = int("488")

    DL_CLASS_CODE_J_NOTES = int("489")

    DL_CLASS_CODE_LC_FROM = int("490")

    DL_CLASS_CODE_LC_TO = int("491")

    DL_CLASS_CODE_LC_NOTES = int("492")

    BANK_CARD_NUMBER = int("493")

    BANK_CARD_VALID_THRU = int("494")

    TAX_NUMBER = int("495")

    HEALTH_NUMBER = int("496")

    GRANDFATHER_NAME = int("497")

    SELECTEE_INDICATOR = int("498")

    MOTHER_SURNAME = int("499")

    MOTHER_GIVEN_NAME = int("500")

    FATHER_SURNAME = int("501")

    FATHER_GIVEN_NAME = int("502")

    MOTHER_DATE_OF_BIRTH = int("503")

    FATHER_DATE_OF_BIRTH = int("504")

    MOTHER_PERSONAL_NUMBER = int("505")

    FATHER_PERSONAL_NUMBER = int("506")

    MOTHER_PLACE_OF_BIRTH = int("507")

    FATHER_PLACE_OF_BIRTH = int("508")

    MOTHER_COUNTRY_OF_BIRTH = int("509")

    FATHER_COUNTRY_OF_BIRTH = int("510")

    DATE_FIRST_RENEWAL = int("511")

    DATE_SECOND_RENEWAL = int("512")

    PLACE_OF_EXAMINATION = int("513")

    APPLICATION_NUMBER = int("514")

    VOUCHER_NUMBER = int("515")

    AUTHORIZATION_NUMBER = int("516")

    FACULTY = int("517")

    FORM_OF_EDUCATION = int("518")

    DNI_NUMBER = int("519")

    RETIREMENT_NUMBER = int("520")

    PROFESSIONAL_ID_NUMBER = int("521")

    AGE_AT_ISSUE = int("522")

    YEARS_SINCE_ISSUE = int("523")

    DL_CLASS_CODE_BTP_FROM = int("524")

    DL_CLASS_CODE_BTP_NOTES = int("525")

    DL_CLASS_CODE_BTP_TO = int("526")

    DL_CLASS_CODE_C3_FROM = int("527")

    DL_CLASS_CODE_C3_NOTES = int("528")

    DL_CLASS_CODE_C3_TO = int("529")

    DL_CLASS_CODE_E_FROM = int("530")

    DL_CLASS_CODE_E_NOTES = int("531")

    DL_CLASS_CODE_E_TO = int("532")

    DL_CLASS_CODE_F_FROM = int("533")

    DL_CLASS_CODE_F_NOTES = int("534")

    DL_CLASS_CODE_F_TO = int("535")

    DL_CLASS_CODE_FA_FROM = int("536")

    DL_CLASS_CODE_FA_NOTES = int("537")

    DL_CLASS_CODE_FA_TO = int("538")

    DL_CLASS_CODE_FA1_FROM = int("539")

    DL_CLASS_CODE_FA1_NOTES = int("540")

    DL_CLASS_CODE_FA1_TO = int("541")

    DL_CLASS_CODE_FB_FROM = int("542")

    DL_CLASS_CODE_FB_NOTES = int("543")

    DL_CLASS_CODE_FB_TO = int("544")

    DL_CLASS_CODE_G1_FROM = int("545")

    DL_CLASS_CODE_G1_NOTES = int("546")

    DL_CLASS_CODE_G1_TO = int("547")

    DL_CLASS_CODE_H_FROM = int("548")

    DL_CLASS_CODE_H_NOTES = int("549")

    DL_CLASS_CODE_H_TO = int("550")

    DL_CLASS_CODE_I_FROM = int("551")

    DL_CLASS_CODE_I_NOTES = int("552")

    DL_CLASS_CODE_I_TO = int("553")

    DL_CLASS_CODE_K_FROM = int("554")

    DL_CLASS_CODE_K_NOTES = int("555")

    DL_CLASS_CODE_K_TO = int("556")

    DL_CLASS_CODE_LK_FROM = int("557")

    DL_CLASS_CODE_LK_NOTES = int("558")

    DL_CLASS_CODE_LK_TO = int("559")

    DL_CLASS_CODE_N_FROM = int("560")

    DL_CLASS_CODE_N_NOTES = int("561")

    DL_CLASS_CODE_N_TO = int("562")

    DL_CLASS_CODE_S_FROM = int("563")

    DL_CLASS_CODE_S_NOTES = int("564")

    DL_CLASS_CODE_S_TO = int("565")

    DL_CLASS_CODE_TB_FROM = int("566")

    DL_CLASS_CODE_TB_NOTES = int("567")

    DL_CLASS_CODE_TB_TO = int("568")

    DL_CLASS_CODE_TM_FROM = int("569")

    DL_CLASS_CODE_TM_NOTES = int("570")

    DL_CLASS_CODE_TM_TO = int("571")

    DL_CLASS_CODE_TR_FROM = int("572")

    DL_CLASS_CODE_TR_NOTES = int("573")

    DL_CLASS_CODE_TR_TO = int("574")

    DL_CLASS_CODE_TV_FROM = int("575")

    DL_CLASS_CODE_TV_NOTES = int("576")

    DL_CLASS_CODE_TV_TO = int("577")

    DL_CLASS_CODE_V_FROM = int("578")

    DL_CLASS_CODE_V_NOTES = int("579")

    DL_CLASS_CODE_V_TO = int("580")

    DL_CLASS_CODE_W_FROM = int("581")

    DL_CLASS_CODE_W_NOTES = int("582")

    DL_CLASS_CODE_W_TO = int("583")

    URL = int("584")

    CALIBER = int("585")

    MODEL = int("586")

    MAKE = int("587")

    NUMBER_OF_CYLINDERS = int("588")

    SURNAME_OF_HUSBAND_AFTER_REGISTRATION = int("589")

    SURNAME_OF_WIFE_AFTER_REGISTRATION = int("590")

    DATE_OF_BIRTH_OF_WIFE = int("591")

    DATE_OF_BIRTH_OF_HUSBAND = int("592")

    CITIZENSHIP_OF_FIRST_PERSON = int("593")

    CITIZENSHIP_OF_SECOND_PERSON = int("594")

    CVV = int("595")

    DATE_OF_INSURANCE_EXPIRY = int("596")

    MORTGAGE_BY = int("597")

    OLD_DOCUMENT_NUMBER = int("598")

    OLD_DATE_OF_ISSUE = int("599")

    OLD_PLACE_OF_ISSUE = int("600")

    DL_CLASS_CODE_LR_FROM = int("601")

    DL_CLASS_CODE_LR_TO = int("602")

    DL_CLASS_CODE_LR_NOTES = int("603")

    DL_CLASS_CODE_MR_FROM = int("604")

    DL_CLASS_CODE_MR_TO = int("605")

    DL_CLASS_CODE_MR_NOTES = int("606")

    DL_CLASS_CODE_HR_FROM = int("607")

    DL_CLASS_CODE_HR_TO = int("608")

    DL_CLASS_CODE_HR_NOTES = int("609")

    DL_CLASS_CODE_HC_FROM = int("610")

    DL_CLASS_CODE_HC_TO = int("611")

    DL_CLASS_CODE_HC_NOTES = int("612")

    DL_CLASS_CODE_MC_FROM = int("613")

    DL_CLASS_CODE_MC_TO = int("614")

    DL_CLASS_CODE_MC_NOTES = int("615")

    DL_CLASS_CODE_RE_FROM = int("616")

    DL_CLASS_CODE_RE_TO = int("617")

    DL_CLASS_CODE_RE_NOTES = int("618")

    DL_CLASS_CODE_R_FROM = int("619")

    DL_CLASS_CODE_R_TO = int("620")

    DL_CLASS_CODE_R_NOTES = int("621")

    DL_CLASS_CODE_CA_FROM = int("622")

    DL_CLASS_CODE_CA_TO = int("623")

    DL_CLASS_CODE_CA_NOTES = int("624")

    CITIZENSHIP_STATUS = int("625")

    MILITARY_SERVICE_FROM = int("626")

    MILITARY_SERVICE_TO = int("627")

    DL_CLASS_CODE_NT_FROM = int("628")

    DL_CLASS_CODE_NT_TO = int("629")

    DL_CLASS_CODE_NT_NOTES = int("630")

    DL_CLASS_CODE_TN_FROM = int("631")

    DL_CLASS_CODE_TN_TO = int("632")

    DL_CLASS_CODE_TN_NOTES = int("633")

    DL_CLASS_CODE_D3_FROM = int("634")

    DL_CLASS_CODE_D3_TO = int("635")

    DL_CLASS_CODE_D3_NOTES = int("636")

    ALT_DATE_OF_EXPIRY = int("637")

    DL_CLASS_CODE_CD_FROM = int("638")

    DL_CLASS_CODE_CD_TO = int("639")

    DL_CLASS_CODE_CD_NOTES = int("640")

    ISSUER_IDENTIFICATION_NUMBER = int("641")

    PAYMENT_PERIOD_FROM = int("642")

    PAYMENT_PERIOD_TO = int("643")

    VACCINATION_CERTIFICATE_IDENTIFIER = int("644")

    FIRST_NAME = int("645")

    DATE_OF_ARRIVAL = int("646")

    SECOND_NAME = int("647")

    THIRD_NAME = int("648")

    FOURTH_NAME = int("649")

    LAST_NAME = int("650")

    DL_CLASS_CODE_RM_FROM = int("651")

    DL_CLASS_CODE_RM_NOTES = int("652")

    DL_CLASS_CODE_RM_TO = int("653")

    DL_CLASS_CODE_PW_FROM = int("654")

    DL_CLASS_CODE_PW_NOTES = int("655")

    DL_CLASS_CODE_PW_TO = int("656")

    DL_CLASS_CODE_EB_FROM = int("657")

    DL_CLASS_CODE_EB_NOTES = int("658")

    DL_CLASS_CODE_EB_TO = int("659")

    DL_CLASS_CODE_EC_FROM = int("660")

    DL_CLASS_CODE_EC_NOTES = int("661")

    DL_CLASS_CODE_EC_TO = int("662")

    DL_CLASS_CODE_EC1_FROM = int("663")

    DL_CLASS_CODE_EC1_NOTES = int("664")

    DL_CLASS_CODE_EC1_TO = int("665")

    PLACE_OF_BIRTH_CITY = int("666")

    YEAR_OF_BIRTH = int("667")

    YEAR_OF_EXPIRY = int("668")

    GRANDFATHER_NAME_MATERNAL = int("669")

    FIRST_SURNAME = int("670")

    MONTH_OF_BIRTH = int("671")

    ADDRESS_FLOOR_NUMBER = int("672")

    ADDRESS_ENTRANCE = int("673")

    ADDRESS_BLOCK_NUMBER = int("674")

    ADDRESS_STREET_NUMBER = int("675")

    ADDRESS_STREET_TYPE = int("676")

    ADDRESS_CITY_SECTOR = int("677")

    ADDRESS_COUNTY_TYPE = int("678")

    ADDRESS_CITY_TYPE = int("679")

    ADDRESS_BUILDING_TYPE = int("680")

    DATE_OF_RETIREMENT = int("681")

    DOCUMENT_STATUS = int("682")

    SIGNATURE = int("683")

    FT_UNIQUE_CERTIFICATE_IDENTIFIER = int("684")

    FT_EMAIL = int("685")

    FT_DATE_OF_SPECIMEN_COLLECTION = int("686")

    FT_TYPE_OF_TESTING = int("687")

    FT_RESULT_OF_TESTING = int("688")

    FT_METHOD_OF_TESTING = int("689")

    FT_DIGITAL_TRAVEL_AUTHORIZATION_NUMBER = int("690")

    FT_DATE_OF_FIRST_POSITIVE_TEST_RESULT = int("691")

    EF_CARD_ACCESS = int("692")

    SHORT_FLIGHT_NUMBER = int("693")

    AIRLINE_CODE = int("694")

    allowable_values = [DOCUMENT_CLASS_CODE, ISSUING_STATE_CODE, DOCUMENT_NUMBER, DATE_OF_EXPIRY, DATE_OF_ISSUE, DATE_OF_BIRTH, PLACE_OF_BIRTH, PERSONAL_NUMBER, SURNAME, GIVEN_NAMES, MOTHERS_NAME, NATIONALITY, SEX, HEIGHT, WEIGHT, EYES_COLOR, HAIR_COLOR, ADDRESS, DONOR, SOCIAL_SECURITY_NUMBER, DL_CLASS, DL_ENDORSED, DL_RESTRICTION_CODE, DL_UNDER_21_DATE, AUTHORITY, SURNAME_AND_GIVEN_NAMES, NATIONALITY_CODE, PASSPORT_NUMBER, INVITATION_NUMBER, VISA_ID, VISA_CLASS, VISA_SUBCLASS, MRZ_TYPE, OPTIONAL_DATA, DOCUMENT_CLASS_NAME, ISSUING_STATE_NAME, PLACE_OF_ISSUE, DOCUMENT_NUMBER_CHECKSUM, DATE_OF_BIRTH_CHECKSUM, DATE_OF_EXPIRY_CHECKSUM, PERSONAL_NUMBER_CHECKSUM, FINAL_CHECKSUM, PASSPORT_NUMBER_CHECKSUM, INVITATION_NUMBER_CHECKSUM, VISA_ID_CHECKSUM, SURNAME_AND_GIVEN_NAMES_CHECKSUM, VISA_VALID_UNTIL_CHECKSUM, OTHER, MRZ_STRINGS, NAME_SUFFIX, NAME_PREFIX, DATE_OF_ISSUE_CHECKSUM, DATE_OF_ISSUE_CHECK_DIGIT, DOCUMENT_SERIES, REG_CERT_REG_NUMBER, REG_CERT_CAR_MODEL, REG_CERT_CAR_COLOR, REG_CERT_BODY_NUMBER, REG_CERT_CAR_TYPE, REG_CERT_MAX_WEIGHT, REG_CERT_WEIGHT, ADDRESS_AREA, ADDRESS_STATE, ADDRESS_BUILDING, ADDRESS_HOUSE, ADDRESS_FLAT, PLACE_OF_REGISTRATION, DATE_OF_REGISTRATION, RESIDENT_FROM, RESIDENT_UNTIL, AUTHORITY_CODE, PLACE_OF_BIRTH_AREA, PLACE_OF_BIRTH_STATE_CODE, ADDRESS_STREET, ADDRESS_CITY, ADDRESS_JURISDICTION_CODE, ADDRESS_POSTAL_CODE, DOCUMENT_NUMBER_CHECK_DIGIT, DATE_OF_BIRTH_CHECK_DIGIT, DATE_OF_EXPIRY_CHECK_DIGIT, PERSONAL_NUMBER_CHECK_DIGIT, FINAL_CHECK_DIGIT, PASSPORT_NUMBER_CHECK_DIGIT, INVITATION_NUMBER_CHECK_DIGIT, VISA_ID_CHECK_DIGIT, SURNAME_AND_GIVEN_NAMES_CHECK_DIGIT, VISA_VALID_UNTIL_CHECK_DIGIT, PERMIT_DL_CLASS, PERMIT_DATE_OF_EXPIRY, PERMIT_IDENTIFIER, PERMIT_DATE_OF_ISSUE, PERMIT_RESTRICTION_CODE, PERMIT_ENDORSED, ISSUE_TIMESTAMP, NUMBER_OF_DUPLICATES, MEDICAL_INDICATOR_CODES, NON_RESIDENT_INDICATOR, VISA_TYPE, VISA_VALID_FROM, VISA_VALID_UNTIL, DURATION_OF_STAY, NUMBER_OF_ENTRIES, DAY, MONTH, YEAR, UNIQUE_CUSTOMER_IDENTIFIER, COMMERCIAL_VEHICLE_CODES, AKA_DATE_OF_BIRTH, AKA_SOCIAL_SECURITY_NUMBER, AKA_SURNAME, AKA_GIVEN_NAMES, AKA_NAME_SUFFIX, AKA_NAME_PREFIX, MAILING_ADDRESS_STREET, MAILING_ADDRESS_CITY, MAILING_ADDRESS_JURISDICTION_CODE, MAILING_ADDRESS_POSTAL_CODE, AUDIT_INFORMATION, INVENTORY_NUMBER, RACE_ETHNICITY, JURISDICTION_VEHICLE_CLASS, JURISDICTION_ENDORSEMENT_CODE, JURISDICTION_RESTRICTION_CODE, FAMILY_NAME, GIVEN_NAMES_RUS, VISA_ID_RUS, FATHERS_NAME, FATHERS_NAME_RUS, SURNAME_AND_GIVEN_NAMES_RUS, PLACE_OF_BIRTH_RUS, AUTHORITY_RUS, ISSUING_STATE_CODE_NUMERIC, NATIONALITY_CODE_NUMERIC, ENGINE_POWER, ENGINE_VOLUME, CHASSIS_NUMBER, ENGINE_NUMBER, ENGINE_MODEL, VEHICLE_CATEGORY, IDENTITY_CARD_NUMBER, CONTROL_NUMBER, PARENTS_GIVEN_NAMES, SECOND_SURNAME, MIDDLE_NAME, REG_CERT_VIN, REG_CERT_VIN_CHECK_DIGIT, REG_CERT_VIN_CHECKSUM, LINE_1_CHECK_DIGIT, LINE_2_CHECK_DIGIT, LINE_3_CHECK_DIGIT, LINE_1_CHECKSUM, LINE_2_CHECKSUM, LINE_3_CHECKSUM, REG_CERT_REG_NUMBER_CHECK_DIGIT, REG_CERT_REG_NUMBER_CHECKSUM, REG_CERT_VEHICLE_ITS_CODE, CARD_ACCESS_NUMBER, MARITAL_STATUS, COMPANY_NAME, SPECIAL_NOTES, SURNAME_OF_SPOUSE, TRACKING_NUMBER, BOOKLET_NUMBER, CHILDREN, COPY, SERIAL_NUMBER, DOSSIER_NUMBER, AKA_SURNAME_AND_GIVEN_NAMES, TERRITORIAL_VALIDITY, MRZ_STRINGS_WITH_CORRECT_CHECK_SUMS, DL_CDL_RESTRICTION_CODE, DL_UNDER_18_DATE, DL_RECORD_CREATED, DL_DUPLICATE_DATE, DL_ISSUE_TYPE, MILITARY_BOOK_NUMBER, DESTINATION, BLOOD_GROUP, SEQUENCE_NUMBER, REG_CERT_BODY_TYPE, REG_CERT_CAR_MARK, TRANSACTION_NUMBER, AGE, FOLIO_NUMBER, VOTER_KEY, ADDRESS_MUNICIPALITY, ADDRESS_LOCATION, SECTION, OCR_NUMBER, FEDERAL_ELECTIONS, REFERENCE_NUMBER, OPTIONAL_DATA_CHECKSUM, OPTIONAL_DATA_CHECK_DIGIT, VISA_NUMBER, VISA_NUMBER_CHECKSUM, VISA_NUMBER_CHECK_DIGIT, VOTER, PREVIOUS_TYPE, FIELD_FROM_MRZ, CURRENT_DATE, STATUS_DATE_OF_EXPIRY, BANKNOTE_NUMBER, CSC_CODE, ARTISTIC_NAME, ACADEMIC_TITLE, ADDRESS_COUNTRY, ADDRESS_ZIP_CODE, E_ID_RESIDENCE_PERMIT_1, E_ID_RESIDENCE_PERMIT_2, E_ID_PLACE_OF_BIRTH_STREET, E_ID_PLACE_OF_BIRTH_CITY, E_ID_PLACE_OF_BIRTH_STATE, E_ID_PLACE_OF_BIRTH_COUNTRY, E_ID_PLACE_OF_BIRTH_ZIP_CODE, CDL_CLASS, DL_UNDER_19_DATE, WEIGHT_POUNDS, LIMITED_DURATION_DOCUMENT_INDICATOR, ENDORSEMENT_EXPIRATION_DATE, REVISION_DATE, COMPLIANCE_TYPE, FAMILY_NAME_TRUNCATION, FIRST_NAME_TRUNCATION, MIDDLE_NAME_TRUNCATION, EXAM_DATE, ORGANIZATION, DEPARTMENT, PAY_GRADE, RANK, BENEFITS_NUMBER, SPONSOR_SERVICE, SPONSOR_STATUS, SPONSOR, RELATIONSHIP, USCIS, CATEGORY, CONDITIONS, IDENTIFIER, CONFIGURATION, DISCRETIONARY_DATA, LINE_1_OPTIONAL_DATA, LINE_2_OPTIONAL_DATA, LINE_3_OPTIONAL_DATA, EQV_CODE, ALT_CODE, BINARY_CODE, PSEUDO_CODE, FEE, STAMP_NUMBER, SBH_SECURITY_OPTIONS, SBH_INTEGRITY_OPTIONS, DATE_OF_CREATION, VALIDITY_PERIOD, PATRON_HEADER_VERSION, BDB_TYPE, BIOMETRIC_TYPE, BIOMETRIC_SUBTYPE, BIOMETRIC_PRODUCT_ID, BIOMETRIC_FORMAT_OWNER, BIOMETRIC_FORMAT_TYPE, PHONE, PROFESSION, TITLE, PERSONAL_SUMMARY, OTHER_VALID_ID, CUSTODY_INFO, OTHER_NAME, OBSERVATIONS, TAX, DATE_OF_PERSONALIZATION, PERSONALIZATION_SN, OTHER_PERSON_NAME, PERSON_TO_NOTIFY_DATE_OF_RECORD, PERSON_TO_NOTIFY_NAME, PERSON_TO_NOTIFY_PHONE, PERSON_TO_NOTIFY_ADDRESS, DS_CERTIFICATE_ISSUER, DS_CERTIFICATE_SUBJECT, DS_CERTIFICATE_VALID_FROM, DS_CERTIFICATE_VALID_TO, VRC_DATA_OBJECT_ENTRY, TYPE_APPROVAL_NUMBER, ADMINISTRATIVE_NUMBER, DOCUMENT_DISCRIMINATOR, DATA_DISCRIMINATOR, ISO_ISSUER_ID_NUMBER, DTC_VERSION, DTC_ID, DTC_DATE_OF_EXPIRY, GNIB_NUMBER, DEPT_NUMBER, TELEX_CODE, ALLERGIES, SP_CODE, COURT_CODE, CTY, SPONSOR_SSN, DOD_NUMBER, MC_NOVICE_DATE, DUF_NUMBER, AGY, PNR_CODE, FROM_AIRPORT_CODE, TO_AIRPORT_CODE, FLIGHT_NUMBER, DATE_OF_FLIGHT, SEAT_NUMBER, DATE_OF_ISSUE_BOARDING_PASS, CCW_UNTIL, REFERENCE_NUMBER_CHECKSUM, REFERENCE_NUMBER_CHECK_DIGIT, ROOM_NUMBER, RELIGION, REMAINDER_TERM, ELECTRONIC_TICKET_INDICATOR, COMPARTMENT_CODE, CHECK_IN_SEQUENCE_NUMBER, AIRLINE_DESIGNATOR_OF_BOARDING_PASS_ISSUER, AIRLINE_NUMERIC_CODE, TICKET_NUMBER, FREQUENT_FLYER_AIRLINE_DESIGNATOR, FREQUENT_FLYER_NUMBER, FREE_BAGGAGE_ALLOWANCE, PDF417_CODEC, IDENTITY_CARD_NUMBER_CHECKSUM, IDENTITY_CARD_NUMBER_CHECK_DIGIT, VETERAN, DL_CLASS_CODE_A1_FROM, DL_CLASS_CODE_A1_TO, DL_CLASS_CODE_A1_NOTES, DL_CLASS_CODE_A_FROM, DL_CLASS_CODE_A_TO, DL_CLASS_CODE_A_NOTES, DL_CLASS_CODE_B_FROM, DL_CLASS_CODE_B_TO, DL_CLASS_CODE_B_NOTES, DL_CLASS_CODE_C1_FROM, DL_CLASS_CODE_C1_TO, DL_CLASS_CODE_C1_NOTES, DL_CLASS_CODE_C_FROM, DL_CLASS_CODE_C_TO, DL_CLASS_CODE_C_NOTES, DL_CLASS_CODE_D1_FROM, DL_CLASS_CODE_D1_TO, DL_CLASS_CODE_D1_NOTES, DL_CLASS_CODE_D_FROM, DL_CLASS_CODE_D_TO, DL_CLASS_CODE_D_NOTES, DL_CLASS_CODE_BE_FROM, DL_CLASS_CODE_BE_TO, DL_CLASS_CODE_BE_NOTES, DL_CLASS_CODE_C1E_FROM, DL_CLASS_CODE_C1E_TO, DL_CLASS_CODE_C1E_NOTES, DL_CLASS_CODE_CE_FROM, DL_CLASS_CODE_CE_TO, DL_CLASS_CODE_CE_NOTES, DL_CLASS_CODE_D1E_FROM, DL_CLASS_CODE_D1E_TO, DL_CLASS_CODE_D1E_NOTES, DL_CLASS_CODE_DE_FROM, DL_CLASS_CODE_DE_TO, DL_CLASS_CODE_DE_NOTES, DL_CLASS_CODE_M_FROM, DL_CLASS_CODE_M_TO, DL_CLASS_CODE_M_NOTES, DL_CLASS_CODE_L_FROM, DL_CLASS_CODE_L_TO, DL_CLASS_CODE_L_NOTES, DL_CLASS_CODE_T_FROM, DL_CLASS_CODE_T_TO, DL_CLASS_CODE_T_NOTES, DL_CLASS_CODE_AM_FROM, DL_CLASS_CODE_AM_TO, DL_CLASS_CODE_AM_NOTES, DL_CLASS_CODE_A2_FROM, DL_CLASS_CODE_A2_TO, DL_CLASS_CODE_A2_NOTES, DL_CLASS_CODE_B1_FROM, DL_CLASS_CODE_B1_TO, DL_CLASS_CODE_B1_NOTES, SURNAME_AT_BIRTH, CIVIL_STATUS, NUMBER_OF_SEATS, NUMBER_OF_STANDING_PLACES, MAX_SPEED, FUEL_TYPE, EC_ENVIRONMENTAL_TYPE, POWER_WEIGHT_RATIO, MAX_MASS_OF_TRAILER_BRAKED, MAX_MASS_OF_TRAILER_UNBRAKED, TRANSMISSION_TYPE, TRAILER_HITCH, ACCOMPANIED_BY, POLICE_DISTRICT, FIRST_ISSUE_DATE, PAYLOAD_CAPACITY, NUMBER_OF_AXLES, PERMISSIBLE_AXLE_LOAD, PRECINCT, INVITED_BY, PURPOSE_OF_ENTRY, SKIN_COLOR, COMPLEXION, AIRPORT_FROM, AIRPORT_TO, AIRLINE_NAME, AIRLINE_NAME_FREQUENT_FLYER, LICENSE_NUMBER, IN_TANKS, EXCEPT_IN_TANKS, FAST_TRACK, OWNER, MRZ_STRINGS_ICAO_RFID, NUMBER_OF_CARD_ISSUANCE, NUMBER_OF_CARD_ISSUANCE_CHECKSUM, NUMBER_OF_CARD_ISSUANCE_CHECK_DIGIT, CENTURY_DATE_OF_BIRTH, DL_CLASS_CODE_A3_FROM, DL_CLASS_CODE_A3_TO, DL_CLASS_CODE_A3_NOTES, DL_CLASS_CODE_C2_FROM, DL_CLASS_CODE_C2_TO, DL_CLASS_CODE_C2_NOTES, DL_CLASS_CODE_B2_FROM, DL_CLASS_CODE_B2_TO, DL_CLASS_CODE_B2_NOTES, DL_CLASS_CODE_D2_FROM, DL_CLASS_CODE_D2_TO, DL_CLASS_CODE_D2_NOTES, DL_CLASS_CODE_B2E_FROM, DL_CLASS_CODE_B2E_TO, DL_CLASS_CODE_B2E_NOTES, DL_CLASS_CODE_G_FROM, DL_CLASS_CODE_G_TO, DL_CLASS_CODE_G_NOTES, DL_CLASS_CODE_J_FROM, DL_CLASS_CODE_J_TO, DL_CLASS_CODE_J_NOTES, DL_CLASS_CODE_LC_FROM, DL_CLASS_CODE_LC_TO, DL_CLASS_CODE_LC_NOTES, BANK_CARD_NUMBER, BANK_CARD_VALID_THRU, TAX_NUMBER, HEALTH_NUMBER, GRANDFATHER_NAME, SELECTEE_INDICATOR, MOTHER_SURNAME, MOTHER_GIVEN_NAME, FATHER_SURNAME, FATHER_GIVEN_NAME, MOTHER_DATE_OF_BIRTH, FATHER_DATE_OF_BIRTH, MOTHER_PERSONAL_NUMBER, FATHER_PERSONAL_NUMBER, MOTHER_PLACE_OF_BIRTH, FATHER_PLACE_OF_BIRTH, MOTHER_COUNTRY_OF_BIRTH, FATHER_COUNTRY_OF_BIRTH, DATE_FIRST_RENEWAL, DATE_SECOND_RENEWAL, PLACE_OF_EXAMINATION, APPLICATION_NUMBER, VOUCHER_NUMBER, AUTHORIZATION_NUMBER, FACULTY, FORM_OF_EDUCATION, DNI_NUMBER, RETIREMENT_NUMBER, PROFESSIONAL_ID_NUMBER, AGE_AT_ISSUE, YEARS_SINCE_ISSUE, DL_CLASS_CODE_BTP_FROM, DL_CLASS_CODE_BTP_NOTES, DL_CLASS_CODE_BTP_TO, DL_CLASS_CODE_C3_FROM, DL_CLASS_CODE_C3_NOTES, DL_CLASS_CODE_C3_TO, DL_CLASS_CODE_E_FROM, DL_CLASS_CODE_E_NOTES, DL_CLASS_CODE_E_TO, DL_CLASS_CODE_F_FROM, DL_CLASS_CODE_F_NOTES, DL_CLASS_CODE_F_TO, DL_CLASS_CODE_FA_FROM, DL_CLASS_CODE_FA_NOTES, DL_CLASS_CODE_FA_TO, DL_CLASS_CODE_FA1_FROM, DL_CLASS_CODE_FA1_NOTES, DL_CLASS_CODE_FA1_TO, DL_CLASS_CODE_FB_FROM, DL_CLASS_CODE_FB_NOTES, DL_CLASS_CODE_FB_TO, DL_CLASS_CODE_G1_FROM, DL_CLASS_CODE_G1_NOTES, DL_CLASS_CODE_G1_TO, DL_CLASS_CODE_H_FROM, DL_CLASS_CODE_H_NOTES, DL_CLASS_CODE_H_TO, DL_CLASS_CODE_I_FROM, DL_CLASS_CODE_I_NOTES, DL_CLASS_CODE_I_TO, DL_CLASS_CODE_K_FROM, DL_CLASS_CODE_K_NOTES, DL_CLASS_CODE_K_TO, DL_CLASS_CODE_LK_FROM, DL_CLASS_CODE_LK_NOTES, DL_CLASS_CODE_LK_TO, DL_CLASS_CODE_N_FROM, DL_CLASS_CODE_N_NOTES, DL_CLASS_CODE_N_TO, DL_CLASS_CODE_S_FROM, DL_CLASS_CODE_S_NOTES, DL_CLASS_CODE_S_TO, DL_CLASS_CODE_TB_FROM, DL_CLASS_CODE_TB_NOTES, DL_CLASS_CODE_TB_TO, DL_CLASS_CODE_TM_FROM, DL_CLASS_CODE_TM_NOTES, DL_CLASS_CODE_TM_TO, DL_CLASS_CODE_TR_FROM, DL_CLASS_CODE_TR_NOTES, DL_CLASS_CODE_TR_TO, DL_CLASS_CODE_TV_FROM, DL_CLASS_CODE_TV_NOTES, DL_CLASS_CODE_TV_TO, DL_CLASS_CODE_V_FROM, DL_CLASS_CODE_V_NOTES, DL_CLASS_CODE_V_TO, DL_CLASS_CODE_W_FROM, DL_CLASS_CODE_W_NOTES, DL_CLASS_CODE_W_TO, URL, CALIBER, MODEL, MAKE, NUMBER_OF_CYLINDERS, SURNAME_OF_HUSBAND_AFTER_REGISTRATION, SURNAME_OF_WIFE_AFTER_REGISTRATION, DATE_OF_BIRTH_OF_WIFE, DATE_OF_BIRTH_OF_HUSBAND, CITIZENSHIP_OF_FIRST_PERSON, CITIZENSHIP_OF_SECOND_PERSON, CVV, DATE_OF_INSURANCE_EXPIRY, MORTGAGE_BY, OLD_DOCUMENT_NUMBER, OLD_DATE_OF_ISSUE, OLD_PLACE_OF_ISSUE, DL_CLASS_CODE_LR_FROM, DL_CLASS_CODE_LR_TO, DL_CLASS_CODE_LR_NOTES, DL_CLASS_CODE_MR_FROM, DL_CLASS_CODE_MR_TO, DL_CLASS_CODE_MR_NOTES, DL_CLASS_CODE_HR_FROM, DL_CLASS_CODE_HR_TO, DL_CLASS_CODE_HR_NOTES, DL_CLASS_CODE_HC_FROM, DL_CLASS_CODE_HC_TO, DL_CLASS_CODE_HC_NOTES, DL_CLASS_CODE_MC_FROM, DL_CLASS_CODE_MC_TO, DL_CLASS_CODE_MC_NOTES, DL_CLASS_CODE_RE_FROM, DL_CLASS_CODE_RE_TO, DL_CLASS_CODE_RE_NOTES, DL_CLASS_CODE_R_FROM, DL_CLASS_CODE_R_TO, DL_CLASS_CODE_R_NOTES, DL_CLASS_CODE_CA_FROM, DL_CLASS_CODE_CA_TO, DL_CLASS_CODE_CA_NOTES, CITIZENSHIP_STATUS, MILITARY_SERVICE_FROM, MILITARY_SERVICE_TO, DL_CLASS_CODE_NT_FROM, DL_CLASS_CODE_NT_TO, DL_CLASS_CODE_NT_NOTES, DL_CLASS_CODE_TN_FROM, DL_CLASS_CODE_TN_TO, DL_CLASS_CODE_TN_NOTES, DL_CLASS_CODE_D3_FROM, DL_CLASS_CODE_D3_TO, DL_CLASS_CODE_D3_NOTES, ALT_DATE_OF_EXPIRY, DL_CLASS_CODE_CD_FROM, DL_CLASS_CODE_CD_TO, DL_CLASS_CODE_CD_NOTES, ISSUER_IDENTIFICATION_NUMBER, PAYMENT_PERIOD_FROM, PAYMENT_PERIOD_TO, VACCINATION_CERTIFICATE_IDENTIFIER, FIRST_NAME, DATE_OF_ARRIVAL, SECOND_NAME, THIRD_NAME, FOURTH_NAME, LAST_NAME, DL_CLASS_CODE_RM_FROM, DL_CLASS_CODE_RM_NOTES, DL_CLASS_CODE_RM_TO, DL_CLASS_CODE_PW_FROM, DL_CLASS_CODE_PW_NOTES, DL_CLASS_CODE_PW_TO, DL_CLASS_CODE_EB_FROM, DL_CLASS_CODE_EB_NOTES, DL_CLASS_CODE_EB_TO, DL_CLASS_CODE_EC_FROM, DL_CLASS_CODE_EC_NOTES, DL_CLASS_CODE_EC_TO, DL_CLASS_CODE_EC1_FROM, DL_CLASS_CODE_EC1_NOTES, DL_CLASS_CODE_EC1_TO, PLACE_OF_BIRTH_CITY, YEAR_OF_BIRTH, YEAR_OF_EXPIRY, GRANDFATHER_NAME_MATERNAL, FIRST_SURNAME, MONTH_OF_BIRTH, ADDRESS_FLOOR_NUMBER, ADDRESS_ENTRANCE, ADDRESS_BLOCK_NUMBER, ADDRESS_STREET_NUMBER, ADDRESS_STREET_TYPE, ADDRESS_CITY_SECTOR, ADDRESS_COUNTY_TYPE, ADDRESS_CITY_TYPE, ADDRESS_BUILDING_TYPE, DATE_OF_RETIREMENT, DOCUMENT_STATUS, SIGNATURE, FT_UNIQUE_CERTIFICATE_IDENTIFIER, FT_EMAIL, FT_DATE_OF_SPECIMEN_COLLECTION, FT_TYPE_OF_TESTING, FT_RESULT_OF_TESTING, FT_METHOD_OF_TESTING, FT_DIGITAL_TRAVEL_AUTHORIZATION_NUMBER, FT_DATE_OF_FIRST_POSITIVE_TEST_RESULT, EF_CARD_ACCESS, SHORT_FLIGHT_NUMBER, AIRLINE_CODE]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """TextFieldType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, TextFieldType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextFieldType):
            return True

        return self.to_dict() != other.to_dict()
