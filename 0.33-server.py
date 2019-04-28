try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from sanic import Sanic
from sanic.response import json, text
from sanic.response import stream
import asyncio
import time

app = Sanic(__name__)


@app.route("/convert", methods=["GET"])
async def fetch_string(response):
    start = time.time()
    data = response.json
    image = data["image"]
    await asyncio.sleep(0.01)
    translation = pytesseract.image_to_string(Image.open("images/" + image))[0:5]
    end = time.time()
    metadata = image + ": " + translation + " time: {:.2f}".format(end - start)
    await asyncio.sleep(0)
    return text(metadata)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
