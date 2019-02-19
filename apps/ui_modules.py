# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

from tornado.web import UIModule
from tornado import escape

class custom(UIModule):

    def render(self, *args, **kwargs):
        return escape.xhtml_escape('<h1>%s</h1>'%args[0])
