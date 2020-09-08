# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 物业系统-合同信息管理页面



from common.basePage import BasePage
from time import sleep




# 继承BasePage类

class Contract_ManagementPage(BasePage):




    def __init__(self, driver, log):
        self.element = self.element_info("ContractManagement_page", file_name="property/property_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver




    # 查询合同信息
    def the_query(self, Contractno):

        self.await_element(*self.element["按钮-基础信息"])
        self.mouse_hover(*self.element["按钮-基础信息"])
        self.await_element(*self.element["按钮-合同信息管理"])
        self.click(*self.element["按钮-合同信息管理"])
        self.switch_to_frame(*self.element["框架-合同信息管理"])
        self.await_element(*self.element["输入框-合同编号"])
        self.send_keys(Contractno, *self.element["输入框-合同编号"])
        self.click(*self.element["按钮-查询"])
        sleep(10)
        #获取合同名称
        self.await_element(*self.element["校验点-合同名称"])
        check_name = self.element_text(*self.element["校验点-合同名称"])
        return check_name


