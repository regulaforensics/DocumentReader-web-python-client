#!/bin/sh

DOCS_DEFINITION_FOLDER="${PWD}/../DocumentReader-web-openapi" \
\
&& docker run --user "$(id -u):$(id -g)" --rm -v "${PWD}:/client" -v "$DOCS_DEFINITION_FOLDER:/definitions" \
openapitools/openapi-generator-cli:v5.0.0 generate -g python-legacy \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates \
--type-mappings AnyOfDocVisualExtendedFieldRectDocVisualExtendedFieldRfid=DocVisualExtendedField \
--type-mappings AnyOfSecurityFeatureResultIdentResultFiberResultOCRSecurityTextResultPhotoIdentResult=AuthenticityCheckResultItem \
--type-mappings  AnyOfGraphicFieldRectGraphicFieldRfid=GraphicField \
--type-mappings AnyOfStatusResultTextResultDocumentImageResultImagesResultChosenDocumentTypeResultDocumentTypesCandidatesResultTextDataResultGraphicsResultLexicalAnalysisResultAuthenticityResultImageQualityResultDocumentPositionResultDocBarCodeInfoLicenseResultEncryptedRCLResultDocumentBinaryInfoResult=ResultItem \
--type-mappings AnyOfStatusResultTextResultDocumentImageResultImagesResultChosenDocumentTypeResultDocumentTypesCandidatesResultTextDataResultGraphicsResultLexicalAnalysisResultAuthenticityResultImageQualityResultDocumentPositionResultDocBarCodeInfoLicenseResultEncryptedRCLResult=ResultItem \
--type-mappings AnyOfStatusResultTextResultDocumentImageResultImagesResultChosenDocumentTypeResultDocumentTypesCandidatesResultTextDataResultGraphicsResultLexicalAnalysisResultAuthenticityResultImageQualityResultDocumentPositionResultDocBarCodeInfoLicenseResultEncryptedRCLResultByteArrayResult=ResultItem
