# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'



import pymysql
from config.config import DATABASES as dbconfig
from warnings import filterwarnings
filterwarnings('ignore', category=pymysql.Warning)
CONNECT_TIMEOUT = 100
IP = ''
PORT = ''
USER = ''
PASSSWORD = ''

if 'default' in dbconfig.keys():
    conf        = dbconfig['default']
    HOST        = conf['HOST']
    USER        = conf['USER']
    PASSSWORD   = conf['PASSWORD']
    PORT        = conf['PORT']
    NAME        = conf['NAME']

from DBUtils.PooledDB import PooledDB
import traceback

from apps.libs import RUtils

util = RUtils.util()

class DB():
    def __init__(self):
        self.host = HOST
        self.name = NAME
        self.user = USER
        self.passwd = PASSSWORD
        self.port = PORT
        self.pool = PooledDB(pymysql,5,host=self.host,user=self.user,passwd=self.passwd,db=self.name,port=self.port) #5为连接池里的最少连接数


    # 连接数据库
    def connect_db(self):
        self.db = self.pool.connection()
        self.cur = self.db.cursor()

    # 关闭连接
    def close_db(self):
        self.cur.close()
        self.db.close()

    # 执行sql
    def execute(self, sql):
        self.connect_db()
        return self.cur.execute(sql)

    # 获取所有数据列表
    def get_list(self, table, fields):
        sql = "select %s from %s" % (",".join(fields), table)
        try:
            self.execute(sql)
            result = self.cur.fetchall()
            if result:
                result = [dict((k, row[i]) for i, k in enumerate(fields)) for row in result]
            else:
                result = {}
            return result;
        except:
            util.WriteLog('db').info("Execute '%s' error: %s" % (sql, traceback.format_exc()))
        finally:
            self.close_db()

    # 获取某一条数据，返回字典
    def get_one(self, table, fields, where):
        if isinstance(where, dict) and where:
            conditions = []
            for k, v in where.items():
                conditions.append("%s='%s'" % (k, v))
        sql = "select %s from %s where %s" % (",".join(fields), table, ' AND '.join(conditions))
        try:
            self.execute(sql)
            result = self.cur.fetchone()
            if result:
                result = dict((k, result[i]) for i, k in enumerate(fields))
            else:
                result = {}
            return result
        except:
            util.WriteLog('db').info("Execute '%s' error: %s" % (sql, traceback.format_exc()))
        finally:
            self.close_db()

    # 更新数据
    def update(self, table, fields):
        data = ",".join(["%s='%s'" % (k, v) for k, v in fields.items()])
        sql = "update %s set %s where id=%s " % (table, data, fields["id"])
        try:
            return self.execute(sql)
        except:
            util.WriteLog('db').info("Execute '%s' error: %s" % (sql, traceback.format_exc()))
        finally:
            self.close_db()

    # 添加数据
    def create(self, table, data):
        fields, values = [], []
        for k, v in data.items():
            fields.append(k)
            values.append("'%s'" % v)
        sql = "insert into %s (%s) values (%s)" % (table, ",".join(fields), ",".join(values))
        try:
            return self.execute(sql)
        except:
            util.WriteLog('db').info("Execute '%s' error: %s" % (sql, traceback.format_exc()))
        finally:
            self.close_db()

    # 删除数据
    def delete(self, table, where):
        if isinstance(where, dict) and where:
            conditions = []
            for k, v in where.items():
                conditions.append("%s='%s'" % (k, v))
        sql = "delete from %s where %s" % (table, ' AND '.join(conditions))
        try:
            return self.execute(sql)
        except:
            util.WriteLog('db').info("Execute '%s' error: %s" % (sql, traceback.format_exc()))
        finally:
            self.close_db()
