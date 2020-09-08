# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 统一首页

from common.basePage import *

# 统一首页
class HomePage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("home_page", "portal/portal_elements.xlsx")

    def demand_input(self):
        """
        进入需求批次录入(联通)
        :return:
        """
        try:
            self.mouse_hover(*self.element["按钮-需求审批"])
            self.execute_js("getUrl('/batchManageAction/toBatchManagePage');")
        except Exception as e:
            self.log.error("进入统一需求审批失败，错误信息是：{}".format(e))

    def my_handle(self ):
        """
        进入我的待办
        :return:
        """
        try:
            self.mouse_hover(*self.element["按钮-我的工作台"])
            self.execute_js("getUrl('/bissnessAction/getDaibanPage');")
        except Exception as e:
            self.log.error("进入统一我的待办失败，错误信息是：{}".format(e))

    def get_username(self):
        """
        获取首页登录名
        :return:
        """
        username = self.element_text(*self.element["文本-登录名"])
        return username
