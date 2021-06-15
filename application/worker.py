import asyncio
import datetime as dt

from aiohttp import web


class ListTasks:
    __history_num = 0
    done_tasks = []
    not_done_tasks = {"history_num": [], "date_created": [], "num": [], "timeout": []}

    @classmethod
    def get_not_done_tasks(cls):
        data = {
            f"task_{num}": {
                "history_num": cls.not_done_tasks["history_num"][num],
                "date_created": cls.not_done_tasks["date_created"][num],
                "num": cls.not_done_tasks["num"][num],
                "timeout": cls.not_done_tasks["timeout"][num],
            }
            for num in range(len(cls.not_done_tasks["num"]))
        }
        return data

    @classmethod
    def get_done_tasks(cls):
        return {"result": cls.done_tasks}

    def __add_task__(self, tasks_worker: list, timeouts: list):
        for task, timeout in zip(tasks_worker, timeouts):
            self.not_done_tasks["history_num"].append(self.__history_num)
            self.not_done_tasks["date_created"].append(str(dt.datetime.now()))
            self.not_done_tasks["num"].append(task)
            self.not_done_tasks["timeout"].append(timeout)
            self.__history_num += 1
<<<<<<< HEAD
=======
            print("append:", task)
>>>>>>> 5addc26312a74061abd5358461f43a0cffcda09d

    async def __delete_task__(self, index: int = 0):
        keys = self.not_done_tasks.keys()
        for key in keys:
            self.not_done_tasks[key].pop(index)

    async def await_tasks(self, app: web.Application):
        while True:
            # gets data tasks
            tasks_worker = [await app["queue_worker"].get()]
            timeouts = [await app["queue_timeout"].get()]
<<<<<<< HEAD
            self.__add_task__(tasks_worker, timeouts)
=======
            # print("await ", app["queue_worker"].qsize())
            # loop = asyncio.get_event_loop()
            # add temp data task
            self.__add_task__(tasks_worker, timeouts)
            # loop.create_task(self.completing_tasks())
>>>>>>> 5addc26312a74061abd5358461f43a0cffcda09d

    async def completing_tasks(self, app: web.Application):
        while await self.__size_tasks__():
            # append task in list is done tasks
            timeout = self.not_done_tasks["timeout"][0]
            # apply timeout
            await asyncio.sleep(timeout)
            self.done_tasks.append(self.not_done_tasks["num"][0])
            # del task in list is not done tasks
            await self.__delete_task__()
            # task done
            app["queue_timeout"].task_done()
            app["queue_worker"].task_done()

    async def __size_tasks__(self):
        while True:
            if len(self.not_done_tasks["num"]) != 0:
                return True
            else:
                await asyncio.sleep(0)
