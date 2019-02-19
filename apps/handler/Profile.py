# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

from tornado.web import RequestHandler

class ProfileHandler(RequestHandler):
    def initialize(self, database):
        self.database = database

    def get(self,username):
        self.render("index.html")

