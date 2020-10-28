# -*- coding: utf-8 -*-
# @Date      : 2020-05-27
# @Author  : 纪亚男
# Sample场景： 运行百度测试场景
import multiprocessing
import time
import warnings
import unittest
from pageObject.web.baidu.baidu_home import BaiduHome
from common.driver import Driver
from common.util import get_config_info


class TestBaidu:
    # @multiprocess
    def test_home(self,browser):
        warnings.simplefilter("ignore", ResourceWarning)
        browser = Driver(browser=browser, system="baidu")
        self.driver = browser.driver
        self.log = browser.log
        self.driver_home = BaiduHome(self.driver, self.log)
        self.driver_home.search("java")
        time.sleep(5)
        browser.quit_browser()

if __name__ == '__main__':
    dict = get_config_info("web", filename="devices_info.ini")
    print(dict)
    for k, v in dict.items():
        print(v)
        p = multiprocessing.Process(target=TestBaidu().test_home, args=(v,))
        p.start()

