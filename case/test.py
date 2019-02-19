# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'


import os,sys

# package = "E:/python/web/rtornado/apps/"
# dirs = os.listdir(package)
# for file in dirs:
#     print (file)


# from apps import initHandlers as init
# urls = init.get_urls()
#
# print ( urls)

import pkgutil
# from apps import clazz
# from apps import initHandlers
# package = "E:/python/web/rtornado/apps/clazz"
# modules = initHandlers.get_modules(package)
# print( modules)
# import importlib
# user = importlib.import_module('user')
#
# for filefiner, name, ispkg in pkgutil.iter_modules(clazz.__path__, clazz.__name__ + "."):
#     print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))



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


def read_bigFile(file_path):
    f = open(file_path,'r')
    cont = f.read(10)
    while len(cont) >0 :
        print(cont)
        cont = f.read(10)
    f.close()
import inspect
import sys


import chardet
if __name__ == '__main__':
    # 打开一个文件
    file = "E:\\python\\web\\rtornado\\public\\fonts\\iconfont.ttf"
    coding = 'unicode'
    with open(file,'rb+') as fp: pass
    # fp = open(file,'rb',encoding=coding)
    # ss = fp.read()
    # print(ss)
        # file_data = fp.read()
        # result = chardet.detect(file_data)
        # file_content = file_data.decode(encoding=result['encoding'])
    # from io import
