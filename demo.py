# 这里演示了一些例子

from YourSQL import Mysql
from sql_func import *

mysql = {
    "host": "127.0.0.1",
    "username": "root",
    "passwd": "12345678",
    "database": "img"
}

if __name__ == '__main__':

    # # 使用方法
    # with Mysql(**mysql) as m:
    #     results = m.select("imgs",
    #            column_names=["src", "alert"],
    #            limit=100,
    #            offset=10)
    #     for each in results:
    #         print(each)
    # print(insert("imgs", src="https://demo.com/test.jpg", alert="test"))
    # print(delete("imgs", id=12, alert="test"))
    # print(
    #     select("imgs",
    #            column_names=["src", "alert"],
    #            where={
    #                "id": 1234,
    #                "alert": "test"
    #            },
    #            limit=100,
    #            offset=10))
    with Mysql(**mysql) as m:
        # m.insert("imgs", src="https://example.com/test.jpg", alert="test")
        m.delete("imgs", id=353)
