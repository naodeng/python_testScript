#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging


def log():
    # 日志配置（level日志级别）
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")


if __name__ == '__main__':
    log()
