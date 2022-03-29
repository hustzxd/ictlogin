#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def isConnected():
    hostname = "baidu.com"  # example
    response = 1
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False


def login(username='', passward=''):
    os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
    driver = webdriver.PhantomJS()
    driver.get('https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=1&')
    name = driver.find_element_by_name("username")
    name.send_keys(username)
    password = driver.find_element_by_id('password')
    password.send_keys(passward)
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()


if __name__ == '__main__':
    if not isConnected():
        print('login')
        login(username='', passward='')
    else:
        print('already login')
# 
