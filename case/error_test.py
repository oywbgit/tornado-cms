# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options

define('port', type=int, default=8080)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>享学课堂-Tornado教程</h1>")


class test1Handler(tornado.web.RequestHandler):
    def get(self):
        self.write_error(404)
class test2Handler(tornado.web.RequestHandler):
    def get(self):
        self.write_error(500)
class test3Handler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(500)
class Test4Handler(tornado.web.RequestHandler):
    def get(self):
        #raise tornado.web.HTTPError(404)
        raise tornado.web.HTTPError(status_code=404, log_message='test', reason='Not found page!')
class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h3 style="color:red">无效地址！</h3>')
urls=[
    (r'/',MainHandler),
    (r'/test1',test1Handler),
    (r'/test2',test2Handler),
    (r'/test3',test3Handler),
    (r'/test4',Test4Handler),
    (r'/test5',ErrorHandler)
]
#创建配置-开启调试模式
configs = dict(debug=True)
#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls, **configs)



#创建服务器
def make_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#启动服务器
if __name__ == '__main__':
    make_app()