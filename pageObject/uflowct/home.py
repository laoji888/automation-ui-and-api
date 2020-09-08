# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# 服务工单系统首页和登录页的功能封装
from common import path
from common.basePage import BasePage
from time import sleep
from unittest import TestCase as t


# 封装IT服务工单首页下的功能
class Home(BasePage):

    def __init__(self, driver, log):
        """
    初始化首页功能用到的元素信息
        :param driver: 浏览器对象
        """

        self.log = log
        self.home = self.element_info(sheetname="home_page", file_name="uflowct/uflowct.xlsx")
        super().__init__(driver, log, self.home)

    def login(self, username, pwd, user, sleeptime=0):
        """
    登录到it服务工单系统，验证登录者
        :param s: 休眠时间
        :param username: 用户名
        :param pwd: 用户密码
        :param user: 用户姓名（用于登录后的验证）
        """
        self.send_keys(username, *self.home["输入框-用户名"])
        self.send_keys(pwd, *self.home["输入框-密码"])
        self.keys_enter()
        if sleeptime != 0:
            sleep(sleeptime)
        user1 = self.element_text(*self.home["校验点-登陆者"])
        t.assertIn(self, user, user1)
        self.log.info("登录成功，登录的用户名是{}".format(username))


    def enter_new_workOrder(self):
        """
    进入首页下的新建工单页面
        """
        self.click(*self.home["按钮-新建工单(首页)"])
        self.log.info("进入首页下的新建工单页面")

    def enter_backlog(self):
        """
    进入我的工作台下的我的待办
        """
        self.click(*self.home["按钮-我的工作台"])
        sleep(1)
        self.click(*self.home["按钮-我的工作台》我的待办"])
        self.log.info("进入我的工作台下的我的待办")

    def enter_my_workOrder(self):
        """
    进入我的工作台下的我的工单
        """
        self.click(*self.home["按钮-我的工作台"])
        self.click(*self.home["按钮-我的工作台》我的工单"])
        self.log.info("进入我的工作台下的我的工单")

    def enter_unified_issue(self):
        """
    进入我的工作台下的统一发布
        """
        self.click(*self.home["按钮-我的工作台"])
        self.click(*self.home["按钮-我的工作台》统一发布"])
        self.log.info("进入我的工作台下的统一发布")
