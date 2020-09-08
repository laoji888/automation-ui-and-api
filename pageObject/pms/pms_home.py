# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# pms首页的功能封装
from common.basePage import BasePage
from time import sleep
from unittest import TestCase as t


# 封装PMS系统首页的功能
class PmsHome(BasePage):

    def __init__(self, driver, log):
        """
    初始化当前页面使用的元素信息
        :param driver: 浏览器对象
        """
        self.log = log
        self.home_page = self.element_info(sheetname="home_page", file_name="pms/pms_elements.xlsx")
        self.backlog_page = self.element_info(sheetname="backlog_page", file_name="pms/pms_elements.xlsx")
        super().__init__(driver, log, self.backlog_page)

    def login(self, username):
        """
    登录到pms系统
        :param username: 用户名
        """
        self.send_keys(username, *self.home_page["输入框-用户名"])
        self.keys_enter()
        self.click(*self.home_page["按钮-系统公告关闭"])
        sleep(3)
        user = self.element_text(*self.home_page["校验点-登陆者"])
        t.assertIn(self, "王玉芳", user)
        self.log.info("登录成功，登录的用户名是{}".format(username))

    def enter_into_backlog(self):
        """
    进入我的工作下的我的待办并切换到框架
        """
        self.mouse_hover(*self.home_page["按钮-我的工作"])
        self.click(*self.home_page["按钮-我的待办"])
        self.switch_to_frame(*self.backlog_page["框架-代办下一级框架"])
        sleep(2)
        self.switch_to_frame(*self.backlog_page["框架-代办下二级框架"])
        self.log.info("已进入我的工作下的我的待办并切换到框架")

    def click_one(self):
        """
    点击我的待办下的第8条数据
        """
        self.click(*self.backlog_page["链接-我的代办下第8条数据"])
        self.switch_to_window()
        sleep(3)
        try:
            self.alert_accept()
            self.log.info("已进入项目详情页弹窗处理成功")
        except:
            self.log.info("处理弹窗失败或者没有弹窗")
            pass


    def uploading(self, name):
        """
    文件上传
        :param name: 要上传的文件名
        """
        sleep(13)
        self.scroll_into_element(*self.backlog_page["按钮-上传附件"])
        self.click(*self.backlog_page["按钮-上传附件"])
        self.switch_to_frame(*self.backlog_page["框架-上传附件框架"])
        sleep(3)
        self.click(*self.backlog_page["下拉框-上传类型"])
        self.click(*self.backlog_page["按钮-上传类型》维护改造原因"])
        self.clickXY(*self.backlog_page["按钮-浏览"], section="Jiyn_firefox", key="pms_host")
        self.linux_file_upload(file_path=name, section="Jiyn_firefox", key="pms_host")
        sleep(2)
        self.click(*self.backlog_page["按钮-上传"])
        self.click(*self.backlog_page["按钮-上传确认按钮"])
        self.await_element(*self.backlog_page["校验点-上传成功"])
        t.assertIn(self, "操作成功！", self.element_text(*self.backlog_page["校验点-上传成功"]))
        sleep(2)
        self.click(*self.backlog_page["按钮-上传后的确认"])
        self.log.info("文件上传成功")
