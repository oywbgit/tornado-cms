#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'



import tornado.web

#放在内存 redis  文件  数据库
container={}

#定义一个session类
class Session:
    def __init__(self,handler):
        self.handler=handler
        self.random_str=None
        pass

    def __genarate_random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding="utf8"))#传入byte类型
        random_str = obj.hexdigest()#返回字符串
        return random_str

    def set_value(self,key,value):
        #在container中加入随机字符串
        #加入自定义数据
        #在客户端中写入随机字符串
        if not self.random_str:
            if self.handler.get_cookie('py_session'):
                random_str=self.handler.get_cookie('py_session')
                if not container.get(random_str,None):
                    random_str = self.__genarate_random_str()
            else:
                random_str=self.__genarate_random_str()

            self.random_str=random_str
        if not container.get(self.random_str,None):
            container[self.random_str]={}
        container[self.random_str][key]=value
        #加入客户端
        self.handler.set_cookie('py_session',self.random_str)


    def get_value(self,key):
        #先去获取客户端的随机字符串
        #从container中获取自定义数据
        #random_str=self.handler.get_cookie('py_session',None)
        random_str=self.random_str
        dict_info=container.get(random_str,None)
        if not dict_info:
            return None
        return dict_info[key]