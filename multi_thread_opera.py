#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import random
import time
import datetime


# 设置并发数量
threadNum = 3


# 定义一个随机方法
def get_caes_list():
    return [i for i in range(1, 20)]


# 定义执行方法
def run_case(case_id):
    run_time = random.randrange(1, 10)
    time.sleep(run_time)
    print('run case: %d, result is pass, run time is : %d seconds' % (case_id, run_time))


def pool():
    # 设置多线程执行
    start = datetime.datetime.now()
    pool = ThreadPool(threadNum)
    pool.map(run_case, get_caes_list())
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    end = datetime.datetime.now()
    t1 = str((end - start).seconds)
    print('多线程执行时间为:' + t1)


def one():
    # 设置单线程执行
    start = datetime.datetime.now()
    for i in range(1, 20):
        run_case(i)
    end = datetime.datetime.now()
    t2 = str((end - start).seconds)
    print('单线程执行时间为:' + t2)


if __name__ == '__main__':
    pool()
    one()
