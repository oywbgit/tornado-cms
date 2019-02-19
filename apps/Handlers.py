# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


# import tornado
import tornado.web
# import tornado.httpserver
import tornado.options

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


if __name__ == '__main__':
    # print(__dir__)
    # print(dir())
    # print(list.__dict__)
    # print(list.__dict__.keys())
    for obj in dir():
        if obj.endswith("Handler"):
            print(obj)
            print(obj[:-7])
        # print(type(obj))
        # print(obj.endswith("Handler"))

    # import inspect
    # print ([i for i in dir(list) if inspect.isbuiltin(getattr(list, i))])
