# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 编辑整合详情页

from common.basePage import *
from time import sleep
from common.database import *


# 规划管理主页》需求整合》塔类需求整合》编辑整合详情页
class ReqInfoPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("requirement_info_page", "tapweb/tapweb_elements.xlsx")

    def tower_req(self, req_id):
        """
        编辑需求整合详情
        :param req_id: 需求编码
        :return:
        """
        try:
            sql = "select demand_id from addr_demand where request_id ='{}'".format(req_id)
            demandId = operation_oracle(self.log, sql, databaseInfo="Tapweb_Oracle")[0]
            self.driver.get("http://120.52.96.35:9104/preweb/addr/addr.spr?method=addrSelection&demandId={}".format(demandId))
            sleep(3)
            self.click(*self.element["下拉框-建设方式"])
            self.click(*self.element["按钮-存量直接满足(建设方式)"])
            self.send_keys(35, *self.element["输入框-天线挂高开始范围"])
            self.scroll_into_element(*self.element["单选框-共享范围"])
            self.click(*self.element["单选框-共享范围"])
            self.send_keys(1, *self.element["输入框-天线个数"])
            self.send_keys(1, *self.element["输入框-机位个数"])
            self.send_keys(50, *self.element["输入框-天线挂高结束范围"])
            self.send_keys("铁塔", *self.element["输入框-谈址人"])
            self.click(*self.element["下拉框-铁塔类型"])
            self.click(*self.element["按钮-普通地面塔(铁塔类型)"])
            self.click(*self.element["单选框-是否第三方转让(否)"])
            self.send_keys("山东济南", *self.element["输入框-地址"])
            self.send_keys("15727783578", *self.element["输入框-电话"])
            self.click(*self.element["下拉框-机房类型"])
            self.click(*self.element["按钮-机房类型-无机房"])
            self.click(*self.element["单选框-供电方式-直供"])
            self.click(*self.element["单选框-是否疑难站址-否"])
            self.click(*self.element["下拉框-选址渠道"])
            self.click(*self.element["按钮-自有员工"])
            self.click(*self.element["按钮-小三角"])
            sleep(1)
            self.click(*self.element["按钮-确认"])
            sleep(3)
        except Exception as e:
            self.log.error("需求整合，错误信息是：{}".format(e))