try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from sanic import Sanic
from sanic.response import json, text
from sanic.response import stream
from sanic.log import logger
import logging
import asyncio
import time

# create logger
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('example.log')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s \t%(name)s \t%(levelname)s \t%(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

app = Sanic(__name__)


@app.route("/convert", methods=["GET"])
async def fetch_string(response):
    start = time.time()
    data = response.json
    image = data["image"]
    await asyncio.sleep(0.01)
    translation = pytesseract.image_to_string(
        Image.open("images/" + image))[0:5]
    end = time.time()
    metadata = image + ": " + translation + " time: {:.2f}".format(end - start)
    await asyncio.sleep(0)
    return text(metadata)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
