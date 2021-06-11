from aiohttp import web
from application.responses.response import json_response
from marshmallow.exceptions import ValidationError
import asyncio
import json


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web.HTTPException as ex:
        return json_response(status=ex.status, text_status=ex.text, data_ret={})
    except ValidationError as ex:
        return json_response(status=404, text_status=str(ex), data_ret={})
    except json.decoder.JSONDecodeError:
        return json_response(status=422, text_status="Error in json", data_ret={})
    except KeyError as ex:
        return json_response(status=404, text_status="ValidationError", data_ret={})
    except Exception as e:
        request.app.logger.exception("Exception: {}".format(str(e)), exc_info=e)
        return json_response(status=500, text_status=str(e), data_ret={})


@web.middleware
async def workers_middleware(request, handler):
    try:
        return await handler(request)
    except asyncio.queues.QueueEmpty:
        return json_response(text_status="There are no tasks in the queue")
