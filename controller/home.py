#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import tornado.web
container = {}     #可以是数据库，可以是缓存也可以是文件

class Session:
    def __init__(self, handler):        #handler就是之前传递过来的handler方法，所以它也会有setcookie方法。
        #self.r_str 当前用户的cookie
        self.handler = handler
        self.r_str = handler.get_cookie("__session_id__")    #获取客户端的cookie
        if self.r_str:                                       #如果获取到cookie
            if self.r_str in container:                      #检查这个cookie是否存在在container中
                #如果客户端访问的md5在我的列表中证明是真的
                print("有cookie")
                self.r_str = self.r_str
                print(self.r_str)#设置一个字段，以备以后调用
            else:#否则就是假的
                self.cookie = client_publish.md5_str()  # 先生成一个变化的cookie
                handler.set_cookie("__session_id__",self.cookie)            #设置一个新的cookie
                print("假的cookie")
                container[self.cookie] = {}                                 #把这个cookie放在字典中
                self.r_str = self.cookie                                    #同样因为是新生成的cookie，还是设置一个字段，以备后患
        else:
            print("没有cookie")
            self.cookie = client_publish.md5_str()
            self.r_str = self.cookie
            container[self.r_str] = {}  # 如果没有设置cookie，第一次访问
        handler.set_cookie("__session_id__", self.r_str, expires=time.time() + 20)  # 设置cookie并且设置超时时间，每次用户访问都设置一下


    def set_session(self, key, value):
        print(container)
        container[self.r_str][key] = value  #设置session 这样可以保存很多key和value
        print(container)

    def get_session(self):
        user_session = self.handler.get_cookie("__session_id__", None)
        if user_session in container:
            try:
                if container[user_session]["is_login"]:
                    return True
            except Exception as e:
                print(e,"not value")
                return False

class MyRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        #在RequestHandler中有set_cookie方法
        self.key = Session(self)  #我们把self传递给Session 自定义的这个类中


class HomeHadler(MyRequestHandler):
    def get(self):
        #self.set_cookie()   因为这里继承了MyRequestHandler，所以在这里也有set cookie方法
        session = Session(self)
        user_login = session.get_session()
        if user_login:
            self.redirect("/index")                                          #跳转到这个用户已经登陆
        else:
            self.render("login.html")                                       #如果这个用户没有登陆，则进入登陆页面

    def post(self):
        user = self.get_argument("user")
        pwd = self.get_argument("pass")
        print(user, pwd)
        if user == "hanxu" and pwd =="123":                                 #从数据库中查找出来的用户名密码
            session = Session(self)
            session.set_session("is_login", True)
            session.set_session("user", user)
            self.redirect("/index")


class HostHadler2(MyRequestHandler):   #这种方式的话就可以方便统一使用，统一修改了
    def get(self):
        session = Session(self)
        user_session = session.get_session()
        if user_session:
            self.write("主页")
        else:                           #如果没有登陆，就调回登陆页面
            self.redirect("/home")