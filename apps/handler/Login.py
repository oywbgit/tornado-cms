#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import tornado.web
import tornado.ioloop

from apps.handler.Base import BaseHandler
from apps.libs.RUtils import Session

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html' ,state = "")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        _xsrf = self.get_argument('_xsrf')
        # code =self.get_argument('code')
        # check_code = self.session['CheckCode']
        # if username =="oywb" and password == "123" and code.upper() == check_code.upper():
        if username =="admin" and password == "admin" :
            self.write("登录成功")
            self.set_cookie('login_xsrf',_xsrf)
            self.set_cookie('username',username)
            self.set_cookie('password',password)
            self.set_cookie('update_time',password)
            self.set_cookie('__session__',password)

        else:
            self.render('login.html',state = "验证码错误")

        self.write(self.get_cookie('login_xsrf'))