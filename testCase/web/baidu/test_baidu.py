# -*- coding: utf-8 -*-
# @Date      : 2020-05-27
# @Author  : 纪亚男
# Sample场景： 运行百度测试场景

import warnings
import unittest
from pageObject.web.baidu.baidu_home import BaiduHome
from common.driver import Driver
from common.util import multiprocess


class TestBaidu(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)



    @multiprocess
    def test_home(self,browser="firefox"):
        self.browser = Driver(browser=browser, system="baidu")
        self.driver = self.browser.driver
        self.log = self.browser.log
        self.driver_home = BaiduHome(self.driver, self.log)
        self.driver_home.search("java")
        self.browser.quit_browser()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
