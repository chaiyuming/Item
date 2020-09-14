#!/usr/bin/python
# codeing: utf-8

import logging.handlers
import os


class LogUtil():

    def __init__(self, log_file_name, log_dir='log', level=logging.DEBUG):
        # self.logger = logging.basicConfig(format='%(asctime)s - %(module)s - %(funcName)s - %(filename)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)
        self._logger = logging.getLogger(log_file_name)
        fmt = '%(asctime)s - [%(levelname)s] - %(message)s'
        formatter = logging.Formatter(fmt)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        # self.filehandler = logging.handlers.RotatingFileHandler(os.path.join(log_dir, "{}.log".format(log_file_name)),
        #                                                    maxBytes=1024 * 1024 * 10, backupCount=5)
        self.filehandler = logging.handlers.RotatingFileHandler(os.path.join(log_dir, "{}.log".format(log_file_name)), mode ='w' , encoding='utf-8')
        # rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # self.filehandler =logging.FileHandler(os.path.join(rootdir,log_dir,"{}.log".format(log_file_name)))
        self.filehandler.setFormatter(formatter)
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.console.setFormatter(formatter)
        self._logger.setLevel(level)
        self._logger.addHandler(self.console)
        self._logger.addHandler(self.filehandler)

    def close_logger(self):
        self._logger.removeHandler(self.console)
        self._logger.removeHandler(self.filehandler)
        self._logger = None

    def info(self, msg):
        self._logger.info(msg)

    def warning(self, msg):
        self._logger.warning(msg)

    def error(self, msg):
        self._logger.error(msg)

    def debug(self, msg):
        self._logger.debug(msg)

    def critical(self, msg):
        self._logger.critical(msg)


if __name__ == '__main__':
    pass
