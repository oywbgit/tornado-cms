# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'



import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
from tornado.web import url, URLSpec
#定义端口配置
define('port', type=int, default=8080)

#创建视图处理器
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>hello，world</h1>")

class CourseHandler2(tornado.web.RequestHandler):
    def get(self,name ):
        self.write('<h1>享学课堂-当前课程名称：%s</h1>'%(name))

class CourseHandler(tornado.web.RequestHandler):
    def get(self,cid ):
        self.write('<h1>享学课堂-当前课程ID：%d</h1>'%(int(cid)))

# 请求重定向
class XXKTHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://www.11face.com')

# 重定向方法下载文件
class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        url = 'https://github.com/tornadoweb/tornado/archive/master.zip'
        self.redirect(url)

#创建路由表
urls = [
    (r"/", MainHandler),
    (r"/index",MainHandler),
    (r'/course2/([a-zA-Zi]+)',CourseHandler2),
    # (r'/course/(d+)',CourseHandler),
    (r'/course/([0-9]+)',CourseHandler),
    (r"/xxkt", XXKTHandler),
    (r"/easy", tornado.web.RedirectHandler, dict(url='http://www.11face.com')), #直接在路由表里配置
    (r'/download',DownloadHandler)
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