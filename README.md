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
    "host": "127.0.0.1",
    "username": "root",
    "passwd": "12345678",
    "database": "img"
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
    results = m.select("imgs",
            column_names=["src", "alert"],
            where={
                "id": 1,
                "alert": "foo"
            },
            limit=100,
            offset=10)
    for each in results:
        print(each)
```

