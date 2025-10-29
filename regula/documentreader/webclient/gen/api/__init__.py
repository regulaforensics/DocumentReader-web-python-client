# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from regula.documentreader.webclient.gen.api.healthcheck_api import HealthcheckApi
    from regula.documentreader.webclient.gen.api.process_api import ProcessApi
    from regula.documentreader.webclient.gen.api.resources_api import ResourcesApi
    from regula.documentreader.webclient.gen.api.transaction_api import TransactionApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from regula.documentreader.webclient.gen.api.healthcheck_api import HealthcheckApi
from regula.documentreader.webclient.gen.api.process_api import ProcessApi
from regula.documentreader.webclient.gen.api.resources_api import ResourcesApi
from regula.documentreader.webclient.gen.api.transaction_api import TransactionApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
