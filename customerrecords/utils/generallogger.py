import logging
import os
import datetime


class SingletonMetaclass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonMetaclass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GeneralLogger(object, metaclass=SingletonMetaclass):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("customer_records")
        self._logger.setLevel(logging.INFO)
        formatter = self.__getFormatter()
        self.__setFileHandler(formatter)

    def __getFormatter(self):
        return logging.Formatter(
            "%(asctime)s \t [%(levelname)s | "
            "%(filename)s:%(lineno)s] > %(message)s")

    def __setFileHandler(self, formatter):
        now = datetime.datetime.now()
        dirname = "./log"
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(
            dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log")
        fileHandler.setFormatter(formatter)
        self._logger.addHandler(fileHandler)

    def get_logger(self):
        return self._logger
