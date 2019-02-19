#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        lst = ["python", "www.itdiffer.com", "qiwsir@gmail.com"]
        self.render("t.html", info=str(lst))


handlers = [(r"/", IndexHandler), ]

template_path = os.path.join(os.path.dirname(__file__), "temploop")
static_path = os.path.join(os.path.dirname(__file__), "static")  # 这里增加设置了静态路径

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, template_path, static_path, debug=True)  # 这里也多了点
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
