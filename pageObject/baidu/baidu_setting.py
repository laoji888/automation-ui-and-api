from selenium import webdriver
from common.base_web import Base_web
from time import sleep
from common import path



# 继承Base_web类
class Sample2(Base_web):

    def element(self):
        element = self.element_info("sample2")
        return element

    # 这是页面下的某个功能点，对应到某个系统下某个页面的功能，比如进入待办功能，
    # 相当于新大陆平台页面下的用例
    def login(self, username, passwd):
        # 资源管理系统
        self.send_keys(username, *self.element()["输入框-用户名"])
        self.send_keys(passwd, *self.element()["输入框-密码"])
        self.click(*self.element()["按钮-登入"])

        # #浏览器前进后退
        # sleep(5)
        # self.back()
        # sleep(5)
        # self.forward()
        # sleep(2)
        # self.js('$(".mnav")[0].click()')
        # sleep(3)
        # 切换窗口
        # self.switch_to_window(1)
        # self.get_title()

        #self.send_keys("123", self.element(11))


        # # 鼠标移动到设置后点击高级搜索
        # self.mouse_hover(*self.element(2))
        # self.click(*self.element(3))
        #
        # # 高级搜索内操作
        # self.select(1, *self.element(4))
        # self.click(*self.element(5))
        # self.send_keys("选择", *self.element(6))
        # self.find_elements(0, *self.element(7))
        # self.click(*self.element(8))

    # 这是页面下的某个功能点，对应到某个系统下某个页面的功能，比如进入待办功能，
    # 相当于新大陆平台页面下的用例
    # def to_ele(self, value):
    #     self.send_keys(value, *self.element(0))
    #     self.click(*self.element(1))
        # 滚动条滚动到下一页
        # self.to_element(*self.element(9))
        # sleep(3)
