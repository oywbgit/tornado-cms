# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

CELERY_IMPORTS = ('tasks',)
BROKER_URL = 'amqp://guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'amqp://'