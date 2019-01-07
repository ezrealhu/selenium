#!/usr/bin/env python  
# encoding: utf-8

from selenium import webdriver
import unittest
import time, os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://115.236.67.13:9000/zdzz")  #测试网址
        time.sleep(1)

    def assertAndScreenshot(self, a, b):
        if a == b:
            print("测试通过！")
        else:
            print('标题不等于“%s” 测试不通过!' % b)
            self.driver.get_screenshot_as_file("E:\\PycharmProjects\\selenium-test\\report\\1.jpg")

    def tearDown(self):
        self.driver.quit()

def wait_title(self, location):   #通过判断title的方式,封装显式等待方法
    try:
        WebDriverWait(self.driver, 3, 0.5).until(EC.title_contains(location))
    except:
            "等待页面时间超时！"
    return


def assertAndScreenshot(self, a, b):
    if a == b:
        print("测试通过！")
    else:
        print('标题不等于“%s” 测试不通过!' % b)
        self.driver.get_screenshot_as_file("E:\\PycharmProjects\\selenium-test\\report\\1.jpg")
