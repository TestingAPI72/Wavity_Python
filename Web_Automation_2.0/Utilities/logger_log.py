import logging
import inspect


def customLogger():
    logName = inspect.stack()[1][3]
    loggers = logging.getLogger(logName)
    loggers.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("Logfile.log", mode='a')
    formatter = logging.Formatter('%(asctime)s:: [Log] ::%(levelname)s::%(message)s')
    fileHandler.setFormatter(formatter)
    if loggers.hasHandlers():
        loggers.handlers.clear()
    loggers.addHandler(fileHandler)
    return loggers

