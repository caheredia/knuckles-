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
t0 = time.time()
for image in images:
    start = time.time()
    print("{}...starting".format(image))
    translation = pytesseract.image_to_string(Image.open("images/" + image))[0:5]
    end = time.time()
    metadata = image + ": " + translation + " time: {:.2f}".format(end - start)
    print(metadata)
tf = time.time()
print("Total time: {:.2f}".format(tf - t0))

