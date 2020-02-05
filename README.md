# YourSQL
对pymysql封装,简单如此,嘿~你的SQL;不,这是你的SQL



## quick start

### 导入(import)

```python
from YourSQL import Mysql
```

### 配置(config)

```python
mysql = {
    "host": "localhost",
    "port": 3306,   # 必须是 int 类型
    "user": "root",
    "password": "12345678",
    "database": "img",
}
```



### 增(insert)

```python
with Mysql(**mysql) as m:
    for i in range(10):
        m.insert("test", id=i, name="name_" + str(i))

```



### 删(delete)

```python
with Mysql(**mysql) as m:
        m.delete("test", id=1)
```



### 改(update)

```python
with Mysql(**mysql) as m:
    m.update("test", new_items={
        "name": "kainhuck"
    }, where={
        "id": 2
    })
```



### 查(select)

```python
 with Mysql(**mysql) as m:
        result = m.select_return_by_dict(table_name="imgs", limit=10)
        for each in result:
            print(each)

 with Mysql(**mysql) as m:
        result = m.select_return_by_tuple(table_name="imgs", limit=10)
        for each in result:
            print(each)
```

