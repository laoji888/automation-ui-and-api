# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 人力人力资源管理系统业务平台-新员工入职审批页面



from common.basePage import BasePage
from time import sleep






class NewEmpApprovalPage(BasePage):



    #读取newempapproval_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("newempapproval_page", file_name="hr/hr_hcm_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver




    # 新员工入职，新建申请功能
    def induction(self, name, idno, dateofbirth, rank, thephone):

        """
        name : 输入框姓名
        idno : 证件号码
        rank : 录入职级
        thephone : 移动电话
        dateofbirth : 出生日期

        """
        self.await_element(*self.element["按钮-员工管理"])
        self.click(*self.element["按钮-员工管理"])
        self.await_element(*self.element["按钮-员工团队"])
        self.click(*self.element["按钮-员工团队"])
        self.await_element(*self.element["按钮-入职"])
        self.click(*self.element["按钮-入职"])
        sleep(5)
        self.await_element(*self.element["按钮-新员工入职审批"])
        self.click(*self.element["按钮-新员工入职审批"])
        self.await_element(*self.element["按钮-新建申请"])
        self.click(*self.element["按钮-新建申请"])
        self.await_element(*self.element["按钮-生成工号"])
        self.click(*self.element["按钮-生成工号"])
        sleep(3)
        self.await_element(*self.element["输入框-姓名"])
        #self.send_keys(worknumber, *self.element["输入框-姓名"])
        self.send_keys(name, *self.element["输入框-姓名"])
        self.click(*self.element["下拉框-证件类型"])
        self.await_element(*self.element["下拉框-选择证件类型"])
        self.click(*self.element["下拉框-选择证件类型"])
        self.await_element(*self.element["输入框-证件号码"])
        self.send_keys(idno, *self.element["输入框-证件号码"])
        self.click(*self.element["下拉框-性别"])
        self.click(*self.element["下拉框-选择性别"])
        sleep(5)
        self.send_keys(dateofbirth, *self.element["输入框-出生日期"])
        sleep(3)
        self.click(*self.element["下拉框-选聘方式"])
        self.await_element(*self.element["按钮-选聘方式》组织调动"])
        self.click(*self.element["按钮-选聘方式》组织调动"])
        self.click(*self.element["下拉框-进入铁塔来源"])
        self.await_element(*self.element["按钮-进入铁塔来源》其他社会单位"])
        self.click(*self.element["按钮-进入铁塔来源》其他社会单位"])
        self.send_keys(rank, *self.element["输入框-拟录入职级"])
        self.click(*self.element["按钮-所属公司"])
        self.await_element(*self.element["按钮-选择所属公司"])
        self.click(*self.element["按钮-选择所属公司"])
        self.click(*self.element["按钮-所属部门"])
        self.await_element(*self.element["按钮-所属部门》公司领导"])
        self.click(*self.element["按钮-所属部门》公司领导"])
        self.click(*self.element["按钮-员工分类"])
        self.await_element(*self.element["按钮-员工分类》总部公司总经理"])
        self.click(*self.element["按钮-员工分类》总部公司总经理"])
        sleep(3)
        worknumber = self.execute_js('return document.getElementById("el113").value;')
        self.send_keys(thephone, *self.element["输入框-移动电话"])
        self.click(*self.element["按钮-提交审批"])
        self.await_element(*self.element["验证点-操作成功"])

        #获取提交后弹窗文本
        check_text = self.element_text(*self.element["验证点-操作成功"])
        return check_text, worknumber


    # 校验新员工入职审批状态
    def check_approval_status(self, worknumber):
        """
        :param worknumber: 工号
        :return:

        """

        self.click(*self.element["按钮-员工管理"])
        sleep(3)
        self.click(*self.element["按钮-员工团队"])
        sleep(3)
        self.click(*self.element["按钮-入职"])
        sleep(3)
        self.click(*self.element["按钮-新员工入职审批"])
        self.await_element(*self.element["按钮-高级查询"])
        self.click(*self.element["按钮-高级查询"])
        sleep(5)
        self.await_element(*self.element["输入框-工号（高级查询）"])
        self.send_keys(worknumber, *self.element["输入框-工号（高级查询）"])
        self.click(*self.element["按钮-执行查询"])
        self.await_element(*self.element["文本-审批状态"])

        #获取审批状态文本
        check_text = self.element_text(*self.element["文本-审批状态"])
        return check_text

