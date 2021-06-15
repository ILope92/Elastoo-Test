from aiohttp import web
from aiohttp_apispec import docs, request_schema, response_schema

from application.models.requests_schemas import POST
from application.models.response_schemas import ResultQueueWorkSchema, ResultSchema
from application.worker import ListTasks


@docs(
    tags=["GET a list of completed tasks"],
    summary="Post method summary",
    description="Post method description",
    responses={
        "405": {"description": "Invalid input"},
        "422": {"description": "error in json"},
        "404": {"description": "Validate err"},
        "200": {"description": "Successfull"},
    },
)
@response_schema(ResultSchema())
async def get_result(request: web.Request):
    return web.json_response(ListTasks.get_done_tasks())


@docs(
    tags=["GET a list of outstanding tasks"],
    summary="Post method summary",
    description="Post method description",
    responses={
        "405": {"description": "Invalid input"},
        "422": {"description": "error in json"},
        "404": {"description": "Validate err"},
        "200": {"description": "Successfull"},
    },
)
@response_schema(ResultQueueWorkSchema())
async def get_queue_work(request: web.Request):
    return web.json_response(ListTasks.get_not_done_tasks())


@docs(
    tags=["POST: Submit a task"],
    summary="Post method summary",
    description="Post method description",
    responses={
        "405": {"description": "Invalid input"},
        "422": {"description": "error in json"},
        "404": {"description": "Validate err"},
        "200": {"description": "Successfull"},
    },
)
@request_schema(POST())
async def add_task(request: web.Request):
    answer = await request.json()
    queue_work = request.app["queue_worker"]
    queue_timeout = request.app["queue_timeout"]
    await queue_work.put(item=answer["num"])
    await queue_timeout.put(item=answer["timeout"])
    return web.json_response(text="ok")
