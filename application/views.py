from aiohttp import web
from aiohttp_apispec import docs, request_schema, response_schema

from application.models.requests_schemas import POST
from application.models.response_schemas import ResultQueueWorkSchema, ResultSchema
from application.models.worker_model import Worker


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
    # queue = request.app["queue_worker"]
    return web.json_response({"result": Worker.result_worker})


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
    response = {
        f"task_{Worker.list_id[num]}": {
            "date_created": Worker.date_create[num],
            "num": Worker.not_done_tasks[num],
            "timeout": Worker.timeout[num],
        }
        for num in range(len(Worker.not_done_tasks))
    }
    return web.json_response(response)


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
