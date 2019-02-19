#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'



import logging
def log():
    logger = logging.getLogger('服务端')
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter('%(name)s-->%(asctime)s-->%(message)s')
    fh = logging.FileHandler('ServerLog.txt', encoding='utf-8')

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logger

lg = log()
lg.error('wsx')
