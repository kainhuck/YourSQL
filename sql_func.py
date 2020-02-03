# 这里定义了一些构造sql语句的函数
def insert(table_name, **kwargs):
    '''
    构造sql插入语句
    :param table_name:
    :param kwargs:
    :return:
    '''
    # 创建sql语句
    field = '('
    for each in kwargs.keys():
        field += each + ','
    field = field[:-1] + ') VALUES ('

    for each in kwargs.values():
        field += '"' + each + '",'
    field = field[:-1] + ');'

    sql = "INSERT INTO %s %s" % (table_name, field)
    return sql


def delete(table_name, **kwargs):
    """
    构造sql删除语句
    delete from <table_name> where <>="<>" and <>="<>";
    """
    field = ''
    for item in kwargs.items():
        field += item[0] + '="' + str(item[1]) + '" AND '
    field = field[:-5] + ';'
    sql = "DELETE FROM %s WHERE %s" % (table_name, field)
    return sql


def select(table_name, column_names=[], where={}, limit=None, offset=0):
    """
    column_names : 待查询的属性
    where : 约束
    limit : 返回记录数
    offset : SELECT语句开始查询的数据偏移量

    SELECT column_name,column_name
    FROM table_name
    [WHERE Clause]
    [LIMIT N][ OFFSET M]
    """
    field = "*"
    where_part = ""
    limit_part = ""
    offset_part = ""

    if len(column_names):
        # 构造查询字段
        field = ""
        for each in column_names:
            field += str(each) + ","
        field = field[:-1]

    if len(where):
        # 构造 where 部分
        where_part = " WHERE "
        for item in where.items():
            where_part += str(item[0]) + '="' + str(item[1]) + '" AND '
        where_part = where_part[:-5]

    if limit != None:
        # 构造 limit 部分
        limit_part = " LIMIT " + str(int(limit))

        if offset > 0:
            # 构造 offset 部分:
            offset_part = " OFFSET " + str(int(offset))

    sql = "SELECT %s FROM %s%s%s%s;" % (field, table_name, where_part,
                                        limit_part, offset_part)
    return sql