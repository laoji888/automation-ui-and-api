# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 合同系统-首页



from common.basePage import BasePage
from time import sleep





class Home_Page(BasePage):



    # 读取home_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("home_page", file_name="cms/thecontract_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver




    # 登录合同系统
    def login(self, username, passwd):
        self.send_keys(username, *self.element["输入框-用户名"])
        self.send_keys(passwd, *self.element["输入框-密码"])
        self.click(*self.element["按钮-登录"])
        sleep(3)

        # 获取登录后用户名
        check_name = self.element_text(*self.element["校验点-用户名"])
        return check_name

