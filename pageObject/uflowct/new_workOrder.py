# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# 新建工单页面功能封装

from common.basePage import BasePage
from time import sleep
from unittest import TestCase as t


# 封装新建工单页面下的功能
class NewWorkOrder(BasePage):

    def __init__(self, driver, log):
        """
    初始化元素信息
        :param driver: 浏览器对象
        """

        self.log = log
        self.home = self.element_info("home_page", file_name="uflowct/uflowct.xlsx")
        self.demand_workOrder_page = self.element_info("demand_workOrder_page", file_name="uflowct/uflowct.xlsx")
        super().__init__(driver, log,self.demand_workOrder_page)

    def enter_new_demand_workOrder(self):
        """
    进入新建工单页面下的新建需求工单页面，验证切换后的页面title
        """
        try:
            self.click(*self.home["按钮-新建工单(需求工单)"])
        except Exception as e:
            self.click(*self.home["按钮-新建工单(首页)"])
            self.click(*self.home["按钮-新建工单(需求工单)"])
        self.switch_to_window()
        t.assertIn(self, "IT工单管理平台", self.get_title())

    def new_demand_workOrder(self, title, describe):
        """
    新建需求工单，验证提交后的提示信息
        :param describe: 工单描述
        :param title:工单标题
        """
        # 填写新建需求工单的详细信息
        self.send_keys(title, *self.demand_workOrder_page["输入框-工单标题"])
        self.click(*self.demand_workOrder_page["下拉框-设计模块"])
        self.click(*self.demand_workOrder_page["单选框-4A管理"])
        # 选择设计模块后下拉框不隐藏，需要点击下其他地方
        self.click(*self.demand_workOrder_page["输入框-工单标题"])
        self.send_keys(describe, *self.demand_workOrder_page["输入框-工单描述"])
        self.click(*self.demand_workOrder_page["时间控件-期望上线时间"])
        self.select(6, *self.demand_workOrder_page["下拉框-年份选择"])
        self.click(*self.demand_workOrder_page["按钮-日期选择"])
        self.click(*self.demand_workOrder_page["按钮-时间控件确定"])
        self.click(*self.demand_workOrder_page["按钮-提交"])
        t.assertIn(self, "成功", self.element_text(*self.demand_workOrder_page["校验点-提交成功"]))
        self.click(*self.demand_workOrder_page["按钮-提交后的确定"])
        self.log.info("新建需求工单成功，工单标题还：{}".format(title))
