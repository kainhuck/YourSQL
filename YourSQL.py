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

    def update(self, table_name, new_items={}, where={}):
        self.executeSql(update(table_name, new_items, where))

    def select_return_by_tuple(self, table_name, column_names=[], where={}, limit=None, offset=0):
        self.executeSql(select(table_name, column_names, where, limit, offset))
        return self.cursor.fetchall()

    def select_return_by_dict(self, table_name, column_names=[], where={}, limit=None, offset=0):
        self.executeSql(select(table_name, column_names, where, limit, offset))
        result_tuple = self.cursor.fetchall()
        result_dict = []
        if len(column_names):
            for item in result_tuple:
                temp = {}
                for i in range(len(column_names)):
                    temp[column_names[i]] = item[i]
                result_dict.append(temp)
        else:
            for column_info in self.cursor.description:
                column_names.append(column_info[0])
            for item in result_tuple:
                temp = {}
                for i in range(len(column_names)):
                    temp[column_names[i]] = item[i]
                result_dict.append(temp)

        return result_dict

    def executeSql(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行，为了及时跟进数据库这句最好加上
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()