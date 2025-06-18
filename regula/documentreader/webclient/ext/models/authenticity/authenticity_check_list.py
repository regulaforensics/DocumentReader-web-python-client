from typing import Optional

from regula.documentreader.webclient.gen.models import AuthenticityCheckList as GenAuthenticityCheckList
from regula.documentreader.webclient.gen.models import AuthenticityResultType, AuthenticityCheckResult
from regula.documentreader.webclient.ext.models.authenticity.fiber import FiberChecks
from regula.documentreader.webclient.ext.models.authenticity.ident import IdentChecks
from regula.documentreader.webclient.ext.models.authenticity.image_ident import ImageIdentChecks
from regula.documentreader.webclient.ext.models.authenticity.ocr_security_text import OCRSecurityTextChecks
from regula.documentreader.webclient.ext.models.authenticity.security_feature import SecurityFeatureChecks


class AuthenticityCheckList(GenAuthenticityCheckList):

    @property
    def uv_luminescence_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.UV_LUMINESCENCE)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def ir_b900_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.IR_B900)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def image_pattern_checks(self) -> Optional[IdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.IMAGE_PATTERN)
        if result:
            return IdentChecks.from_json(result.to_json())
        return None

    @property
    def axial_protection_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.AXIAL_PROTECTION)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def uv_fiber_checks(self) -> Optional[FiberChecks]:
        result = self.__result_by_type(AuthenticityResultType.UV_FIBERS)
        if result:
            return FiberChecks.from_json(result.to_json())
        return None

    @property
    def ir_visibility_checks(self) -> Optional[IdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.IR_VISIBILITY)
        if result:
            return IdentChecks.from_json(result.to_json())
        return None

    @property
    def ocr_security_text_checks(self) -> Optional[OCRSecurityTextChecks]:
        result = self.__result_by_type(AuthenticityResultType.OCR_SECURITY_TEXT)
        if result:
            return OCRSecurityTextChecks.from_json(result.to_json())
        return None

    @property
    def ipi_checks(self) -> Optional[ImageIdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.IPI)
        if result:
            return ImageIdentChecks.from_json(result.to_json())
        return None

    @property
    def embed_image_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.PHOTO_EMBED_TYPE)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def holograms_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.HOLOGRAMS)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def photo_area_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.PHOTO_AREA)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def portrait_comparison_checks(self) -> Optional[IdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.PORTRAIT_COMPARISON)
        if result:
            return IdentChecks.from_json(result.to_json())
        return None

    @property
    def barcode_format_checks(self) -> Optional[SecurityFeatureChecks]:
        result = self.__result_by_type(AuthenticityResultType.BARCODE_FORMAT_CHECK)
        if result:
            return SecurityFeatureChecks.from_json(result.to_json())
        return None

    @property
    def kinegram_checks(self) -> Optional[IdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.KINEGRAM)
        if result:
            return IdentChecks.from_json(result.to_json())
        return None

    @property
    def letter_screen_checks(self) -> Optional[IdentChecks]:
        result = self.__result_by_type(AuthenticityResultType.LETTER_SCREEN)
        if result:
            return IdentChecks.from_json(result.to_json())
        return None

    def __result_by_type(self, authenticity_type: int) -> Optional[AuthenticityCheckResult]:
        for result in self.list:
            if result.type == authenticity_type:
                return result
        return None
