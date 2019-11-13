#!/usr/bin/python
# -*- coding: UTF-8 -*-
import script_time, datetime


# 获取时间戳
def getTimeStamp():
    currentTime = datetime.datetime.now()
    print('TimeStamp in second for %s is  %d ' % (currentTime,int(script_time.mktime(currentTime.timetuple()))))
    print('TimeStamp in micros second for %s is  %d ' % (currentTime, int(script_time.mktime(currentTime.timetuple())) * 1000))


# 时间计算
def timedelta():
    currentTime = datetime.datetime.now()
    daysBefore = currentTime - datetime.timedelta(days=10,hours=5,minutes=20,seconds=30)
    print('%s - 10 days = %s '%(currentTime,daysBefore))


# 时间格式转换
def dateFormate():
    date_formate = "%Y-%m-%d"
    dateFormate = datetime.datetime.strptime('2019-01-23', date_formate)
    print(dateFormate)

    date_formate = "%Y%m%d"
    dateFormate = datetime.datetime.strptime('20190123', date_formate)
    print(dateFormate)

    currentTime = datetime.datetime.now()
    print('before : %s after : %s' %(currentTime, currentTime.strftime("%Y%m%d%H%M%S")))

    date_formate = "%Y%m%d%H%M%S"
    date_string = '20190125102536'
    print('before : %s after : %s' % (date_string, datetime.datetime.strptime(date_string, date_formate)))


if __name__ == '__main__':
    getTimeStamp()
    timedelta()
