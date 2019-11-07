#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import tornado.web

class RegisterHandler(tornado.web.RequestHandler):   #注册
    def get(self):
        self.render('08register.html',error=None)

    def post(self):
        if self._check_argument():
            try:
                self._create_user()
                self.render('08login.html',error=None)
            except AuthError as e:
                self.render('08register.html',error=e)
            except Exception as e:
                self.render('08register.html',error=e)
        else:
            self.render('08register.html',error='input error')

    def _check_argument(self):      #对密码和用户名进行检验
        username = self.get_argument('name','')
        passwd = self.get_argument('password1','')
        if len(username)<10 and len(passwd)<10:
            return True
        else:
            return False

    def _create_user(self):
        if User.by_name(self.get_argument('name','')):
            raise AuthError('Name is registered')
        if self.get_argument('password1','') != self.get_argument('password2',''):
            raise AuthError('Password error')
        user = User()
        user.username = self.get_argument('name','')
        user.password = self.get_argument('password1','')
        session.add(user)
        session.commit()