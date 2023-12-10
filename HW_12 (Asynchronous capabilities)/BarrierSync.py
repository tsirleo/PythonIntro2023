import asyncio
from random import shuffle


shared_list = []


async def serial(number, barrier):
    await barrier.wait()

    shared_list.append(number)
    if len(shared_list) == barrier.parties:
        for i in sorted(shared_list):
            print(i)


# async def main(num):
#     bar = asyncio.Barrier(num)
#     tasks = [serial(i * 2 % num, bar) for i in range(num)]
#     shuffle(tasks)
#     await asyncio.gather(*tasks)
#
# asyncio.run(main(10))
