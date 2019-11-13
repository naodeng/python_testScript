#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib


def md5(value):
    md5 = hashlib.md5()
    md5.update(str(value).encode('utf-8'))
    value = md5.hexdigest()
    return value


# md5加密
def md5_test():
    # 待加密的值
    key = 'python'
    # 加密后的值
    key_md5 = md5(key)
    print('MD5加密前：' + key)
    print('MD5加密后：' + key_md5)


if __name__ == '__main__':
    md5_test()
