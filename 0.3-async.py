try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time
import os
import asyncio

images = os.listdir("images") * 2


async def fetch_string(image):
    start = time.time()
    print("Start: " + image)
    await asyncio.sleep(0.01)
    data = pytesseract.image_to_string(Image.open("images/" + image))[0:10]
    await asyncio.sleep(0.01)
    print(data)
    end = time.time()
    print(image + " time: {:.2f}".format(end - start))


async def main():
    ## build list with image to string objects
    futures = [fetch_string(image) for image in images]
    await asyncio.gather(*futures)


# loop = asyncio.get_event_loop()
t0 = time.time()
asyncio.run(main())
tf = time.time()
print("Total time to read files {}".format(tf - t0))
