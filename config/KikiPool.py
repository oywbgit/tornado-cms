# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


from apps.utils import db
from pymysql.err import OperationalError

class ConnectPool(object):
    def __init__(self):
        try:
            self.pool = db.MyPymysqlPool("tornado", {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'root',
                                             'db_name': 'tornado'})
        except OperationalError as e:
            self.pool = None

        # self.mysql_db = MySQLDatabase(host=mysql_conf['host'], user=mysql_conf['username'], passwd=mysql_conf['password'], database='test')
        # self.cache_redis = Redis(host=redis_conf['host'], port=redis_conf['port'], db=redis_conf['db'])
    def get_dbPool(self):
        return self.pool