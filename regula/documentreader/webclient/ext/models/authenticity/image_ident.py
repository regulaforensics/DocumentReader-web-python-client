from typing import List

from regula.documentreader.webclient import gen


class ImageIdentChecks(gen.AuthenticityCheckResult):
    @gen.AuthenticityCheckResult.list.getter
    def list(self) -> List[gen.PhotoIdentResult]:
        # noinspection PyTypeChecker
        return super().list
