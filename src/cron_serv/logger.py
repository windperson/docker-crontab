import logging
import sys


class ConsoleLogger:
    """
    Output log to stdout
    """
    __logger = logging.getLogger()
    __ch = logging.StreamHandler(sys.stdout)

    def __init__(self):
        self.__logger.setLevel(logging.INFO)
        self.__logger.addHandler(self.__ch)
        pass

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)
        self.__ch.flush()
        pass

    def info(self, msg, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)
        self.__ch.flush()
        pass

    def warning(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)
        self.__ch.flush()
        pass

    def error(self, msg, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)
        self.__ch.flush()
        pass

    def critical(self, msg, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)
        self.__ch.flush()
        pass
