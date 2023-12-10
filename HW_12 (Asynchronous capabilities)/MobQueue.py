import asyncio
import string
from collections import Counter


async def sender(queue, pattern):
    for char in pattern:
        await queue.put(char)
    await queue.put(None)


async def reader(queue, number):
    counter = Counter()
    count_none = 0

    while count_none < number:
        item = await queue.get()
        if item is None:
            count_none += 1
        else:
            counter[item] += 1

    return counter


# async def main(n):
#     queue = asyncio.Queue(4)
#     alp = string.ascii_lowercase
#     senders = [sender(queue, alp[len(alp) * i // n: len(alp) * (i + 1) // n]) for i in range(n)]
#     res = await asyncio.gather(reader(queue, n), *senders)
#     print(", ".join(f"{key}:{val}" for key, val in sorted(res[0].items())))
#
# asyncio.run(main(10))
