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

class TestBaidu():
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.browser = Driver_web("firefox", "baidu1",
                "Jiyn_firefox", "host")
        self.log = log("baidutest")


    # 这是一个场景，是把objects下某个系统的单个功能点串起来形成一个场景，启动下一个driver前需要把上一个driver关掉
    def test_home(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.browser = Driver_web("firefox", "bd",
                                  "Jiyn_firefox", "host")
        self.log = log("baidutest")
        '''百度测试场景'''
        self.driver = self.browser.driver
        self.driver_home = BaiduHome(self.driver, self.log)
        #self.driver_home.screenshot("baidu.png")
        self.driver_home.search("java")
        # self.driver_home.set()


    def tearDown(self):
        self.browser.quit_browser()



if __name__ == '__main__':
    TestBaidu().test_home()
