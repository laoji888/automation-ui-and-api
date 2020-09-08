# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
#合同系统-合同起草-草稿箱页面


"""
页面应用了远程执行cmd方法，实现文件上传，操作excel文件
页面应用了执行js方法，实现下拉滚动条，删除readonly属性
"""

from selenium import webdriver
from common.basePage import BasePage
from time import sleep
from common import path
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase



class DraftboxPage(BasePage):


    #读取draftbox_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("draftbox_page", file_name="cms/thecontract_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver



    # 修改物业推送的合同
    def modification_contract(self, serialnumber,contractname,thedateof,contractamount,sitecode,paymentinstructions,paymentdate ):
        """
        :param serialnumber: 合同流水号
        :param contractname: 合同名称
        :param thedateof: 合同有效期
        :param contractamount: 合同总金额
        :param sitecode: 站址编码
        :param paymentinstructions: 付款说明
        :param paymentdate: 计划付款日期
        :return:

        """
        self.mouse_hover(*self.element["按钮-合同起草"])
        sleep(3)
        self.click(*self.element["按钮-草稿箱"])
        self.switch_to_frame(*self.element["框架-mainframe"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        sleep(8)
        self.click(*self.element["单选框-选择合同"])
        sleep(3)
        self.click(*self.element["按钮-修改"])
        sleep(10)
        self.switch_to_window(-1)
        sleep(5)
        self.run_command("C:\自动化\click.exe", "Gaogd_ie", "cms_host")
        sleep(3)
        self.switch_to_frame(*self.element["框架-经济事项"])
        self.click(*self.element["单选框-选择经济事项"])
        self.click(*self.element["按钮-确定"])
        self.switch_to_default()
        sleep(5)
        self.click(*self.element["下拉框-是否有条件转名合同"])
        self.click(*self.element["下拉框-选择是否有条件转名合同"])
        self.send_keys(contractname, *self.element["输入框-合同名称"])
        sleep(5)
        self.execute_js("$('html,body').scrollTop(800);")
        sleep(3)
        self.execute_js('document.getElementById("text_no").click();')
        sleep(10)
        self.run_command("C:\自动化\ht_closetext.exe","Gaogd_ie","cms_host")
        sleep(10)
        self.click(*self.element["按钮-定稿预览"])
        sleep(10)
        self.run_command("C:\自动化\ht_Closefile.exe", "Gaogd_ie", "cms_host")
        sleep(8)
        self.send_keys(thedateof, *self.element["输入框-合同有效期（结束日期）"])
        sleep(3)
        self.execute_js("$('html,body').scrollTop(1200);")
        self.click(*self.element["单选框-是否开具增值税发票"])
        self.await_element(*self.element["单选框-合同约定租金模式"])
        self.click(*self.element["单选框-合同约定租金模式"])
        sleep(3)
        self.send_keys(contractamount,*self.element["输入框-合同总金额"])
        sleep(3)
        self.execute_js("$('html,body').scrollTop(1800);")
        self.await_element(*self.element["按钮-添加（账户信息）"])
        self.click(*self.element["按钮-添加（账户信息）"])
        self.switch_to_frame(*self.element["框架上传附件"])
        self.await_element(*self.element["单选框-选择账户信息"])
        self.click(*self.element["单选框-选择账户信息"])
        self.click(*self.element["按钮-确定（选择账户信息）"])
        self.switch_to_default()
        sleep(3)
        self.click(*self.element["按钮-添加（付款条款）"])
        sleep(3)
        #删除日历只读属性
        self.execute_js("$('.mini-buttonedit-input').removeAttr('readonly');")
        sleep(2)
        self.send_keys(paymentdate, *self.element["输入框-计划付款日期"])
        self.send_keys(sitecode, *self.element["输入框-站址编码"])
        self.send_keys(paymentinstructions, *self.element["输入框-付款说明"])
        self.click(*self.element["按钮-提交"])
        sleep(6)
        #切换框架
        self.switch_to_frame(*self.element["框架-选择办理人框架"])
        self.double_click(*self.element["按钮-选择下一步办理人为"])
        self.click(*self.element["按钮-提交（选择办理人页面）"])
        sleep(5)




