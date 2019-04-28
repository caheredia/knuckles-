try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time
import os
import asyncio

images = os.listdir("images") * 2

# Simple image to string
start = time.time()
for image in images:
    print("Start: " + image)
    t0 = time.time()
    print(pytesseract.image_to_string(Image.open("images/" + image))[0:10])
    tf = time.time()
    print("End {} time: {:.2f}".format(image, tf - t0))
end = time.time()
print("Time: {:.2f}".format(end - start))

