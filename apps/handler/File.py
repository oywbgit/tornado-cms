#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'

from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os
# class FileHandler(StaticFileHandler):
from tornado.web import HTTPError

from socket import *
import codecs
import datetime
#解析请求报文的请求形象路径


class FileHandler(RequestHandler):
    def initialize(self, path, default_filename=None,encoding='UTF-8'):
        self.root = path
        self.default_filename = default_filename
        self.encoding = encoding

    def upfile(self, *args, **kwargs):
        file_metas = self.request.files["filename"]     # 获取文件信息
        for meta in file_metas:
            file_name = meta['filename']                # 获得他的文件名字
            file_names = os.path.join('static','img',file_name)
            with open(file_names,'wb') as up:           # 打开本地一个文件
                up.write(meta['body'])                  # body就是文件内容，把他写到本地

    def post(self,):
        fun = self.get_argument('fun', default='default', strip=True)
        if fun == '':
            self.get()
        else:
            eval('self.' + fun + '()')


    def get(self, *args, **kwargs):
        uri = str(self.request.uri)
        if uri.find('?') > 0:
            wh = uri.index('?')
            filename = str(uri[:wh]).replace('/',os.sep)
        else:
            filename = str(uri).replace('/',os.sep)
        path = str(self.root).replace('/',os.sep)

        file_path = path + filename
        # self.write(file_path)
        if os.path.isdir(file_path):
            file_path = file_path + os.sep + self.default_filename

        if os.path.exists(file_path):
            pass
        else:
            # raise HTTPError(404)
            return

        from apps.utils import endwith
        self.set_header("charset", self.encoding)
        try:
            end = os.path.splitext(file_path)[-1]
            if end in endwith.format.keys():
                EndFormat = endwith.format[end]
                self.set_header("Content-Type", EndFormat)
            else:
                EndFormat =  'application/octet-stream'
                self.set_header("Content-Type",EndFormat)
        except KeyError as e:
            self.write(str(e))
            raise HTTPError(503)
        try:
            with open(file_path, 'rb+') as f:
                ss = f.read()
                self.write(ss)
            f.close()
        except UnicodeDecodeError as e:
            self.write(str(e))
            raise HTTPError(503)


