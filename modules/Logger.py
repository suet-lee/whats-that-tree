import logging
import os
import pathlib

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno >= self.__level

logger = logging.getLogger('default')
path = os.path.join(pathlib.Path(__file__).parent.absolute(), "app.log")
handler = logging.FileHandler(path)
handler.addFilter(MyFilter(logging.ERROR))
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log(msg):
    logger.error(msg)
