# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import os
from config.config import UTIL_CONFIG

class util():
    def __init__(self):
        # self.out_file = UTIL_CONFIG['logfile']
        self.db_log_file = UTIL_CONFIG['db_log_file']
        self.web_log_file = UTIL_CONFIG['web_log_file']

    # 以写的方式打开文件，如果文件不存在，就会自动创建
    def WriteLog(self,logtype='web'):
        if logtype == 'db':
            self.out_file = self.db_log_file


    def readline(self,):
        f = open()

    def info(self,text,isLine=True):
        file_write_obj = open(self.out_file,'w')
        file_write_obj.writelines(text)
        if isLine:
            file_write_obj.writelines('\n')
        file_write_obj.close()


class Session:
    container = {}
    def __init__(self, handler):
        self.handler = handler
        self.random_str = None

    def __genarate_random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))
        random_str = obj.hexdigest()
        return random_str

    def __setitem__(self, key, value):
        # 在container中加入随机字符串
        # 定义专属于自己的数据
        # 在客户端中写入随机字符串
        # 判断，请求的用户是否已有随机字符串
        if not self.random_str:
            random_str = self.handler.get_cookie('__session__')
            if not random_str:
                random_str = self.__genarate_random_str()
                Session.container[random_str] = {}
            else:
                # 客户端有随机字符串
                if random_str in Session.container.keys():
                    pass
                else:
                    random_str = self.__genarate_random_str()
                    Session.container[random_str] = {}
            self.random_str = random_str # self.random_str = asdfasdfasdfasdf

        Session.container[self.random_str][key] = value
        self.handler.set_cookie("__session__", self.random_str)

    def __getitem__(self, key):
        # 获取客户端的随机字符串
        # 从container中获取专属于我的数据
        #  专属信息【key】
        random_str =  self.handler.get_cookie("__session__")
        if not random_str:
            return None
        # 客户端有随机字符串
        user_info_dict = Session.container.get(random_str,None)
        if not user_info_dict:
            return None
        value = user_info_dict.get(key, None)
        return value