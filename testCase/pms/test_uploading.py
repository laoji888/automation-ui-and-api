# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# Sample场景： pms文件上传场景

from pageObject.pms import *
from time import sleep
import os
from BeautifulReport import BeautifulReport
from common.driver import Driver
from common.baseTest import BaseTest
from common import path
from common.logger import log




class TestUploading(BaseTest):
    def setUp(self):
        self.log = log("pms")
        self.browser = Driver("firefox", "PMS", "Jiyn_firefox", "pms_host")

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

    # 这是一个场景，是把PageObject下某个页面的功能串起来形成一个场景，启动下一个driver前需要把上一个driver关掉
    @BeautifulReport.add_test_img("test_001_uploading")
    def test_001_uploading(self):
        '''pms非input上传场景'''
        # 启动配置文件指定的firefox执行机
        self.driver = self.browser.driver
        self.driver_pms = pms_home.PmsHome(self.driver,self.log)

        # 主动截图并把图片放到测试报告中
        # self.driver_pms.screenshot("001.png")

        self.driver_pms.login("wangyf5")
        self.driver_pms.enter_into_backlog()
        self.driver_pms.click_one()
        sleep(2)
        self.driver_pms.uploading("pms_upload/file.txt")

    def tearDown(self):
        self.browser.quit_browser()


if __name__ == '__main__':
    print(os.path.abspath("screenshots"))