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


logging_dict = dict(version=1,
                    disable_existing_loggers=False,
                    formatters={
                        'generic': {
                            'format': '%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
                            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                            'class': 'logging.Formatter'},
                        'access': {
                            'format': '%(asctime)s - (%(name)s)[%(levelname)s] [%(host)s]: %(request)s %(message)s %(status)d %(byte)d',
                            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                            'class': 'logging.Formatter'}
                    },
                    handlers={
                        'console': {
                            'class': 'logging.FileHandler',
                            'formatter': 'generic',
                            'filename': "example.log"},
                        'error_console': {
                            'class': 'logging.FileHandler',
                            'formatter': 'generic',
                            'filename': "example.log"},
                        'access_console': {
                            'class': 'logging.FileHandler',
                            'formatter': 'access',
                            'filename': "example.log"},
                    },
                    loggers={
                        'sanic.root': {'level': 'INFO', 'handlers': ['console']},
                        'sanic.error': {'level': 'INFO', 'handlers': ['error_console'], 'propagate': True, 'qualname': 'sanic.error'},
                        'sanic.access': {'level': 'INFO', 'handlers': ['access_console'], 'propagate': True, 'qualname': 'sanic.access'}}
                    )


app = Sanic(__name__, log_config=logging_dict)


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
    logger.info(f"processing {image}")
    return text(metadata)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
