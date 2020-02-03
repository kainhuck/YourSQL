#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from sql_func import *

class Mysql(object):
    def __init__(self, host, username, passwd, database):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.database = database
        self.cursor = None

    def __enter__(self):
        self.db = pymysql.connect(self.host, self.username, self.passwd, self.database)
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            # 如果出现异常
            print("An Exception: %s." % exc_val)

        self.db.close()
        return True

    def insert(self, table_name, **kwargs):
        self.executeSql(insert(table_name, **kwargs))

    def delete(self, table_name, **kwargs):
        self.executeSql(delete(table_name, **kwargs))

    def select(self, table_name, column_names=[], where={}, limit=None, offset=0):
        self.executeSql(select(table_name, column_names, where, limit, offset))
        return self.cursor.fetchall()

    def executeSql(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行，为了及时跟进数据库这句最好加上
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()