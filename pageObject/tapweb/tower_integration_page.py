# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 塔类需求整合页

from common.basePage import *
from time import sleep


# 规划管理主页》需求整合》塔类需求整合
class TowerIntegrationPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("tower_integration_page", "tapweb/tapweb_elements.xlsx")

    def req_search(self, ReqId):
        """
        搜索需求编码
        :param DemandId:
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.send_keys(ReqId, *self.element["输入框-需求编码"])
            self.click(*self.element["按钮-查询"])
            # self.js("window.focus()")
            # self.wait(5)
            sleep(2)
        except Exception as e:
            self.log.error("搜索需求编码，错误信息是：{}".format(e))

    def get_requirement_id(self):
        """
        获取需求编码用于检验
        :return:
        """
        try:
            demand_id = self.element_text(*self.element["文本-站址编码"])
            self.log.info("获取站址编码-{}成功".format(demand_id))
            return demand_id
        except Exception as e:
            self.log.error("获取站址编码失败，错误信息是：{}".format(e))


