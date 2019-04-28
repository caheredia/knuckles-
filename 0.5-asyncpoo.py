"""This didnt work, it yielded a time of 25 seconds, 
which is about the same as just using blocking functions. 
Because of no iprovement, I'm uninstalling package from environment. """

import asyncpool
import logging
import asyncio

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time
import os

images = os.listdir("images") * 2


async def fetch_string(image, result_queue):
    print("{}...starting".format(image))
    await asyncio.sleep(0.01)
    await result_queue.put(
        pytesseract.image_to_string(Image.open("images/" + image))[0:5]
    )
    await asyncio.sleep(0.01)


async def result_reader(queue):
    while True:
        value = await queue.get()
        if value is None:
            break
        print(value)


async def run():

    result_queue = asyncio.Queue()

    reader_future = asyncio.ensure_future(result_reader(result_queue), loop=loop)

    # Start a worker pool with 10 coroutines, invokes `example_coro` and waits for it to complete or 5 minutes to pass.
    async with asyncpool.AsyncPool(
        loop,
        num_workers=3,
        name="ExamplePool",
        logger=logging.getLogger("ExamplePool"),
        worker_co=fetch_string,
        max_task_time=300,
        log_every_n=10,
    ) as pool:
        for image in images:
            await pool.push(image, result_queue)

    await result_queue.put(None)
    await reader_future


loop = asyncio.get_event_loop()
t0 = time.time()
loop.run_until_complete(run())
tf = time.time()
print("Total run time: {:.2f}".format(tf - t0))

