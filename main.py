# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import os.path
import random

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.log

import logging
import glob
import importlib

from config.KikiPool import ConnectPool


def init():
    dbPool = ConnectPool().get_dbPool()
    setting = {
        'main': dict(db=dbPool),
        # 'index':dict(objPool=objPool)
    }
    return setting


PARAMETERS = init()

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

import inspect
import apps.handler
from apps.handler.Index import IndexHandler
from tornado.web import StaticFileHandler

current_path = os.path.dirname(__file__)
# 创建配置-开启调试模式
settings = {
    # "static_path": os.path.join(os.path.dirname(__file__), "public"),
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "public/static"),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",  # cookie自定义字符串加盐
    "login_url": "/login",
    # 'xsrf_cookies': True,                                               # 防止跨站伪造
}
from apps.handler.File import FileHandler

# 创建路由表
urls = [
    # (r'^/()$', StaticFileHandler,{"path": os.path.join(current_path, "public"), "default_filename": "index.html"}),
    # (r'^.*^phtml$()', FileHandler,{"path": os.path.join(current_path, "public"), "default_filename": "index.html"}),
    # (r'^/.*$', FileHandler),
    # (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,  dict(path=settings['static_path'])),
]
package = "apps\\handler"

objPool = {}
module_paths = glob.glob(package + '/**.py')
for path in module_paths:
    module_name = path.replace("/", '.').replace("\\", '.')[:-3]
    module = importlib.import_module(module_name)
    for element in dir(module):
        # 获取用户自定义的函数和变量名称
        if not element.startswith('__') and element.endswith('Handler'):
            fun = eval('module.{}'.format(element))
            handler_path = str(fun.__dict__['__module__'])
            if not str(fun.__dict__['__module__']).startswith('tornado'):
                # print(handler_path)
                handler_name = element[:-7].lower()
                if handler_name in PARAMETERS.keys():
                    # print(PARAMETERS[handler_name])
                    obj = ('/' + handler_name + ".tpy.*", fun, PARAMETERS[handler_name])
                else:
                    obj = ('/' + handler_name + ".tpy.*", fun)
                objPool[handler_name] = fun
                urls.append(obj)

# urls.append((r'^.*^tpy$()', FileHandler,{"path": os.path.join(current_path, "public"), "default_filename": "index.html"}))
urls.append((r'.*()', FileHandler, {"path": os.path.join(current_path, "public"), "default_filename": "index.html"}))
urls.append((r'/api.tpy$()', IndexHandler, dict(objPool=objPool)))


# 自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, settings):
        super(MyApplication, self).__init__(
            handlers=urls,
            ui_modules=module_list,
            debug=True,
            **settings
        )


# 这里配置的是日志的路径，配置好后控制台的相应信息就会保存到目标路径中。
# options.log_file_prefix = os.path.join(os.path.dirname(__file__), 'logs/tornado_main.log')

# 格式化日志输出格式
# 默认是这种的：[I 160807 09:27:17 web:1971] 200 GET / (::1) 7.00ms
# 格式化成这种的：[2016-08-07 09:38:01 执行文件名:执行函数名:执行行数 日志等级] 内容消息
class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


module_list = {}


# 创建服务器
def make_app():
    tornado.options.parse_command_line()
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls, settings))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


# 启动服务器
if __name__ == '__main__':
    make_app()
