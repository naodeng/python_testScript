#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import time


def time1():  # datetime.datetime.now()获取的是当前日期
    start = datetime.datetime.now()
    time.sleep(1)
    end = datetime.datetime.now()
    t1 = bytes((end - start).seconds)
    print('第一种方法脚本运行时间为:' + t1)


def time2():  # time.time()获取自纪元以来的当前时间（以秒为单位)
    start = time.time()
    time.sleep(1)
    end = time.time()
    # t2 = bytes(end - start)
    t2 = "{:.0f}".format(end - start)
    print('第二种方法脚本运行时间为:' + t2)


def time3():  # time.clock()CPU的执行时间
    start = time.clock()
    time.sleep(1)
    end = time.clock()
    # t3 = bytes(end - start)
    t3 = "{:.0f}".format(end - start)
    print('第三种方法脚本运行时间为:' + t3)


if __name__ == '__main__':
    time1()
    time2()
    time3()
