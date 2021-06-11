from aiohttp.web import Application

from asyncio import sleep, get_event_loop
from application.models.worker_model import Worker

import datetime as dt


async def worker(app: Application):
    history_num = 0
    while True:
        tasks = [await app["queue_worker"].get()]
        timeouts = [await app["queue_timeout"].get()]
        for task in tasks:
            # Add temp data outstanding tasks
            Worker.not_done_tasks.append(task)
            # add history num
            Worker.list_id.append(history_num)
            # add date create task
            Worker.date_create.append(str(dt.datetime.now()))
            history_num += 1
        for timeout in timeouts:
            # add temp timeout outstanding tasks
            Worker.timeout.append(timeout)

        loop = get_event_loop()
        loop.create_task(tasks_work(app, tasks, timeouts))


async def tasks_work(app: Application, tasks: list, timeouts: list):
    for task, timeout in zip(tasks, timeouts):
        await sleep(timeout)
        # complete task
        app["queue_timeout"].task_done()
        app["queue_worker"].task_done()
        # add сompleted tasks
        Worker.result_worker.append(task)
        # clear data worker
        Worker.not_done_tasks.pop(0)
        Worker.date_create.pop(0)
        Worker.timeout.pop(0)
        Worker.list_id.pop(0)
