# -*- coding: utf-8 -*-
# @Date      : 2020-05-27
# @Author  : 纪亚男
# Sample场景： 服务工单系统-新建需求工单场景

from pageObject.uflowct.home import Home
from pageObject.uflowct.my_workbench import MyWorkbench
from pageObject.uflowct.new_workOrder import NewWorkOrder
from time import sleep
import os, time
from BeautifulReport import BeautifulReport
from common.driver import Driver
from common.baseTest import BaseTest
from common import path
from common.logger import log


class TestNewDemandWorkOrder(BaseTest):

    def setUp(self):
        self.log = log(logname="服务工单")

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:图片名称
        """
        # 如果错误截图目录不存在，则自动创建一个screenshots目录
        if not os.path.exists(path.IMG_DIR): os.mkdir(path.IMG_DIR)

        # 保存截图到screenshots下
        self.dr["driver"].get_screenshot_as_file('{}/{}.png'.format(path.IMG_DIR, img_name))

    def browser(self, browsertype="chrome", systemurl="Uflowct",
                perform="Jiyn-chrome", perform_ip="uflowct_host"):
        """
    启动浏览器，返回object对象
        :param browsertype: 浏览器类型
        :param systemurl: 配置文件中的系统名（用于读取url地址）
        :param perform: 配置文件下浏览器名
        :param perform_ip: 配置文件下的浏览器IP对应的“键”
        :return: object
        """
        browser = Driver(browsertype, systemurl, perform, perform_ip)
        driver = browser.driver
        object = {"browser": browser, "driver": driver}
        return object

    def logi_and_enter_backlog(self, number, task,  t=0, **kwargs):
        """
    登录后进入我的待办，搜索工单后验证工单信息
        :param number: 工单编号
        :param task: 当前任务
        :param kwargs: 用户和浏览器信息
        """
        driver_home = Home(kwargs["driver"], self.log)
        driver_home.login(kwargs["username"], kwargs["passwd"], kwargs["name"],sleeptime=t)
        driver_home.enter_backlog()
        driver_my_workOrder = MyWorkbench(kwargs["driver"], self.log)
        driver_my_workOrder.search_workOrder(workOrder_number=number)
        sleep(3)
        # 验证工单信息
        driver_my_workOrder.verification_workOrder_info("自动化测试", "高珊", task, "4A管理", "需求管理流程")

    @BeautifulReport.add_test_img("test_001_new_demand_workOrder")
    def test_001_new_demand_workOrder(self):
        """
    新建需求工单场景
        """
        # 需求提出（高珊）
        self.dr = self.browser()
        self.driver_home = Home(self.dr["driver"], self.log)
        self.driver_home.login("gaoshan", "Ct#2018", "高珊")
        # 进入新建工单并填写信息后提交
        self.driver_home.enter_new_workOrder()
        self.driver_WorkOrder = NewWorkOrder(self.dr["driver"], self.log)
        self.driver_WorkOrder.enter_new_demand_workOrder()
        self.driver_WorkOrder.new_demand_workOrder("自动化测试", "需求工单")
        self.driver_home.switch_to_window(num=0)
        self.driver_home.enter_my_workOrder()
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        # 获取工单编号
        self.workOrder_number = self.driver_my_workOrder.workOrder_number()
        self.dr["browser"].quit_browser()
        self.log.info("高珊新建需求工单")

        # 需求审核（杨行波）
        self.dr = self.browser()
        # 登录后进入我的待办，搜索并验证工单信息
        data = {"driver": self.dr["driver"], "username": "yangxb3", "passwd": "Ct#2018", "name": "杨行波"}
        self.logi_and_enter_backlog(self.workOrder_number, "需求审核", **data)
        # 审核
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_my_workOrder.enter_info_page(self.workOrder_number)
        self.driver_my_workOrder.demand_audit(self.workOrder_number)
        self.driver_my_workOrder.commit_and_verification()
        # 退出当前浏览器
        self.dr["browser"].quit_browser()

        # 需求分析（杨兆刚）
        self.dr = self.browser()
        data = {"driver": self.dr["driver"], "username": "zb-yangzg", "passwd": "Ct#2018", "name": "杨兆刚"}
        self.logi_and_enter_backlog(self.workOrder_number, "需求分析", **data)
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_my_workOrder.enter_info_page(self.workOrder_number)
        self.driver_my_workOrder.demand_analyze()
        self.driver_my_workOrder.commit_and_verification()
        self.dr["browser"].quit_browser()

        # 制定开发测试计划
        self.dr = self.browser()
        data = {"driver": self.dr["driver"], "username": "zb-yangzg", "passwd": "Ct#2018", "name": "杨兆刚"}
        self.logi_and_enter_backlog(self.workOrder_number, "制定开发测试计划", **data)
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_my_workOrder.enter_info_page(self.workOrder_number)
        self.driver_my_workOrder.exploit_plan()
        self.driver_my_workOrder.commit_and_verification()
        self.dr["browser"].quit_browser()

        # 执行开发测试
        self.dr = self.browser()
        data = {"driver": self.dr["driver"], "username": "zb-yangzg", "passwd": "Ct#2018", "name": "杨兆刚"}
        self.logi_and_enter_backlog(self.workOrder_number, "执行开发测试", **data)
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_my_workOrder.enter_info_page(self.workOrder_number)
        self.driver_my_workOrder.execute_exploit_test()
        self.driver_my_workOrder.commit_and_verification()
        self.dr["browser"].quit_browser()

        # 开发终审（IE浏览器）
        self.dr = self.browser(browsertype="ie", systemurl="Uflowct",
                               perform="Jiyn-ie", perform_ip="uflowct_host")
        data = {"driver": self.dr["driver"], "username": "zb-yangzg", "passwd": "Ct#2018", "name": "杨兆刚"}
        self.logi_and_enter_backlog(self.workOrder_number, "开发终审", t=5, **data)
        self.driver_my_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_my_workOrder.enter_info_page(self.workOrder_number)
        sleep(2)
        self.driver_my_workOrder.commit_and_verification()
        self.dr["browser"].quit_browser()

        # 开发打包
        self.dr = self.browser()
        self.driver_home = Home(self.dr["driver"], self.log)
        self.driver_home.login("zb-yangzg", "Ct#2018", "杨兆刚")
        self.driver_home.enter_unified_issue()
        self.driver_workOrder = MyWorkbench(self.dr["driver"], self.log)
        planname = "4A管理" + time.strftime("%Y-%m-%d-%H-%M-%S")
        self.driver_workOrder.exploit_packaging(self.workOrder_number, planname)
        self.dr["browser"].quit_browser()

        # 测试审核
        self.dr = self.browser()
        self.driver_home = Home(self.dr["driver"], self.log)
        self.driver_home.login("yugf", "Ct#2018", "于贵发")
        self.driver_home.enter_unified_issue()
        self.driver_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_workOrder.test_audit(planname)
        self.dr["browser"].quit_browser()

        # 上线发布
        self.dr = self.browser()
        self.driver_home = Home(self.dr["driver"], self.log)
        self.driver_home.login("zb-zhangjx3", "Ct#2018", "张佳鑫")
        self.driver_home.enter_unified_issue()
        self.driver_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_workOrder.issue(planname)
        self.dr["browser"].quit_browser()

        # 提出人确认
        self.dr = self.browser()
        self.driver_home = Home(self.dr["driver"], self.log)
        self.driver_home.login("gaoshan", "Ct#2018", "高珊")
        self.driver_workOrder = MyWorkbench(self.dr["driver"], self.log)
        self.driver_home.enter_backlog()
        self.driver_workOrder.search_workOrder(workOrder_number=self.workOrder_number)
        self.driver_workOrder.enter_info_page(self.workOrder_number)
        self.driver_workOrder.affirm()
        self.driver_workOrder.commit_and_verification()
        # 跳转到我的工单页面
        self.driver_workOrder.execute_js("$('.menuul>li:eq(1)>ul>li:eq(1)')[0].click()")
        self.driver_workOrder.search_workOrder(workOrder_number=self.workOrder_number)
        self.driver_workOrder.verification_status("关闭")
        self.driver_workOrder.screenshot("新建需求工单最终截图")
        self.dr["browser"].quit_browser()

    def tearDown(self):
        try:
            self.dr["browser"].quit_browser()
        except Exception as e:
            pass


if __name__ == '__main__':
    pass
