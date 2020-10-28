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
from common.util import *



@multiprocess
def test_home(browser1):
    warnings.simplefilter("ignore", ResourceWarning)
    browser = Driver(browser=browser1, system="baidu")
    driver = browser.driver
    log = browser.log
    driver_home = BaiduHome(driver, log)
    time.sleep(5)
    # driver_home.set()
    driver_home.search("java")
    browser.quit_browser()

if __name__ == '__main__':
    test_home()

