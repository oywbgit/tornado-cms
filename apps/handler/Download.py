# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import tornado.web

# 重定向方法下载文件
class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        url = 'https://github.com/tornadoweb/tornado/archive/master.zip'
        self.redirect(url)