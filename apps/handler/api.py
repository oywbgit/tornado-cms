#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


from tornado.web import RequestHandler

class ApiHandler(RequestHandler):

    def get(self):
        self.write('Hello World')


    def post(self,):
        fun = self.get_argument('fun', default='default', strip=True)
        handler = self.get_argument('h', default='api', strip=True)
        if fun == '':
            self.get()
        else:
            eval('self.' + fun + '()')

        if not handler == 'api':
            # eval('')
            self.write('方法未定义')
