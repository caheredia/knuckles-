try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Simple image to string
print(type(pytesseract.image_to_string(Image.open("test.png"))))
