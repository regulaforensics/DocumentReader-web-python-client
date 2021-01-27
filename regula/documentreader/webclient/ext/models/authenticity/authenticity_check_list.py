from typing import Optional

from regula.documentreader.webclient import gen, AuthenticityResultType
from regula.documentreader.webclient.ext.models.authenticity.fiber import FiberChecks
from regula.documentreader.webclient.ext.models.authenticity.ident import IdentChecks
from regula.documentreader.webclient.ext.models.authenticity.image_ident import ImageIdentChecks
from regula.documentreader.webclient.ext.models.authenticity.ocr_security_text import OCRSecurityTextChecks
from regula.documentreader.webclient.ext.models.authenticity.security_feature import SecurityFeatureChecks


class AuthenticityCheckList(gen.AuthenticityCheckList):

    @property
    def uv_luminescence_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.UV_LUMINESCENCE, SecurityFeatureChecks)

    @property
    def ir_b900_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.IR_B900, SecurityFeatureChecks)

    @property
    def image_pattern_checks(self) -> Optional[IdentChecks]:
        return self.__result_by_type(AuthenticityResultType.IMAGE_PATTERN, IdentChecks)

    @property
    def axial_protection_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.AXIAL_PROTECTION, SecurityFeatureChecks)

    @property
    def uv_fiber_checks(self) -> Optional[FiberChecks]:
        return self.__result_by_type(AuthenticityResultType.UV_FIBERS, FiberChecks)

    @property
    def ir_visibility_checks(self) -> Optional[IdentChecks]:
        return self.__result_by_type(AuthenticityResultType.IR_VISIBILITY, IdentChecks)

    @property
    def ocr_security_text_checks(self) -> Optional[OCRSecurityTextChecks]:
        return self.__result_by_type(AuthenticityResultType.OCR_SECURITY_TEXT, OCRSecurityTextChecks)

    @property
    def ipi_checks(self) -> Optional[ImageIdentChecks]:
        return self.__result_by_type(AuthenticityResultType.IPI, ImageIdentChecks)

    @property
    def embed_image_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.PHOTO_EMBED_TYPE, SecurityFeatureChecks)

    @property
    def holograms_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.HOLOGRAMS, SecurityFeatureChecks)

    @property
    def photo_area_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.PHOTO_AREA, SecurityFeatureChecks)

    @property
    def portrait_comparison_checks(self) -> Optional[IdentChecks]:
        return self.__result_by_type(AuthenticityResultType.PORTRAIT_COMPARISON, IdentChecks)

    @property
    def barcode_format_checks(self) -> Optional[SecurityFeatureChecks]:
        return self.__result_by_type(AuthenticityResultType.BARCODE_FORMAT_CHECK, SecurityFeatureChecks)

    @property
    def kinegram_checks(self) -> Optional[IdentChecks]:
        return self.__result_by_type(AuthenticityResultType.KINEGRAM, IdentChecks)

    @property
    def letter_screen_checks(self) -> Optional[IdentChecks]:
        return self.__result_by_type(AuthenticityResultType.LETTER_SCREEN, IdentChecks)

    def __result_by_type(self, authenticity_type: int, parent_class: type) -> Optional[gen.AuthenticityCheckResult]:
        for result in self.list:
            if result.type == authenticity_type:
                result.__class__ = parent_class
                return result
        return None
