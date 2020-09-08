# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# Sample用例：规划系统-塔类需求整合，该场景展示了 数据库操作 和 通过URL打开网页对话框

import os
from BeautifulReport import BeautifulReport
from common.baseTest import BaseTest
from common.logger import log
from common.driver import Driver
from pageObject.tapweb import *
from pageObject.oa import *
from common import path


class TestReqIntegration(BaseTest):

    @classmethod
    def  setUpClass(cls):
        cls.log = log(logname="规划系统-塔类需求整合")

    def setUp(self):
        self.browser = Driver("chrome", "OA", "Mawj-chrome", "tapweb_host", 10)

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

    # 需求整合
    @BeautifulReport.add_test_img("test_001_demand_integration")
    def test_001_demand_integration(self):
        """
        通过SQL操作完成flash需求整合
        """
        # 启动配置文件指定的chrome执行机
        self.driver = self.browser.driver

        # 从OA进入规划系统
        self.driver_loginpage = LoginPage(self.driver, self.log)
        self.driver_homepage = HomePage(self.driver, self.log)
        self.driver_loginpage.login("lining5", "1qaz@WSX")
        self.driver_homepage.into_operation_management()
        username_check = self.driver_homepage.get_username()
        self.assertIn("李宁", username_check)   # 登录校验
        self.driver_integrationpage = SystemPage(self.driver, self.log)
        self.driver_integrationpage.get_into_system("按钮-资产形成","按钮-规划支撑")

        #需求整合
        # self.driver_loginpage = LoginPage(self.driver)
        # self.driver_loginpage.login("lining5", "zTerEs@0925")
        self.driver_homepage = HomebPage(self.driver, self.log)
        # 进入需求整合页面
        self.driver_homepage.get_into_requirement_integration()
        self.driver_integrationpage = ReqIntegrationPage(self.driver, self.log)
        # 获取需求编码并通过SQL进行需求整合
        req_id = self.driver_integrationpage.get_requirement_id()
        self.driver_integrationpage.demand_integrate(req_id)
        self.driver_integrationpage.tower_requirement()
        self.tapweb_demandpage = TowerIntegrationPage(self.driver, self.log)
        # 校验SQL需求整合整合是否成功
        self.tapweb_demandpage.req_search(req_id)
        demand_id_check = self.tapweb_demandpage.get_requirement_id()
        self.assertEqual(demand_id_check, req_id)
        self.tapweb_demandinfopage = ReqInfoPage(self.driver, self.log)
        # 编辑整合详情
        self.tapweb_demandinfopage.tower_req(req_id)
        self.tapweb_demandinfopage.screenshot("req_integrate.png")

    def tearDown(self):
        self.browser.quit_browser()


# if __name__ == '__main__':
#     unittest.main()


