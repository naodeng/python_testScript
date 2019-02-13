#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis


def redis_select():
    # 连接redis
    r = redis.Redis(host='10.1.51.36', port=6379, db=0)
    key = r.keys()
    print(key)   # 打印redis里的key值
    print type(key)  # 打印redis里的key类型


def redis_delete():
    # 连接redis
    r = redis.Redis(host='10.1.51.36', port=6379, db=0)
    # 设置想要删除的key值
    key = r.keys("python")
    # 执行删除
    r.delete(key)


if __name__ == '__main__':
    redis_select()
    redis_delete()
