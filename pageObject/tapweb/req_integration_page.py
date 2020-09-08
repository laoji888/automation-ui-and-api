# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 需求整合页

from common.basePage import *
from common.database import *
from time import sleep

# 规划管理主页》需求整合
class ReqIntegrationPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.element = self.element_info("requirement_integration_page", "tapweb/tapweb_elements.xlsx")

    # 进入需求整合
    def tower_requirement(self):
        # try:
        #     self.switch_to_window(-1)
        #     self.switch_to_frame(*self.element["框架-gisFrame"])
            self.click(*self.element["按钮-需求整合"])
            sleep(2)
        # except Exception as e:
        #     LOG.error("进入需求整合，错误信息是：{}".format(e))

    def demand_integrate(self, demand_id):
        """
        通过数据库操作来代替页面flash操作
        :param demand_id: 需求编码
        :return:
        """
        update_demand_sql = "update addr_demand aa set aa.is_modify='1',aa.is_relative='1' where aa.request_id='{}'".format(demand_id)
        delete_old_data_sql = "delete from addr_comparission_info where comparison_id='000187971000000000030237'"
        integrate_sql = "insert into addr_comparission_info(demand_id,addr_id,comparison_id,is_effective) values((select demand_id from addr_demand aa where aa.request_id ='{}'),(select id from addr_storage vv where vv.code='370105908000000329' and vv.delete_state ='0'),'000187971000000000030237','1')".format(demand_id)
        operation_oracle(self.log, update_demand_sql, "Tapweb_Oracle")
        operation_oracle(self.log, delete_old_data_sql, "Tapweb_Oracle")
        operation_oracle(self.log, integrate_sql, "Tapweb_Oracle")

    def get_requirement_id(self):
        """
        获取需求编码
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.switch_to_frame(*self.element["框架-gisFrame"])
            requirement_id = self.element_text(*self.element["文本-需求编码"])
            self.log.error("获取需求编码-{}成功".format(requirement_id))
            return requirement_id
        except Exception as e:
            self.log.error("获取需求编码失败，错误信息是：{}".format(e))

