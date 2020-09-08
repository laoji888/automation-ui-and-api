# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# OA系统选择页面

from common.basePage import *
from time import sleep


# 系统选择页面
class SystemPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("system_page", "oa/OA.xlsx")

    # 进入相应系统
    def get_into_system(self, system_style, system_name):
        """
        从OA进入目标系统
        :param system_style: 系统类型元素定位
        :param system_name: 系统名元素定位
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.click(*self.element[system_style])
            self.click(*self.element[system_name])
            sleep(2)
        except Exception as e:
            LOG.error("进入{}失败，错误信息是：{}".format(system_name, e))