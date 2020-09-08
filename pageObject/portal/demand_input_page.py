# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 需求录入页面

from common.basePage import *
from time import sleep


# 需求审批》需求批次录入
class DemandInputPage(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("demand_input_page", "portal/portal_elements.xlsx")

    def demand_add(self, addstyle):
        """
        进入需求录入页面，新增需求
        :param addstyle: 需求类型元素定位
        :return:
        """
        try:
            self.switch_to_frame(*self.element["iframe-需求批次录入"])
            self.click(*self.element["按钮-需求批次录入-新增"])
            self.click(*self.element[addstyle])
            self.switch_to_default()
            sleep(2)
        except Exception as e:
            self.log.error("进入统一-->{}失败，错误信息是：{}".format(addstyle, e))

    def demand_state_check(self, build_style):
        """
        新增项目审批状态校验
        :param build_style: 项目类型元素定位
        :return:
        """
        try:
            self.switch_to_window(0)
            self.switch_to_frame(*self.element["iframe-需求批次录入"])
            self.click(*self.element["下拉框-建设方式"])
            self.click(*self.element[build_style])
            # self.js('document.getElementById("1004").click();')
            self.click(*self.element["下拉框-当年项目批次"])
            self.click(*self.element["按钮-最后一个项目批次"])
            self.click(*self.element["按钮-查询"])
            project_num_check = self.element_text(*self.element["校验点-当年项目批次"])
            state_check = self.element_text(*self.element["校验点-状态"])
            return project_num_check,state_check
        except Exception as e:
            self.log.error("获取检验点信息-->{}失败，错误信息是：{}".format(build_style, e))

