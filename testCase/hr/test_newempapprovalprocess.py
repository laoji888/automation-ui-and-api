# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# Sample场景：人力资源管理系统-新员工入职审批流程（地市公司发起）


import os
import unittest
from BeautifulReport import BeautifulReport
from common.driver import Driver
from common.baseTest import BaseTest
import pageObject.hrms.hcm
import pageObject.hrms.selfservice
from common.logger import log



class NewEmpApprovalProcess(BaseTest):
    def setUp(self):
        self.browser = Driver("firefox","Business","Gaogd_firefox","hr_host")
        self.log = log(logname="人力资源管理系统")

    def save_img(self, img_name):  # 错误截图方法
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            "../screenshots"),
            img_name))  # os.path.abspath(r"screenshots")截图存放路径


    # @BaseTest.skipTest("跳过此用例")
    @BeautifulReport.add_test_img("test_1_Atoapplyfor")
    def test_001_Atoapplyfor(self):
        """
        新员工入职审批流程（地市公司发起）

        """
        # 启动配置文件指定的firefox执行机
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.hcm.HomePage(self.driver, self.log)
        # 登录人力业务平台
        check_name = self.driver_home.login("gaiqian", "ALECK1982UAT")
        # 校验登录用户名
        self.assertEqual(check_name, "盖倩")
        # 新员工入职审批》新建申请
        self.driver_Staffmanagement = pageObject.hrms.hcm.NewEmpApprovalPage(self.driver, self.log)
        # 校验弹窗文本
        check_text, worknumber = self.driver_Staffmanagement.induction("张三", "222", "19911013","a","13521328888")
        print(worknumber)
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开自助平台
        self.browser = Driver("firefox", "Self-service","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.selfservice.HomePage(self.driver, self.log)
        self.driver_todo = pageObject.hrms.selfservice.ToDoPage(self.driver, self.log)
        # 自助平台登录
        check_name = self.driver_home.login("gengyz", "ALECK1982UAT")
        #校验登录用户名
        self.assertIn("耿养宗", check_name)
        # 耿养宗审批待办
        check_name, check_text = self.driver_todo.examinationapprovaltodo()
        # 校验审批数据
        self.assertEqual(check_name, "张三新员工录用审批流程")
        # 校验弹窗文本
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开自助平台
        self.browser = Driver("firefox", "Self-service","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.selfservice.HomePage(self.driver, self.log)
        self.driver_todo = pageObject.hrms.selfservice.ToDoPage(self.driver, self.log)
        # 自助平台登录
        check_name = self.driver_home.login("jili", "ALECK1982UAT")
        # 校验用户名
        self.assertIn("纪莉", check_name)
        # 纪莉审批待办
        check_name, check_text = self.driver_todo.examinationapprovaltodo()
        # 校验审批数据
        self.assertEqual(check_name, "张三新员工录用审批流程")
        # 校验弹窗文本
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开自助平台
        self.browser = Driver("firefox", "Self-service","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.selfservice.HomePage(self.driver, self.log)
        self.driver_todo = pageObject.hrms.selfservice.ToDoPage(self.driver, self.log)
        # 自助平台登录
        check_name = self.driver_home.login("lichuang", "ALECK1982UAT")
        # 校验用户名
        self.assertIn("李创", check_name)
        # 李创审批待办
        check_name, check_text = self.driver_todo.examinationapprovaltodo()
        # 校验审批数据
        self.assertEqual(check_name, "张三新员工录用审批流程")
        # 校验弹窗文本
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开自助平台
        self.browser = Driver("firefox", "Self-service","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.selfservice.HomePage(self.driver, self.log)
        self.driver_todo = pageObject.hrms.selfservice.ToDoPage(self.driver, self.log)
        # 自助平台登录
        check_name = self.driver_home.login("zhangyan", "ALECK1982UAT")
        #校验用户名
        self.assertIn("张䶮", check_name)
        # 张䶮审批待办
        check_name, check_text = self.driver_todo.examinationapprovaltodo()
        # 校验审批数据
        self.assertEqual(check_name, "张三新员工录用审批流程")
        # 校验弹窗文本
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开自助平台
        self.browser = Driver("firefox", "Self-service","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.selfservice.HomePage(self.driver, self.log)
        self.driver_todo = pageObject.hrms.selfservice.ToDoPage(self.driver, self.log)
        # 自助平台登录
        check_name = self.driver_home.login("wangjg", "ALECK1982UAT")
        #校验用户名
        self.assertIn("王敬国", check_name)
        # 王敬国审批待办
        check_name, check_text = self.driver_todo.examinationapprovaltodo()
        print(type(worknumber))
        # 校验审批数据
        self.assertEqual(check_name, "张三新员工录用审批流程")
        # 校验弹窗文本
        self.assertEqual(check_text, "操作成功")
        # 关闭浏览器
        self.browser.quit_browser()
        # 打开业务平台
        self.browser = Driver("firefox", "Business","Gaogd_firefox","hr_host")
        self.driver = self.browser.driver
        self.driver_home = pageObject.hrms.hcm.HomePage(self.driver, self.log)
        self.driver_sm = pageObject.hrms.hcm.NewEmpApprovalPage(self.driver, self.log)
        # 盖倩登录业务平台
        check_name = self.driver_home.login("gaiqian", "ALECK1982UAT")
        #校验用户名
        self.assertEqual(check_name, "盖倩")
        # 校验审批状态
        check_text = self.driver_sm.check_approval_status(worknumber)
        self.assertEqual(check_text, "审批通过")
        #主动截图
        self.driver_sm.screenshot("test_newempapprovalprocess.png")





    def tearDown(self):
        self.browser.quit_browser()

if __name__ == '__main__':
    unittest.main()

