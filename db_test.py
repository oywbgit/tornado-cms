#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'
import os
from apps.utils import db


global BASH_PATH
if __name__ == '__main__':
    mysql = db.MyPymysqlPool("tornado",{'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'root', 'db_name': 'tornado'})

    sqlAll = "select * from django_session;"
    result = mysql.getAll(sqlAll)
    for line in result:
        print(line)

    sqlAll = "select * from auth_user;"
    result = mysql.getMany(sqlAll, 2)
    # print(result)
    for line in result:
        print(line)

    result = mysql.getOne(sqlAll)
    print(result)

    # mysql.insert("insert into myTest.aa set a=%s", (1))

    # 释放资源
    mysql.dispose()