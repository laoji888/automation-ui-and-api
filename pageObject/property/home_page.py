# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 物业系统首页



from common.basePage import BasePage
from time import sleep




# 继承BasePage类
class Home_Page(BasePage):

    def __init__(self, driver, log):
        self.element = self.element_info("home_page", file_name="property/property_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver



    # 登录物业系统
    def login(self, username, passwd):
        self.send_keys(username, *self.element["输入框-用户名"])
        self.send_keys(passwd, *self.element["输入框-密码"])
        self.click(*self.element["按钮-登录"])
        sleep(10)
        self.await_element(*self.element["验证点-用户名"])
        check_name = self.element_text(*self.element["验证点-用户名"])
        return check_name


    #同步数据
    def Synchronous_data(self):
        self.driver.get("http://120.52.96.35:48080/default/cn.chinatowercom.property.intf.itfmsgmgr.bl.dispatcher.dispatcher.run.biz.ext")
        sleep(100)




