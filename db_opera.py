#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 连接数据库
db = MySQLdb.connect("db_ip", "db_username", "db_password", "db_name", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL查询语句(可输入增删改查sql语句)
sql = "SELECT * FROM python"
# noinspection PyBroadException
try:
    cursor.execute(sql)  # 执行SQL语句
    results = cursor.fetchall()  # 获取所有记录列表
    for row in results:
        comments = row[1]
        ip = row[3]
    print("python1=%s,python2=%s" % \
            ("python1", "python2"))
except:
    print("Error: 没查询到数据")


# 关闭数据库连接
db.close()
