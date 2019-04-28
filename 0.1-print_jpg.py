try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time

# Simple image to string
start = time.time()
print(pytesseract.image_to_string(Image.open("images/test.png")))
end = time.time()
print("Time: {:.2f}".format(end - start))

