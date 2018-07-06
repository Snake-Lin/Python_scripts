# -*- coding:utf-8 -*-
"""
@author: lin
@file: databaseManager.py
@software: PyCharm
@project: AI-Data-Python
@time: 18-3-15 下午6:00
@desc: 数据库操作文件,　输入不同sql语句，获取数据库返回结果
"""
import os

import cx_Oracle
from pymysql import *



# 解决oracle数据库返回字段???显示问题
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class MysqlEngine(object):
    """mysql数据库连接工具类"""
    def __init__(self, server_mysql_db):
        self.config = server_mysql_db

    def open(self):
        self.conn = connect(self.config['HOST'],
                            self.config['USER'],
                            self.config['PASSWORD'],
                            self.config['DBNAME'],
                            self.config['PORT'],
                            charset='utf8')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()


class OracleEngine(object):
    """oracle数据库连接工具类"""
    def __init__(self, server_oracle_db):
        self.config = server_oracle_db

    def open(self):
        self.conn = cx_Oracle.connect(self.config['USER'],
                                      self.config['PASSWORD'],
                                      self.config['HOST'])
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()


# 不同数据库创建不同的数据库对象
# 合约乘数查询数据库对象
count_oracle = OracleEngine(configs.count_oracle_db)


# 禁买卖池数据库查询对象
oracle = OracleEngine(configs.server_oracle_db)


if __name__ == '__main__':

  pass