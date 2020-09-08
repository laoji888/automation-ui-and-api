# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# OA首页

from selenium import webdriver
from common.basePage import *
from time import sleep
from common import path



# OA系统首页
class HomePage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("home_page", "oa/OA.xlsx")

    # 进入运营管理
    def into_operation_management(self):
        """
        进入首页后点击运营管理
        :return:
        """
        try:
            self.click(*self.element["按钮-运营管理"])
            sleep(2)
        except Exception as e:
            self.log.error("进入运营管理，错误信息是：{}".format(e))

    def get_username(self):
        """
        获取首页登录名，用于校验
        :return:
        """
        username = self.element_text(*self.element["校验点-用户名"])
        return username
