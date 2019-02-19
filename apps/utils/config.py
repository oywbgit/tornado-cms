#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import os
import configparser
CNF_PATH = os.path.dirname(__file__)
class Config(object):
    """
    # Config().get_content("user_information")

    配置文件里面的参数
    [tornado]
    host = 192.168.1.101
    port = 3306
    user = root
    password = python123
    """
    def __init__(self, config_filename="config.cnf",cnf_path=CNF_PATH):
        file_path = os.path.join(cnf_path, config_filename)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def get_content(self, section):
        result = {}
        for option in self.get_options(section):
            value = self.cf.get(section, option)
            result[option] = int(value) if value.isdigit() else value
        return result

if __name__ == '__main__':
    conf = Config().get_content('tornado')
    print(conf)