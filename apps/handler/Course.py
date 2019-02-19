# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'

import tornado.web

class CourseHandler(tornado.web.RequestHandler):
    def get(self,):
        # self.write('<h1>享学课堂-当前课程ID：%d</h1>'%(int(cid)))
        self.write('<h1>享学课堂-当前课程ID</h1>')
