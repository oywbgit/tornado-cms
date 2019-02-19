#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import tornado
import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.log
import logging
from tornado.options import options, define

# 这里配置的是日志的路径，配置好后控制台的相应信息就会保存到目标路径中。
options.log_file_prefix = os.path.join(os.path.dirname(__file__), 'logs/tornado_main.log')


# 后台函数
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [  # 路由设置
            (r"/", MainHandler),
        ]

        self.settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),  # 设置模板路径
            static_path=os.path.join(os.path.dirname(__file__), 'static'),  # 设置静态资源引用路路径
            # static_url_prefix='/myPath/static/', # 设置html中静态文件的引用路径，默认为/static/
            debug=True,
        )
        super(Application, self).__init__(handlers, **self.settings)


# 格式化日志输出格式
# 默认是这种的：[I 160807 09:27:17 web:1971] 200 GET / (::1) 7.00ms
# 格式化成这种的：[2016-08-07 09:38:01 执行文件名:执行函数名:执行行数 日志等级] 内容消息
class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


def main():
    tornado.options.define("port", default="8888", help="run on the port", type=int)  # 设置全局变量port
    tornado.options.parse_command_line()  # 启动应用前面的设置项目
    # [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)  # 在这里应用之前的全局变量port
    tornado.ioloop.IOLoop.current().start()  # 启动监听


if __name__ == "__main__":
    main()

