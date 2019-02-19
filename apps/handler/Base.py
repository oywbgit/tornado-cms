#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import tornado.web
import tornado.ioloop
from apps.libs.RUtils import Session

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)