# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import os
import importlib


def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append("." + name)

    return modules

def get_urls(package = "clazz"):
    # package = "E:/python/web/rtornado/apps/clazz"
    # package = "clazz"

    modules = get_modules(package)

    handler = []

    # 将包下的所有模块，逐个导入，并调用其中的函数
    for module in modules:
        module = importlib.import_module(module, package)

        for attr in dir(module):
            if not attr.startswith("__") and attr.endswith('Handler'):
                print(attr)
                func = getattr(module, attr)
                # func()
                router = r'/%s' % attr[:-7].lower()
                handler.append((router,func))

    return handler

import glob
import importlib
import os


def import_modules(pathname: str) -> dict:
    """
    导入指定路径或者目录下的模块，并返回模块信息

    :param pathname: 要导入的模块路径(相对路径)，可以导入指定目录下的模块，只要符合glob路径表达式写法即可
    :return: 模块信息字典
    """
    modules_dict = {}
    module_paths = glob.glob(pathname+'/**.py')
    for path in module_paths:
        module_name = path.replace("/", '.').replace("\\", '.')[:-3]
        module = importlib.import_module(module_name)
        for element in dir(module):
            # 获取用户自定义的函数和变量名称
            if not element.startswith('__') and element.endswith('Handler'):
                modules_dict[element] = eval('module.{}'.format(element))
    return modules_dict


def get_Handler():
    handler = []
    modules = import_modules()
    for m in modules:
        print(m)


if __name__ == '__main__':
    urls = get_urls()
    print( urls)

