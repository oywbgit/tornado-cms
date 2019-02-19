# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import tornado.web

#创建视图处理器
class MainHandler(tornado.web.RequestHandler):

    def initialize(self, db):
        '''
            覆盖父类的initialize方法
        '''
        self.db = db

    def get(self,**kwargs):
        canshu = self.get_arguments('name')
        self.write(str(canshu) + str(self.db))
        self.write(str(self.db))
        # self.render("index.html")