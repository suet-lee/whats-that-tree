import logging
from flask import current_app as app
# import os
# import pathlib

# A rudimentary logger for errors

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno >= self.__level

logger = logging.getLogger('default')
# path = os.path.join(pathlib.Path(__file__).parent.absolute(), "app.log")
handler = logging.FileHandler(app.root_path)
handler.addFilter(MyFilter(logging.ERROR))
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log(msg):
    logger.error(msg)
