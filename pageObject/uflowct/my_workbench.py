# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# 服务工单我的工作台页面下的功能封装

import time
from common import basePage
from time import sleep
from unittest import TestCase as t


# 封装我的工作台页面下的功能
class MyWorkbench(basePage.BasePage):

    def __init__(self, driver, log):
        """
    初始化元素信息
        :param driver: 浏览器对象
        """

        self.my_backlog_page = self.element_info("my_backlog_page",
                                                 file_name="uflowct/uflowct.xlsx")
        self.my_unified_issue_page = self.element_info("unified_issue_page",
                                                       file_name="uflowct/uflowct.xlsx")
        super().__init__(driver, log, self.my_unified_issue_page)

    def search_workOrder(self, workOrder_number=None, title=None):
        """
    我的工作台下的搜索工单功能
        :param workOrder_number: 工单编号
        :param title: 工单标题
        """
        if workOrder_number == None:
            self.send_keys(title, *self.my_backlog_page["输入框-工单标题(搜索)"])
            self.click(*self.my_backlog_page["按钮-查询（搜索）"])
            sleep(10)
        elif title == None:
            self.send_keys(workOrder_number, *self.my_backlog_page["输入框-工单编号(搜索)"])
            self.click(*self.my_backlog_page["按钮-查询（搜索）"])
            sleep(10)

    def workOrder_number(self):
        """
    获取工单编号
        :return:
        """
        sleep(2)
        number = self.element_text(*self.my_backlog_page["文本-工单编号"])
        self.log.info("获取到的文本信息是{}".format(number))
        return number

    def verification_status(self, status):
        """
    验证工单状态
        :param status: 预期状态
        """
        self.workOrder_status = self.element_text(*self.my_backlog_page["校验点-订单状态"])
        t.assertIn(self, status, self.workOrder_status)
        self.log.info("工单状态验证通过，状态是{}".format(status))

    def enter_info_page(self, workOrder_number):
        """
    进入我的代办下的第一条数据详情页，并切换到此窗口下
        :param workOrder_number: 预期工单编号
        """
        self.click(*self.my_backlog_page["检验点-工单标题"])
        sleep(1)
        self.switch_to_window()
        number = self.element_text(*self.my_backlog_page["校验点-审核页面工单编号"])
        t.assertIn(self, workOrder_number, number)
        self.log.info("进入工单编号为{}的详情页成功".format(number))

    def commit_and_verification(self):
        """
    审批后点击提交按钮并验证是否成功
        """
        self.click(*self.my_backlog_page["按钮-提交"])
        result = self.element_text(*self.my_backlog_page["校验点-提交成功"])
        t.assertIn(self, "成功", result)
        self.click(*self.my_backlog_page["按钮-提交后的确定"])
        self.switch_to_window(num=0)
        self.log.info("点击提交并验证成功")

    def verification_workOrder_info(self, title, introducer, task, mode, name):
        """
    验证工单信息

        :param title: 工单标题
        :param introducer: 提出人
        :param task: 当前任务
        :param mode: 所属模块
        :param name: 流程名称
        """
        self.title = self.element_text(*self.my_backlog_page["检验点-工单标题"])
        self.introducer = self.element_text(*self.my_backlog_page["校验点-提出人"])
        self.mode = self.element_text(*self.my_backlog_page["校验点-涉及模块"])
        self.name = self.element_text(*self.my_backlog_page["校验点-流程名称"])
        self.task = self.element_text(*self.my_backlog_page["校验点-当前任务"])
        t.assertIn(self, title, self.title)
        t.assertIn(self, introducer, self.introducer)
        t.assertIn(self, task, self.task)
        t.assertIn(self, mode, self.mode)
        t.assertIn(self, name, self.name)
        self.log.info("工单信息验证成功")

    def demand_audit(self, workOrder_code):
        """
    需求审核功能（新建需求工单）
        :param workOrder_code: 预期工单编号
        """
        self.workOrder_code = self.element_text(*self.my_backlog_page["校验点-审核页面工单编号"])
        t.assertIn(self, workOrder_code, self.workOrder_code)
        self.send_keys("通过", *self.my_backlog_page["输入框-审核说明"])
        self.log.info("需求审核通过")

    def demand_analyze(self):
        """
    需求分析功能（新建需求工单）
        """
        self.scroll_into_element(*self.my_backlog_page["单选框-是否同时上线（是）"])
        self.click(*self.my_backlog_page["单选框-是否同时上线（是）"])
        self.click(*self.my_backlog_page["下拉框-版本类型"])
        self.click(*self.my_backlog_page["按钮-版本类型》日常版本"])
        self.click(*self.my_backlog_page["下拉框-计划上线时间"])
        self.click(*self.my_backlog_page["按钮-计划上线时间》第一个选项"])
        self.log.info("需求分析通过")

    def exploit_plan(self):
        """
    制定开发测试计划（新建需求工单）
        """
        # 计划开发开始时间
        sleep(2)
        js = "document.documentElement.scrollTop=600"
        self.execute_js(js)
        self.click(*self.my_backlog_page["时间-计划开发开始时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期一"])
        # 计划开发完成时间
        self.click(*self.my_backlog_page["时间-计划开发完成时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期二"])
        self.click(*self.my_backlog_page["按钮-时间控件确定"])
        # 计划测试完成时间
        self.click(*self.my_backlog_page["时间-计划测试完成时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期三"])
        self.click(*self.my_backlog_page["按钮-时间控件确定"])
        # 输入任务详情
        self.send_keys("开发需求", *self.my_backlog_page["输入框-任务详情"])
        self.log.info("制定开发计划成功")

    def execute_exploit_test(self):
        """
    执行开发测试（新建需求工单）
        """
        sleep(2)
        js = "document.documentElement.scrollTop=600"
        # 输入实际开发开始时间
        self.click(*self.my_backlog_page["时间-实际开发开始时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期一"])
        self.click(*self.my_backlog_page["按钮-时间控件确定"])
        # 输入实际开发完成时间
        self.click(*self.my_backlog_page["时间-实际开发完成时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期二"])
        self.click(*self.my_backlog_page["按钮-时间控件确定"])
        # 输入测试完成时间
        self.click(*self.my_backlog_page["时间-实际测试完成时间"])
        self.select(6, *self.my_backlog_page["下拉框-年份（6是2021年）"])
        self.click(*self.my_backlog_page["按钮-第二周的星期三"])
        self.click(*self.my_backlog_page["按钮-时间控件确定"])
        # 输入其他信息
        self.send_keys("100%", *self.my_backlog_page["输入框-当前开发完成比例"])
        self.send_keys("100%", *self.my_backlog_page["输入框-当前测试完成比例"])
        self.send_keys("100%", *self.my_backlog_page["输入框-当前开发完成情况"])
        self.send_keys("100%", *self.my_backlog_page["输入框-当前测试完成情况"])
        self.send_keys("开发任务分配说明", *self.my_backlog_page["输入框-开发任务分配说明"])
        self.send_keys("测试任务分配说明", *self.my_backlog_page["输入框-测试任务分配说明"])
        self.send_keys("无", *self.my_backlog_page["输入框-存在的风险和及应对"])
        self.log.info("执行开发测试成功")

    def exploit_packaging(self, number, planname):
        """
    开发打包（新建需求工单）
        :param number: 工单编号
        :param planname: 计划名称
        """
        sleep(2)
        self.execute_js("document.documentElement.scrollTop=1000")
        # 创建计划
        self.click(*self.my_unified_issue_page["按钮-添加"])
        self.click(*self.my_unified_issue_page["下拉框-涉及模块"])
        self.click(*self.my_unified_issue_page["按钮-涉及模块》4A管理"])
        self.click(*self.my_unified_issue_page["时间-预计上线时间"])
        self.select(6, *self.my_unified_issue_page["下拉框-年份"])
        self.click(*self.my_unified_issue_page["按钮-第二周的星期一"])
        self.click(*self.my_unified_issue_page["按钮-时间控件确定"])
        self.send_keys(planname, *self.my_unified_issue_page["输入框-计划名称"])
        self.click(*self.my_unified_issue_page["按钮-确定"])
        name = self.element_text(*self.my_unified_issue_page["校验点-计划创建成功"])
        t.assertIn(self, "成功", name)
        self.click(*self.my_unified_issue_page["按钮-确定"])
        self.send_keys(planname, *self.my_unified_issue_page["输入框-计划名称搜索框"])
        self.click(*self.my_unified_issue_page["按钮-查询"])
        sleep(1)
        self.click(*self.my_unified_issue_page["单选框-筛选后的计划"])
        self.send_keys("即将停服", *self.my_unified_issue_page["输入框-停服时间及影响"])
        self.send_keys("升级内容", *self.my_unified_issue_page["输入框-升级内容"])
        ele = "//*[text()='" + number + "']/../../td/input"
        self.driver.find_element_by_xpath(ele).click()
        self.click(*self.my_unified_issue_page["按钮-添加(开发打包)"])
        # 上传附件
        self.click(*self.my_unified_issue_page["按钮-上传附件1"])
        self.input_file_upload("pms_upload/aa.py",
                               *self.my_unified_issue_page["input上传-上传附件"])
        self.input_file_upload("pms_upload/excell.xlsx",
                               *self.my_unified_issue_page["input上传-上传附件"])
        self.input_file_upload("pms_upload/test.py",
                               *self.my_unified_issue_page["input上传-上传附件"])
        self.input_file_upload("pms_upload/file1.txt",
                               *self.my_unified_issue_page["input上传-上传附件"])
        sleep(1)
        self.click(*self.my_unified_issue_page["按钮-确定"])
        # 修改上传的附件类型
        self.click(*self.my_unified_issue_page["按钮-修改1"])
        self.select(1, *self.my_unified_issue_page["下拉框-上线功能说明"])
        self.click(*self.my_unified_issue_page["按钮-修改1"])
        self.click(*self.my_unified_issue_page["按钮-修改2"])
        self.select(2, *self.my_unified_issue_page["下拉框-操作手册"])
        self.click(*self.my_unified_issue_page["按钮-修改2"])
        self.click(*self.my_unified_issue_page["按钮-修改3"])
        self.select(3, *self.my_unified_issue_page["下拉框-操作控制表"])
        self.click(*self.my_unified_issue_page["按钮-修改3"])
        self.click(*self.my_unified_issue_page["按钮-提交测试审核"])
        self.click(*self.my_unified_issue_page["下拉框-下一审批人"])
        self.click(*self.my_unified_issue_page["按钮-下一审批人》于贵发"])
        self.click(*self.my_unified_issue_page["按钮-确定"])
        result = self.element_text(*self.my_unified_issue_page["校验点-提交测试后"])
        t.assertIn(self, "成功", result)
        self.click(*self.my_unified_issue_page["按钮-确定"])
        self.log.info("开发打包成功")

    def test_audit(self, planName):
        """
    测试审核
        :param planName:计划名称
        """
        self.mouse_hover(*self.my_unified_issue_page["按钮-上线发布（页面）"])
        self.click(*self.my_unified_issue_page["按钮-测试审核"])
        self.send_keys(planName, *self.my_unified_issue_page["输入框-上线计划名称搜索框"])
        self.click(*self.my_unified_issue_page["按钮-查询"])
        self.click(*self.my_unified_issue_page["单选框-筛选后的计划"])
        self.send_keys("同意", *self.my_unified_issue_page["输入框-审核意见"])

        # 删除class=pxtab的div标签，解决页面布局显示不完全问题
        self.execute_js("$('.pxtab').remove()")
        sleep(2)
        self.select(1, *self.my_unified_issue_page["下拉框-审核结果"])
        self.click(*self.my_unified_issue_page["按钮-提交"])
        self.click(*self.my_unified_issue_page["下拉框-上线发布人"])
        self.click(*self.my_unified_issue_page["按钮-上线发布人》张佳鑫"])
        self.click(*self.my_unified_issue_page["按钮-确定"])
        sleep(1)
        result = self.element_text(*self.my_unified_issue_page["校验点-提交测试后"])
        t.assertIn(self, "成功", result)
        self.click(*self.my_unified_issue_page["按钮-确定"])
        self.log.info("测试审核成功")

    def issue(self, planName):
        """
    上线发布
        :param planName: 计划名称
        """
        self.click(*self.my_unified_issue_page["按钮-上线发布（页面）"])
        self.send_keys(planName, *self.my_unified_issue_page["输入框-上线计划名称搜索框"], timeput=60)
        self.click(*self.my_unified_issue_page["按钮-查询"])
        self.click(*self.my_unified_issue_page["单选框-筛选后的计划"])
        self.click(*self.my_unified_issue_page["时间-实际上线时间"])
        self.select(6, *self.my_unified_issue_page["下拉框-实际上线时间年份"])
        self.click(*self.my_unified_issue_page["按钮-第二周的星期一"])
        self.click(*self.my_unified_issue_page["按钮-时间控件确定"])
        self.send_keys("上线", *self.my_unified_issue_page["输入框-上线说明"])
        self.click(*self.my_unified_issue_page["选择框-本次上线的需求"])
        self.click(*self.my_unified_issue_page["按钮-添加需求"])
        self.click(*self.my_unified_issue_page["单选框-测试报告"])

        # 删除class=pxtab的标签，解决页面布局显示不完全问题
        self.execute_js("$('.pxtab').remove()")

        self.select(1, *self.my_unified_issue_page["下拉框-审核结果1"])
        self.select(1, *self.my_unified_issue_page["下拉框-审核结果2"])
        self.click(*self.my_unified_issue_page["按钮-上线发布(提交)"])
        result = self.element_text(*self.my_unified_issue_page["校验点-计划创建成功"])
        t.assertIn(self, "成功", result)
        self.click(*self.my_unified_issue_page["按钮-确定"])
        self.log.info("上线发布成功")
    def affirm(self):
        """
    提出者确认
        """
        self.send_keys("已确认", *self.my_unified_issue_page["输入框-说明"])
        self.log.info("提出者确认成功")
