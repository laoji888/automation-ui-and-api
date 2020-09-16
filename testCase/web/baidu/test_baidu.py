# -*- coding: utf-8 -*-
# @Date      : 2020-05-27
# @Author  : 纪亚男
# Sample场景： 运行百度测试场景

import warnings
import unittest
from common import path
from pageObject.baidu.baidu_home import BaiduHome
from common.driver_web import Driver_web
from common.logger import log

class TestBaidu(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.browser = Driver_web("firefox", "baidu")
        self.log = log("baidutest")


    def test_home(self):
        self.driver = self.browser.driver
        self.driver_home = BaiduHome(self.driver, self.log)
        self.driver_home.search("java")


    def tearDown(self):
        self.browser.quit_browser()

if __name__ == '__main__':
    unittest.main()
