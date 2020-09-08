# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 室分类批次页面

from common.basePage import *
from time import sleep
from common.path import *


# 需求审批》需求批次录入》新增》室分类批次
class RoomClassPage(BasePage):

    def __init__(self, driver, log):
        super(RoomClassPage, self).__init__(driver, log)
        self.log = log
        self.element = self.element_info("room_class_page", "portal/portal_elements.xlsx")

    # 获取新增需求批次
    def project_num(self):
        """
        获取新增需求批次
        :return:
        """
        self.switch_to_window(-1)
        ProNum = self.element_attribute("value", *self.element["输入框-当年项目批次"])
        return ProNum

    def upload_attachment(self):
        """
        添加附件
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.execute_js("window.focus()")
            self.click(*self.element["按钮-添加附件"])
            self.switch_to_frame(*self.element["iframe-上传附件"])
            # autoit_path = file_path("testData/portal", "attachment_upload.exe")
            autoit_path = r"C:\Users\Administrator\Desktop\UIAutomation_QM\testData\portal\attachment_upload.exe"
            self.log.info("cmd>>{}".format(autoit_path))
            self.run_command(autoit_path,"Mawj_ie","portal_host")
            sleep(2)
            self.click(*self.element["按钮-确认上传"])
            sleep(2)
            self.alert_accept()
            sleep(2)
        except Exception as e:
            self.log.error("联通需求批次上传附件失败，错误信息是：{}".format(e))

    def upload_demand_plan(self):
        """
        需求计划导入(ie)
        :return:
        """
        try:
            self.switch_to_window(-1)
            self.switch_to_default()
            self.click(*self.element["文件输入框-需求计划导入"])
            # autoit_path = file_path("testData/portal", "demand_plan.exe")
            autoit_path = r"C:\Users\Administrator\Desktop\UIAutomation_QM\testData\portal\demand_plan.exe"
            self.log.info("cmd>>{}".format(autoit_path))
            self.run_command(autoit_path,"Mawj_ie","portal_host")
            self.click(*self.element["按钮-导入"])
            sleep(2)
            self.alert_accept()
            sleep(2)
        except Exception as e:
            self.log.error("联通需求批次需求计划导入失败，错误信息是：{}".format(e))

    def demand_commit(self):
        """
        提交需求
        :return:
        """
        try:
            self.click(*self.element["按钮-提交"])
            self.click(*self.element["按钮-确认提交"])
            # sleep(1)
            # self.alert_accept()
            sleep(2)
        except Exception as e:
            self.log.error("联通需求批次需求提交失败，错误信息是：{}".format(e))

