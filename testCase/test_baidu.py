# -*- coding: utf-8 -*-
# @Date      : 2020-05-27
# @Author  : 纪亚男
# Sample场景： 运行百度测试场景

import warnings
import unittest
from BeautifulReport import BeautifulReport
from common import path
from pageObject.baidu.baidu_home import BaiduHome
from common.driver import Driver
from common.baseTest import BaseTest
from common.logger import log


# 继承unittest框架
class TestBaidu(BaseTest):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.browser = Driver("firefox", "baidu",
                "Jiyn_firefox", "pms_host")
        self.log = log("baidutest")

    def save_img(self, img_name):  # 错误截图方法
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(path.IMG_DIR, img_name))

    # 这是一个场景，是把objects下某个系统的单个功能点串起来形成一个场景，启动下一个driver前需要把上一个driver关掉
    @BeautifulReport.add_test_img("test_home")
    def test_home(self):
        '''百度测试场景'''
        self.driver = self.browser.driver
        self.driver_home = BaiduHome(self.driver, self.log)
        #self.driver_home.screenshot("baidu.png")
        self.driver_home.search("java")
        self.driver_home.set()


    def tearDown(self):
        self.browser.quit_browser()



if __name__ == '__main__':
    unittest.main()
