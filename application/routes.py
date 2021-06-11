import logging

from aiohttp.web import Application
from application.views import add_task, get_queue_work, get_result

logger = logging.getLogger(__name__)


def setup_routes(app: Application):
    app.router.add_get("/get_queue_work", handler=get_queue_work)
    app.router.add_get("/get_result", handler=get_result)
    app.router.add_post("/add_task", handler=add_task)
