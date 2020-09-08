# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 规划管理主页

from common.basePage import *
from time import sleep


class HomebPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("home_page", "tapweb/tapweb_elements.xlsx")

    def get_into_requirement_integration(self):
        """
        进入需求整合
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.click(*self.element["按钮-需求整合"])
            sleep(2)
        except Exception as e:
            self.log.error("进入需求整合，错误信息是：{}".format(e))