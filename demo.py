# 这里演示了一些例子

from YourSQL import Mysql
from sql_func import *

mysql = {
    "host": "localhost",
    "port": 3306,   # 必须是 int 类型
    "user": "root",
    "password": "12345678",
    "database": "img",
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
    # print(delete("imgs", id=12))
    # print(
    #     select("imgs",
    #            column_names=["src", "alert"],
    #            where={
    #                "id": 1234,
    #                "alert": "test"
    #            },
    #            limit=100,
    #            offset=10))
    # with Mysql(**mysql) as m:
    #     # m.insert("imgs", src="https://example.com/test.jpg", alert="test")
    #     m.delete("imgs", id=353)

    # print(update("test", new_items={"name": "kangkang"}))

    # with Mysql(**mysql) as m:
    #     for i in range(10):
    #         m.insert("test", id=i, name="name_" + str(i))

    # with Mysql(**mysql) as m:
    #     result = m.select_return_by_dict(table_name="imgs", limit=10)
    #     for each in result:
    #         print(each)
    #     # print(len(result))

    with Mysql(**mysql) as m:
        result = m.select_return_by_tuple(table_name="imgs", limit=10)
        print(result)
        result = m.select_return_by_dict("imgs",["src", "alert"],limit=10,offset=12)
        print(result)

    # print(select("imgs",["src", "alert"],{"src":"sdasd"},0,9))