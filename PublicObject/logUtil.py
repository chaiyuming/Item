#!/usr/bin/python
# codeing: utf-8

import logging.handlers
import os


class LogUtil():

    def __init__(self, log_file_name, log_dir='log', level=logging.DEBUG):
        # 获取logger实例
        self.logger = logging.getLogger(log_file_name)
        fmt = '%(asctime)s - [%(levelname)s] - %(message)s'
        # 指定logger输出格式
        formatter = logging.Formatter(fmt)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        # 文件日志
        self.filehandler = logging.handlers.RotatingFileHandler(os.path.join(log_dir, "{}.log".format(log_file_name)), mode='w', encoding='utf-8')
        self.filehandler.setFormatter(formatter)
        # 控制台日志
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.console.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        # 指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(level)
        # 为logger添加的日志处理器
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.filehandler)

    def close_logger(self):
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.filehandler)
        self.logger = None

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    pass
