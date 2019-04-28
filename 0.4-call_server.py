import asyncio
import aiohttp
import time
import json
import os

url = "http://0.0.0.0:8000/convert"
images = os.listdir("images") * 1


async def fetch_image(session, url, image):
    print("{}...starting".format(image))
    async with session.get(url, data=json.dumps({"image": image})) as response:
        data = await response.text()
    return data


async def call_url(url, image):
    async with aiohttp.ClientSession() as session:
        data = await fetch_image(session, url, image)
        print(data)


futures = [call_url(url, image) for image in images]

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asyncio.wait(futures))
end = time.time()
print("Total time sanic and back {}".format(end - start))
