try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time
import os
import asyncio

images = os.listdir("images") * 3


async def fetch_string(image):
    start = time.time()
    print("{}...starting".format(image))
    await asyncio.sleep(0.01)
    translation = pytesseract.image_to_string(Image.open("images/" + image))[0:5]
    end = time.time()
    metadata = image + ": " + translation + " time: {:.2f}".format(end - start)
    print(metadata)


futures = [fetch_string(image) for image in images]
loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asyncio.wait(futures))
end = time.time()
print("Total time sanic and back {}".format(end - start))

