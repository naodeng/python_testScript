#!/usr/bin/python
# -*- coding: UTF-8 -*-

import script_time
from selenium import webdriver


def login(username, password):
    url = 'https://passport.csdn.net/login'  # 登录url

    driver = webdriver.Firefox()
    driver.get(url)
    print driver.title
    # 点击账号登录连接切换到账号登录页面
    driver.find_element_by_link_text('帐号登录').click();
    # 页面停留1s等待页面加载完成
    script_time.sleep(1)
    name_input = driver.find_element_by_name('all')  # 找到用户名的框框
    pass_input = driver.find_element_by_name('pwd')  # 找到输入密码的框框
    login_button = driver.find_element_by_xpath('//button')  # 找到登录按钮

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    script_time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    script_time.sleep(0.2)
    login_button.click()            # 点击登录

    script_time.sleep(0.2)
    print driver.get_cookies()

    script_time.sleep(2)
    print driver.title

    # driver.close()


if __name__ == "__main__":
    user = "python"
    pw = "password"
    login(user, pw)
