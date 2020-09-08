# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# Sample场景：验证物业续签合同,执行此场景需要登录执行机远程桌面


import sys
sys.path.append("/python-script/UIAutomation_QM")
import os
import unittest
from BeautifulReport import BeautifulReport
from common.driver import Driver
from common.baseTest import BaseTest
import pageObject.cms
import pageObject.property
from common import path
from pageObject.property.synchronousdata import Synchronous_Data
from common.logger import log



class ThePropertyRenewalContract(BaseTest):



    def setUp(self):
        self.log = log(logname="合同系统运行日志")



    def save_img(self, img_name): # 错误截图方法
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # 如果错误截图目录不存在，则自动创建一个screenshots目录
        if not os.path.exists(path.IMG_DIR): os.mkdir(path.IMG_DIR)

        # 保存截图到screenshots下
        self.browser["driver"].get_screenshot_as_file('{}/{}.png'.format(path.IMG_DIR, img_name))

    #@unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_001_Amendingcontract")
    def test_001_Amendingcontract(self):
        """
        赵淑亚修改合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        self.drafit = pageObject.cms.DraftboxPage(self.driverie, self.log)

        #登录合同系统
        check_name = self.home_page.login("zhaosy", "wdPW.7L")
        #校验登录后用户名
        self.assertIn("赵淑亚", check_name)
        #合同流水号
        global Serialnumber
        Serialnumber = "GXNN2020000167"

        #修改物业推送过来的合同
        self.drafit.modification_contract(Serialnumber,"修改合同","2021-12-30","1","1","1","2020-12-26")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_002_fxaminationapproval")
    def test_002_fxaminationapproval(self):
        """
        李本松审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        #登录合同系统
        check_name = self.home_page.login("libs3", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("李本松", check_name)

        #审批
        self.todo.our_todo1(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_003_fxaminationapproval")
    def test_003_fxaminationapproval(self):
        """
        赵淑亚审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        #登录合同系统
        check_name = self.home_page.login("zhaosy", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("赵淑亚", check_name)

        #审批
        self.todo.our_todo2(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_004_fxaminationapproval")
    def test_004_fxaminationapproval(self):
        """
        宋日健审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        #登录合同系统
        check_name = self.home_page.login("songrj", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("宋日健", check_name)
        # 审批
        self.todo.our_todo3(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_005_fxaminationapproval")
    def test_005_fxaminationapproval(self):
        """
        孙传毅审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("suncy", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("孙传毅", check_name)
        # 审批
        self.todo.our_todo4(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_006_fxaminationapproval")
    def test_006_fxaminationapproval(self):
        """
        李庭婷审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("litt3", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("李庭婷", check_name)
        # 审批
        self.todo.our_todo5(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_007_fxaminationapproval")
    def test_007_fxaminationapproval(self):
        """
        罗俊强审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("luojq", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("罗俊强", check_name)
        # 审批
        self.todo.our_todo6(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_008_fxaminationapproval")
    def test_008_fxaminationapproval(self):
        """
        李本松审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("libs3", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("李本松", check_name)
        # 审批
        self.todo.our_todo7(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_009_fxaminationapproval")
    def test_009_fxaminationapproval(self):
        """
        李坚审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("lijian3", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("李坚", check_name)
        # 审批
        self.todo.our_todo8(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_010_fxaminationapproval")
    def test_010_fxaminationapproval(self):
        """
        沈风华审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("shenfh", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("沈风华", check_name)
        # 审批
        self.todo.our_todo9(Serialnumber, "审批")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_011_fxaminationapproval")
    def test_011_fxaminationapproval(self):
        """
        赵淑亚审批定稿

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("zhaosy", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("赵淑亚", check_name)
        #审批并获取合同编号
        global Contractno
        Contractno = self.todo.our_todo10(Serialnumber)

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_012_fxaminationapproval")
    def test_012_fxaminationapproval(self):
        """
        赵淑亚签订盖章

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("zhaosy", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("赵淑亚", check_name)
        # 审批
        self.todo.our_todo11(Serialnumber,"2")

    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_013_fxaminationapproval")
    def test_013_fxaminationapproval(self):
        """
        李本松审批合同

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "cms", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.todo = pageObject.cms.Todopage(self.driverie, self.log)
        self.home_page = pageObject.cms.Home_Page(self.driverie, self.log)
        # 登录合同系统
        check_name = self.home_page.login("libs3", "wdPW.7L")
        # 校验登录用户名
        self.assertIn("李本松", check_name)
        # 审批
        self.todo.our_todo12(Serialnumber, "审批")



    @unittest.skip("跳过此用例")
    @BeautifulReport.add_test_img("test_014_Synchronousdata")
    def test_014_Synchronousdata(self):
        """
        赵淑亚登录物业系统查询数据

        """
        # 启动远程的ie执行机
        self.browser = Driver("ie", "property", "Gaogd_ie", "cms_host")
        self.driverie = self.browser.driver
        self.home_page =pageObject.property.Home_Page(self.driverie, self.log)
        self.Contract_Management = pageObject.property.Contract_ManagementPage(self.driverie, self.log)
        self.Synchronous_Data = Synchronous_Data()
        check_name = self.home_page.login("zhaosy","000000")
        self.assertIn("赵淑亚", check_name)
        #get新url同步数据
        #self.home_page.Synchronous_data()
        #http请求同步数据
        self.Synchronous_Data.synchronousdata()
        #查询合同信息
        check_name = self.Contract_Management.the_query(Contractno)
        # 校验合同名称
        self.assertEqual(check_name, "修改合同")
        #主动截图
        self.Contract_Management.screenshot("test_newempapprovalprocess.png")


    def tearDown(self):
        self.browser.quit_browser()


if __name__ == '__main__':
    unittest.main()
