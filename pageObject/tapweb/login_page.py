# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 规划系统登录页面

from common.basePage import *
from time import sleep

class LoginPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("login_page", "tapweb/tapweb_elements.xlsx")

    def login(self, username, passwd):
        """
        规划系统登录
        :param username: 用户名
        :param passwd: 密码
        :return:
        """
        try:
            self.send_keys(username, *self.element["输入框-用户名"])
            self.send_keys(passwd, *self.element["输入框-密码"])
            self.click(*self.element["按钮-登录"])
            # self.js("window.focus()")
            # self.wait(5)
            sleep(2)
        except Exception as e:
            self.log.error("OA登录失败，错误信息是：{}".format(e))
