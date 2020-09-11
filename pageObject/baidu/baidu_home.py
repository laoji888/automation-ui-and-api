# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 百度首页功能封装

from selenium import webdriver
from common.base_web import Base_web
from time import sleep
from common import path


# 继承BasePage类
class BaiduHome(Base_web):
    def __init__(self, driver, log):
        self.home = self.element_info("home_page", file_name="baidu\\baidu_elements.xlsx")
        super().__init__(driver, log)
        self.log = log

    # 这是页面下的某个功能点，对应到某个系统下某个页面的功能，比如进入待办功能，
    def search(self, value):
        # 百度搜索java
        self.send_keys(value, *self.home["输入框-百度搜索框"])
        self.log.info("在输入框输入-->{}".format(value))
        self.click(*self.home["按钮-百度一下"])
        sleep(2)

    def set(self):
        # 鼠标移动到设置后点击高级搜索
        self.mouse_hover(*self.home["按钮-百度首页设置"])
        self.click(*self.home["按钮-设置下的高级搜索"])

        # 高级搜索内操作
        self.select(1, *self.home["下拉框-时间"])
        self.click(*self.home["单选框-仅网页的标题中"])
        self.send_keys("选择", *self.home["输入框-站内搜索"])
        self.elements_click(0, *self.home["按钮-搜索设置"])
        self.click(*self.home["按钮-保存设置"])
        sleep(2)



if __name__ == '__main__':
    driver = webdriver.Firefox()

