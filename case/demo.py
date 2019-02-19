# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

"""
    tornado web app对于网页模板的处理和静态文件的操作
    网页模板：html页面
    处理：定义html页面、渲染html页面，响应html页面[浏览器]
    静态资源：图片/js/css/字体...
    操作：配置静态资源、查询静态资源[html]、响应数据
"""

# 引入需要的模块
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer
import os.path

# 定义变量
define("port", default=8000, help="默认端口8000")


# 创建视图类
class IndexHandler(RequestHandler):
    def get(self):
        msg = "hello,零"
        self.render("demo.html", info=msg)


# 程序入口
if __name__ == '__main__':
    # 开始监听
    parse_command_line()
    app = Application(
        [
            (r'/', IndexHandler)
        ],

        # 项目配置信息
        # 网页模板
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # 静态文件
        static_path=os.path.join(os.path.dirname(__file__), "static"),

        debug=True
    )

    # 部署
    server = HTTPServer(app)
    server.listen(options.port)

    # 轮询监听
    IOLoop.current().start()

