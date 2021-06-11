import logging

from aiohttp.web import Application
from aiohttp_apispec import setup_aiohttp_apispec

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from application.middlewares.exception_handler import (
    error_middleware,
    workers_middleware,
)
from application.routes import setup_routes
from application.worker import worker

import asyncio


def setup_application(pg_url: str = None) -> Application:
    app = Application()
    # setup_postgres(app, pg_url=pg_url)
    setup_routes(app)
    setup_logging(app)
    setup_middlewares(app)
    setup_external_libraries(app)
    setup_workers(app)
    return app


def setup_logging(application: Application) -> None:
    logging.basicConfig(level=logging.DEBUG)
    application.logger = logging.getLogger(__name__)


def setup_middlewares(application: Application) -> None:
    application.middlewares.append(error_middleware)
    application.middlewares.append(workers_middleware)


def setup_external_libraries(application: Application) -> None:
    setup_aiohttp_apispec(
        app=application,
        title="Documentation",
        version="v1",
        url="/swagger.json",
        swagger_path="/swagger",
    )


def setup_postgres(application: Application, pg_url: str = None) -> None:
    # its my template
    engine = create_engine(pg_url)
    application["db"] = engine
    application["session"] = sessionmaker(bind=engine)


def setup_workers(application: Application):
    loop = asyncio.get_event_loop()
    application["queue_worker"] = asyncio.Queue()
    application["queue_timeout"] = asyncio.Queue()
    application["result_worker"] = []
    application["not_done_tasks"] = []
    application["listen"] = loop.create_task(worker(application))
