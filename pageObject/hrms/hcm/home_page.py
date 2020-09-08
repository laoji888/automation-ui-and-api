# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 人力人力资源管理业务平台首页



from common.basePage import BasePage
from time import sleep



# 继承BasePage类

class HomePage(BasePage):



    # 读取home_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("home_page", file_name="hr/hr_hcm_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver



    # 登录人力系统业务平台
    def login(self, username, passwd):
        """
        :param username: 用户名
        :param passwd: 密码
        :return:

        """
        self.send_keys(username, *self.element["输入框-用户名"])
        self.send_keys(passwd, *self.element["输入框-密码"])
        self.click(*self.element["按钮-登录"])
        sleep(3)
        self.await_element(*self.element["验证点-用户名"])
        check_username = self.element_text(*self.element["验证点-用户名"])
        return check_username

