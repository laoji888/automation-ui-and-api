# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# Sample用例：统一业务平台—联通需求批次审批，该场景展示了 场景执行前初始化SQL操作、执行IE浏览器和调用autoit脚本

import os, unittest
from BeautifulReport import BeautifulReport
from common.baseTest import BaseTest
from common.driver import Driver
from common.database import operation_oracle
from common.logger import log
from pageObject.portal import *
from common import path


class TestCHUDReq(unittest.TestCase):

    @classmethod
    def  setUpClass(cls):
        cls.log = log(logname="统一业务平台—联通需求批次审批")

    def setUp(self):
        self.browser = Driver("ie", "Portal", "Mawj_ie", "portal_host", 10)

    def save_img(self, img_name):  # 错误截图方法
        """
        截图方法，当场景出现异常时会调用此方法进行截图
        :param img_name: 图片名称
        :return:
        """
        # 如果错误截图目录不存在，则自动创建一个screenshots目录
        if not os.path.exists(path.IMG_DIR): os.mkdir(path.IMG_DIR)

        # 保存截图到screenshots下
        self.driver.get_screenshot_as_file('{}/{}.png'.format(path.IMG_DIR,img_name))

    # 联通需求批次录入
    @BeautifulReport.add_test_img("test_001_build")
    def test_001_build(self):
        """
        新增联通批次审批需求
        """
        # 删除历史数据
        operation_oracle(self.log, "delete from batch_main_t where batch_code='2020LSD100100'",
                         databaseInfo="Portal_Oracle")

        # 启动配置文件指定的chrome执行机
        self.driver = self.browser.driver
        # 联通需求批次录入
        self.driver_loginpage = LoginPage(self.driver, self.log)
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_loginpage.login("lt_liqi", "1")
        username_check = self.driver_homepage.get_username()
        self.assertIn("李琪", username_check)  # 登录校验
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_homepage.demand_input()
        self.driver_demand_input = DemandInputPage(self.driver, self.log)
        self.driver_demand_input.demand_add("按钮-新增-室分类批次")
        self.driver_roomclass = RoomClassPage(self.driver, self.log)
        global ProNum  # 批次号
        ProNum = self.driver_roomclass.project_num()
        self.driver_roomclass.upload_attachment()
        self.driver_roomclass.upload_demand_plan()
        self.driver_roomclass.demand_commit()
        # 室分类需求提出校验(审批中)
        project_num_check, state_check = self.driver_demand_input.demand_state_check("按钮-室分类需求(建设方式)")
        self.assertEqual(project_num_check, ProNum)
        self.assertEqual(state_check, "审批中")

    # 运营商人员审批
    @BeautifulReport.add_test_img("test_002_approval")
    def test_002_approval(self):
        """
        运营商人员审批
        """
        # 启动配置文件指定的chrome执行机
        self.driver = self.browser.driver
        self.driver_loginpage = LoginPage(self.driver, self.log)
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_loginpage.login("lt_caoyan", "1")
        username_check = self.driver_homepage.get_username()
        self.assertIn("曹妍", username_check)  # 登录校验
        self.driver_homepage.my_handle()
        self.driver_handlepage = MyHandlePage(self.driver, self.log)
        self.driver_handlepage.handle_style("按钮-联通批次审批")
        self.driver_handlepage.CHU_reqapproval(ProNum)

    # 省份人员审批
    @BeautifulReport.add_test_img("test_003_approval")
    def test_003_approval(self):
        """
        省份人员审批
        """
        # 启动配置文件指定的chrome执行机
        self.driver = self.browser.driver
        self.driver_loginpage = LoginPage(self.driver, self.log)
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_loginpage.login("fujx", "1")
        username_check = self.driver_homepage.get_username()
        self.assertIn("付景新", username_check)  # 登录校验
        self.driver_homepage.my_handle()
        self.driver_handlepage = MyHandlePage(self.driver, self.log)
        self.driver_handlepage.handle_style("按钮-联通批次审批")
        self.driver_handlepage.CHU_reqapproval(ProNum)

    # 省份人员审批
    @BeautifulReport.add_test_img("test_004_approval")
    def test_004_approval(self):
        """
        省份人员审批
        """
        # 启动配置文件指定的chrome执行机
        self.driver = self.browser.driver
        self.driver_loginpage = LoginPage(self.driver, self.log)
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_loginpage.login("penghan", "1")
        username_check = self.driver_homepage.get_username()
        self.assertIn("彭晗", username_check)  # 登录校验
        self.driver_homepage.my_handle()
        self.driver_handlepage = MyHandlePage(self.driver, self.log)
        self.driver_handlepage.handle_style("按钮-联通批次审批")
        self.driver_handlepage.CHU_reqapproval(ProNum)
        self.driver_handlepage.refresh_page()
        # 室分类需求提出校验(审批通过)
        self.driver_homepage.demand_input()
        self.driver_demand_input = DemandInputPage(self.driver, self.log)
        project_num_check, state_check = self.driver_demand_input.demand_state_check("按钮-室分类需求(建设方式)")
        self.assertEqual(project_num_check, ProNum)
        self.assertEqual(state_check, "审批通过")
        self.driver_demand_input.screenshot("CHU_reqapproval.png")

    def tearDown(self):
        self.browser.quit_browser()


if __name__ == '__main__':
    unittest.main()
