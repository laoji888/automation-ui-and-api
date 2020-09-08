# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 人力自助平台待办页面》审批待办



from common.basePage import BasePage
from time import sleep






class ToDoPage(BasePage):


    # 读取todo_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("todo_page", file_name="hr/hr_self_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver





    # 审批待办
    def examinationapprovaltodo(self):
        self.await_element(*self.element["链接-待办"])
        self.click(*self.element["链接-待办"])
        self.await_element(*self.element["链接-新员工入职"])
        self.click(*self.element["链接-新员工入职"])
        self.await_element(*self.element["链接-第一条审批记录"])
        #获取审批数据的名称
        check_name = self.element_text(*self.element["验证点-名称"])
        self.click(*self.element["链接-第一条审批记录"])
        #sleep(3)
        #获取工号
        #worknumber = self.execute_js('return document.getElementById("el102").value;')
        sleep(3)
        self.execute_js("document.getElementsByClassName('application-container OVERFLOW_AUTO')[1].scrollTop=1000;")
        sleep(3)
        self.click(*self.element["下拉框-审批结果"])
        self.await_element(*self.element["按钮-审批结果》通过"])
        self.click(*self.element["按钮-审批结果》通过"])
        self.click(*self.element["按钮-提交"])

        #获取提交后弹窗文本值
        self.await_element(*self.element["验证点-操作成功"])
        check_text = self.element_text(*self.element["验证点-操作成功"])
        return check_name, check_text,

