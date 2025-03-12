# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ParsingNotificationCodes(int, Enum):
    """
    The enumeration contains possible values of notification codes returned during the RFID chip processing.
    """

    """
    allowed enum values
    """
    ntfLDS_ASN_Certificate_IncorrectVersion = 2415919105
    ntfLDS_ASN_Certificate_NonMatchingSignatureAlgorithm = 2415919106
    ntfLDS_ASN_Certificate_IncorrectTimeCoding = 2415919107
    ntfLDS_ASN_Certificate_IncorrectUseOfGeneralizedTime = 2415919108
    ntfLDS_ASN_Certificate_EmptyIssuer = 2415919109
    ntfLDS_ASN_Certificate_EmptySubject = 2415919110
    ntfLDS_ASN_Certificate_UnsupportedCriticalExtension = 2415919112
    ntfLDS_ASN_Certificate_ForcedDefaultCSCARole = 2415919118
    ntfLDS_ASN_Certificate_ForcedDefaultDSRole = 2415919119
    ntfLDS_ASN_Certificate_IncorrectIssuerSubjectDS = 2415919120
    ntfLDS_ASN_Certificate_DuplicatingExtensions = 2415919127
    ntfLDS_ICAO_Certificate_Version_Missed = 2415919616
    ntfLDS_ICAO_Certificate_Version_Incorrect = 2415919617
    ntfLDS_ICAO_Certificate_Issuer_Country_Missed = 2415919618
    ntfLDS_ICAO_Certificate_Issuer_CommonName_Missed = 2415919619
    ntfLDS_ICAO_Certificate_Issuer_CountryNonCompliant = 2415919620
    ntfLDS_ICAO_Certificate_Subject_Country_Missed = 2415919621
    ntfLDS_ICAO_Certificate_Subject_CommonName_Missed = 2415919622
    ntfLDS_ICAO_Certificate_Subject_CountryNonCompliant = 2415919623
    ntfLDS_ICAO_Certificate_UsingNonCompliantData = 2415919624
    ntfLDS_ICAO_Certificate_UnsupportedSignatureAlgorithm = 2415919625
    ntfLDS_ICAO_Certificate_UnsupportedPublicKeyAlgorithm = 2415919626
    ntfLDS_ICAO_Certificate_MissedExtensions = 2415919627
    ntfLDS_ICAO_Certificate_Validity = 2415919628
    ntfLDS_ICAO_Certificate_Ext_UsingNonCompliantData = 2415919629
    ntfLDS_ICAO_Certificate_Ext_KeyUsage_Missed = 2415919630
    ntfLDS_ICAO_Certificate_Ext_KeyUsage_NotCritical = 2415919631
    ntfLDS_ICAO_Certificate_Ext_KeyUsage_IncorrectData = 2415919632
    ntfLDS_ICAO_Certificate_Ext_BasicC_Missed = 2415919633
    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage1 = 2415919634
    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage2 = 2415919635
    ntfLDS_ICAO_Certificate_Ext_BasicC_NotCritical = 2415919636
    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectData = 2415919637
    ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Missed = 2415919638
    ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Incorrect = 2415919639
    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_NotCritical = 2415919640
    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectUsage = 2415919641
    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectData = 2415919642
    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_Missed = 2415919643
    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_IncorrectData = 2415919644
    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_KeyID_Missed = 2415919645
    ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_Missed = 2415919646
    ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_IncorrectData = 2415919647
    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Missed = 2415919648
    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_IncorrectData = 2415919649
    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Empty = 2415919650
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Missed = 2415919651
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_IncorrectData = 2415919652
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Empty = 2415919653
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_NonCompliant = 2415919654
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Critical = 2415919656
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Empty = 2415919657
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Incorrect = 2415919658
    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_NonCompliant = 2415919659
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Missed = 2415919660
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_IncorrectData = 2415919661
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Empty = 2415919662
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_NonCompliant = 2415919663
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Critical = 2415919665
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Empty = 2415919666
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Incorrect = 2415919667
    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_NonCompliant = 2415919668
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Missed = 2415919669
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_IncorrectData = 2415919670
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Version = 2415919671
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes = 2415919672
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes_Empty = 2415919673
    ntfLDS_ICAO_Certificate_Ext_CertPolicies_IncorrectData = 2415919674
    ntfLDS_ICAO_Certificate_Ext_CertPolicies_Empty = 2415919675
    ntfLDS_ICAO_Certificate_Ext_CertPolicies_PolicyID_Missed = 2415919676
    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Missed = 2415919677
    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_IncorrectData = 2415919678
    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Empty = 2415919679
    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_PointMissed = 2415919680
    ntfLDS_ICAO_Certificate_SN_NonCompliant = 2415919681
    ntfLDS_ICAO_Certificate_Issuer_SN_NonCompliant = 2415919682
    ntfLDS_ICAO_Certificate_Subject_SN_NonCompliant = 2415919683
    ntfLDS_ICAO_Certificate_Issuer_AttributeNonCompliant = 2415919684
    ntfLDS_ICAO_Certificate_Subject_AttributeNonCompliant = 2415919685
    ntfLDS_ICAO_Certificate_IssuerSubject_Country_NonMatching = 2415919686
    ntfLDS_ICAO_Certificate_Ext_CSCA_AltNames_NonMatching = 2415919687
    ntfLDS_ICAO_Certificate_Ext_NameChange_IncorrectData = 2415919688
    ntfLDS_ICAO_Certificate_Ext_NameChange_NonCompliant = 2415919689
    ntfLDS_ICAO_Certificate_Ext_NameChange_Critical = 2415919690
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_NonCompliant = 2415919691
    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Critical = 2415919692
    ntfLDS_ICAO_Certificate_Ext_Optional_Critical = 2415919693
    ntfLDS_ICAO_Certificate_Subject_NonCompliant = 2415919694
    ntfLDS_ICAO_Certificate_Subject_CommonNameNonCompliant = 2415919695
    ntfLDS_ICAO_COM_LDS_Version_Incorrect = 2415919136
    ntfLDS_ICAO_COM_LDS_Version_Missing = 2415919137
    ntfLDS_ICAO_COM_Unicode_Version_Incorrect = 2415919138
    ntfLDS_ICAO_COM_Unicode_Version_Missing = 2415919139
    ntfLDS_ICAO_COM_DGPM_Incorrect = 2415919140
    ntfLDS_ICAO_COM_DGPM_Missing = 2415919141
    ntfLDS_ICAO_COM_DGPM_Unexpected = 2415919142
    ntfLDS_ICAO_Application_LDSVersion_Unsupported = 2415919152
    ntfLDS_ICAO_Application_UnicodeVersion_Unsupported = 2415919153
    ntfLDS_ICAO_Application_LDSVersion_Inconsistent = 2415919154
    ntfLDS_ICAO_Application_UnicodeVersion_Inconsistent = 2415919155
    ntfLDS_ASN_SignedData_OID_Incorrect = 2415919360
    ntfLDS_ASN_SignedData_Version_Incorrect = 2415919520
    ntfLDS_ASN_SignedData_ContentOID_Incorrect = 2415919521
    ntfLDS_ICAO_SignedData_Version_Incorrect = 2415919361
    ntfLDS_ICAO_SignedData_DigestAlgorithms_Empty = 2415919362
    ntfLDS_ICAO_SignedData_DigestAlgorithms_Unsupported = 2415919363
    ntfLDS_ICAO_SignedData_SignerInfos_MultipleEntries = 2415919369
    ntfLDS_ICAO_SignedData_Certificates_Missed = 2415919536
    ntfLDS_ICAO_SignedData_Certificates_Empty = 2415919537
    ntfLDS_ICAO_SignedData_CRLs_IncorrectUsage = 2415919538
    ntfLDS_ICAO_LDSObject_IncorrectContentOID = 2415919364
    ntfLDS_ICAO_LDSObject_DGNumber_Incorrect = 2415919365
    ntfLDS_ICAO_LDSObject_DGHash_Missing = 2415919366
    ntfLDS_ICAO_LDSObject_DGHash_Extra = 2415919367
    ntfLDS_ICAO_LDSObject_Version_Incorrect = 2415919368
    ntfLDS_ICAO_MasterList_Version_Incorrect = 2415919552
    ntfLDS_ICAO_DeviationList_Version_Incorrect = 2415919560
    ntfLDS_BSI_DefectList_Version_Incorrect = 2415919568
    ntfLDS_BSI_BlackList_Version_Incorrect = 2415919576
    ntfLDS_ASN_SignerInfo_Version_Incorrect = 2415919370
    ntfLDS_ASN_SignerInfo_SID_IncorrectChoice = 2415919371
    ntfLDS_ASN_SignerInfo_SID_DigestAlgorithmNotListed = 2415919372
    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Missing = 2415919373
    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Data = 2415919374
    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Value = 2415919375
    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Missing = 2415919376
    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Data = 2415919377
    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Value = 2415919378
    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Missing = 2415919387
    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Data = 2415919388
    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Value = 2415919389
    ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Missing = 2415919390
    ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Data = 2415919391
    ntfLDS_Auth_SignerInfo_Certificate_Validity = 2415919381
    ntfLDS_Auth_SignerInfo_Certificate_RootIsNotTrusted = 2415919382
    ntfLDS_Auth_SignerInfo_Certificate_CantFindCSCA = 2415919383
    ntfLDS_Auth_SignerInfo_Certificate_Revoked = 2415919384
    ntfLDS_Auth_SignerInfo_Certificate_SignatureInvalid = 2415919385
    ntfLDS_UnsupportedImageFormat = 2415919386
    ntfLDS_MRZ_DocumentType_Unknown = 139272
    ntfLDS_MRZ_IssuingState_SyntaxError = 139273
    ntfLDS_MRZ_Name_IsVoid = 139274
    ntfLDS_MRZ_Number_IncorrectChecksum = 139277
    ntfLDS_MRZ_Nationality_SyntaxError = 139278
    ntfLDS_MRZ_DOB_SyntaxError = 139279
    ntfLDS_MRZ_DOB_Error = 139280
    ntfLDS_MRZ_DOB_IncorrectChecksum = 139281
    ntfLDS_MRZ_Sex_Incorrect = 139282
    ntfLDS_MRZ_DOE_SyntaxError = 139283
    ntfLDS_MRZ_DOE_Error = 139284
    ntfLDS_MRZ_DOE_IncorrectChecksum = 139285
    ntfLDS_MRZ_OptionalData_IncorrectChecksum = 139286
    ntfLDS_MRZ_IncorrectChecksum = 139287
    ntfLDS_MRZ_Incorrect = 139288
    ntfLDS_Biometrics_FormatOwner_Missing = 2415984640
    ntfLDS_Biometrics_FormatOwner_Incorrect = 2416050176
    ntfLDS_Biometrics_FormatType_Missing = 2416115712
    ntfLDS_Biometrics_FormatType_Incorrect = 2416181248
    ntfLDS_Biometrics_Type_Incorrect = 2416246784
    ntfLDS_Biometrics_SubType_Missing = 2416312320
    ntfLDS_Biometrics_SubType_Incorrect = 2416377856
    ntfLDS_Biometrics_BDB_Image_Missing = 2416443392
    ntfLDS_Biometrics_BDB_FormatID_Incorrect = 2416508928
    ntfLDS_Biometrics_BDB_Version_Incorrect = 2416574464
    ntfLDS_Biometrics_BDB_DataLength_Incorrect = 2416640000
    ntfLDS_Biometrics_BDB_Data_Gender = 2416967680
    ntfLDS_Biometrics_BDB_Data_EyeColor = 2417033216
    ntfLDS_Biometrics_BDB_Data_HairColor = 2417098752
    ntfLDS_Biometrics_BDB_Data_PoseAngle_Yaw = 2417164288
    ntfLDS_Biometrics_BDB_Data_PoseAngle_Pitch = 2417229824
    ntfLDS_Biometrics_BDB_Data_PoseAngle_Roll = 2417295360
    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Yaw = 2417360896
    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Pitch = 2417426432
    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Roll = 2417491968
    ntfLDS_Biometrics_BDB_Data_FaceImageType = 2417557504
    ntfLDS_Biometrics_BDB_Data_ImageDataType = 2417623040
    ntfLDS_SI_PACE_Info_UnsupportedStdParameters = 2432696320
    ntfLDS_SI_PACE_Info_DeprecatedVersion = 2432696321
    ntfLDS_SI_PACE_DomainParams_UsingStdRef = 2432696322
    ntfLDS_SI_PACE_DomainParams_UnsupportedAlgorithm = 2432696323
    ntfLDS_SI_CA_Info_IncorrectVersion = 2432696324
    ntfLDS_SI_CA_PublicKey_UnsupportedAlgorithm = 2432696325
    ntfLDS_SI_CA_DomainParams_UnsupportedAlgorithm = 2432696326
    ntfLDS_SI_TA_Info_IncorrectVersion = 2432696327
    ntfLDS_SI_TA_Info_FileIDForVersion2 = 2432696328
    ntfLDS_SI_eIDSecurity_UnsupportedDigestAlgorithm = 2432696329
    ntfLDS_SI_RI_Info_IncorrectVersion = 2432696330
    ntfLDS_SI_RI_DomainParams_UnsupportedAlgorithm = 2432696331
    ntfLDS_SI_AA_Info_IncorrectVersion = 2432696332
    ntfLDS_SI_AA_Info_UnsupportedAlgorithm = 2432696333
    ntfLDS_SI_AA_Info_InconsistentAlgorithmReference = 2432696334
    ntfLDS_SI_Storage_PACE_Info_NotAvailable = 2432696576
    ntfLDS_SI_Storage_PACE_Info_NoStdParameters = 2432696577
    ntfLDS_SI_Storage_PACE_Info_NoMatchingDomainParams = 2432696578
    ntfLDS_SI_Storage_CA_Info_NotAvailable = 2432696579
    ntfLDS_SI_Storage_CA_DomainParams_NoRequiredOption = 2432696580
    ntfLDS_SI_Storage_CA_DomainParams_NotAvailable = 2432696581
    ntfLDS_SI_Storage_CA_AnonymousInfos = 2432696582
    ntfLDS_SI_Storage_CA_Info_NoMatchingDomainParams = 2432696583
    ntfLDS_SI_Storage_CA_Info_NoMatchingPublicKey = 2432696584
    ntfLDS_SI_Storage_CA_IncorrectInfosQuantity = 2432696585
    ntfLDS_SI_Storage_TA_Info_NotAvailable = 2432696586
    ntfLDS_SI_Storage_CardInfoLocator_MultipleEntries = 2432696587
    ntfLDS_SI_Storage_eIDSecurityInfo_MultipleEntries = 2432696588
    ntfLDS_SI_Storage_PrivilegedTI_MultipleEntries = 2432696589
    ntfLDS_SI_Storage_PrivilegedTI_IncorrectUsage = 2432696590
    ntfLDS_SI_Storage_RI_DomainParams_MultipleEntries = 2432696591
    ntfLDS_SI_Storage_PACEInfos_NonConsistant = 2432696592
    ntfLDS_CVCertificate_Profile_IncorrectVersion = 2432696833
    ntfLDS_CVCertificate_Validity = 2432696834
    ntfLDS_CVCertificate_NonCVCADomainParameters = 2432696835
    ntfLDS_CV_Certificate_PrivateKey_IncorrectVersion = 2432696836
    ntfLDS_TA_PACEStaticBindingUsed = 2432697088
    ntfLDS_Auth_MLSignerInfo_Certificate_Validity = 2449473813
    ntfLDS_Auth_MLSignerInfo_Certificate_RootIsNotTrusted = 2449473814
    ntfLDS_Auth_MLSignerInfo_Certificate_CantFindCSCA = 2449473815
    ntfLDS_Auth_MLSignerInfo_Certificate_Revoked = 2449473816
    ntfLDS_Auth_MLSignerInfo_Certificate_SignatureInvalid = 2449473817
    ntfLDS_ICAO_Certificate_Chain_Country_NonMatching = 2415919696
    ntfLDS_ICAO_Certificate_VisualMrz_Country_NonMatching = 2415919697
    ntfLDS_MRZ_CountryCode_VisualMrz_NonMatching = 139289
    ntfLDS_ICAO_Certificate_MRZ_Country_NonMatching = 2415919698

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ParsingNotificationCodes from a JSON string"""
        return cls(json.loads(json_str))


