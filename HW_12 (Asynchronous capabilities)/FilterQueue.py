import asyncio


class FilterQueue(asyncio.Queue):
    @property
    def window(self):
        if self.empty():
            return None
        return self._queue[0]

    def get(self, _filter=lambda x: None):
        if not any(_filter(i) for i in self._queue):
            return super().get()

        while not _filter(self.window):
            self.later()

        return super().get()

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        item = self.get_nowait()
        self.put_nowait(item)

    def __contains__(self, _filter):
        return any(_filter(i) for i in self._queue)


# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)
#
# async def getter(n, queue, filter):
#     for i in range(n):
#         await asyncio.sleep(0.1)
#         yield await queue.get(filter)
#
# async def main():
#     queue = FilterQueue(10)
#     asyncio.create_task(putter(20, queue))
#     async for res in getter(20, queue, lambda n: n % 2):
#         print(res)
#
# asyncio.run(main())
