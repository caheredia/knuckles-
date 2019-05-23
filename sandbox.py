import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s \t%(name)s \t%(levelname)s \t%(message)s'}
    },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG},
        'f': {'class': 'logging.FileHandler',
              'formatter': 'f',
              'filename': "example.log",
              'level': logging.DEBUG},
        'g': {'class': 'logging.FileHandler',
              'formatter': 'f',
              'filename': "debug.log",
              'level': logging.DEBUG}
    },
    loggers={
        "root": {
            'handlers': ['f'],
            'level': logging.DEBUG,
        },
        "test": {
            'handlers': ['g'],
            'level': logging.DEBUG,
        },
    }
)

dictConfig(logging_config)

logger = logging.getLogger(__name__)
logger.debug('often makes a very good meal of %s', 'visiting tourists')
other_logger = logging.getLogger('test')
other_logger.debug('testing the new logger')
