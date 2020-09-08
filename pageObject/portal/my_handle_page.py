# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 统一系统待办页面

from common.basePage import *
from time import sleep

# 统一系统待办页面
class MyHandlePage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("my_handle_page", "portal/portal_elements.xlsx")

    def refresh_page(self):
        """
        刷新页面并跳转到最新页面
        :return:
        """
        self.refresh()
        sleep(1)
        self.switch_to_window()

    def handle_style(self, cla):
        """
        选择待办种类
        :param cla: 待办类型元素定位
        :return:
        """
        try:
            self.switch_to_frame(*self.element["iframe-我的待办"])
            self.click(*self.element[cla])
        except Exception as e:
            self.log.error("进入统一选择待办种类-->{}失败，错误信息是：{}".format(cla, e))

    def CHU_reqapproval(self, pro_num):
        """
        联通需求批次审批
        :param pro_num: 需求批次号
        :return:
        """
        try:
            self.switch_to_frame(*self.element["iframe-审批"])
            self.send_keys(pro_num, *self.element["输入框-当年项目批次"])
            self.click(*self.element["下拉框-建设方式"])
            self.click(*self.element["按钮-室分类需求"])
            self.click(*self.element["按钮-查询"])
            sleep(1)
            self.click(*self.element["单选框-第一个查询结果"])
            self.click(*self.element["按钮-审批"])
            self.click(*self.element["按钮-提交"])
            self.click(*self.element["按钮-确定"])
            sleep(2)
        except Exception as e:
            self.log.error("统一联通需求批次{}审批失败，错误信息是：{}".format(pro_num, e))