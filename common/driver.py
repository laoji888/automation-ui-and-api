# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 选择并启动对应的浏览器
import os
import time
from selenium import webdriver

from common import path
from common.util import get_config_info
from common.logger import log



class Driver():
    """
    启动浏览器
    利用get_config_info方法读取url地址和执行机信息，先判断要启动的浏览器类型在启动对应的浏览器,
    关闭浏览器需要调用driver_quit方法
    ps:要在config下的configInfo下配置执行机的ip
    """

    def __init__(self, browser="null", device="null", system="null", timeout=30):
        """
    初始化driver类,以下参数需要在config目录下的配置文件中配置
        :param browser: 要启动的浏览器类型
        :param device: 移动端执行机
        :param system: 要启动的系统
        :param timeout: 超时时间
        """
        self.device = device
        self.system = system
        self.log = ""
        self.browser = browser
        self.driver = ""
        self.timeout = timeout
        self.type()

    def type(self):
        if self.device != "null":
            self.log = log(logname=self.device + "-" + self.system, system=self.system)
        else:
            self.log = log(logname=self.browser + "-" + self.system, system=self.system)
        if self.browser != "null":
            self.browser_type()
            self.open_browser()
        else:
            # 执行机信息
            capabilities = get_config_info(self.device, key=None, filename="devices_info.ini")
            # 应用信息
            app = get_config_info(self.system, key=None, filename="app_info.ini")
            capabilities['appPackage'] = app["appPackage"]
            capabilities['appActivity'] = app["appActivity"]
            from appium import webdriver
            self.driver = webdriver.Remote(get_config_info("appiumGrid", key="host", filename="config.ini"),
                                      capabilities)


    def browser_type(self):
        """
    根据参数“browser”判断要启动的执行机的类型后启动对应的执行机
        """
        if self.browser == "firefox":
            option = webdriver.FirefoxProfile()
            # 其中plugin.state.flash后的数值可以为0,1,2； 0：禁止，1：询问，2：允许。
            option.set_preference('plugin.state.flash', 2)
            self.host = get_config_info("seleniumGrid", "host")
            self.driver = webdriver.Remote(command_executor=self.host,
                                           desired_capabilities={'platform': 'ANY',
                                                                 'browserName': 'firefox',
                                                                 'version': "",
                                                                 'javascriptEnabled': True
                                                                 },
                                           browser_profile=option
                                           )
        elif self.browser == "ie":
            self.host =get_config_info("seleniumGrid", "host")
            self.driver = webdriver.Remote(command_executor=self.host,
                                           desired_capabilities={'platform': 'ANY',
                                                                 'browserName': 'internet explorer',
                                                                 'version': "",
                                                                 'javascriptEnabled': True
                                                                 }
                                           )
        elif self.browser == "chrome":
            self.host = get_config_info("seleniumGrid", "host")
            self.driver = webdriver.Remote(command_executor=self.host,
                                           desired_capabilities={'platform': 'ANY',
                                                                 'browserName': 'chrome',
                                                                 'version': "",
                                                                 'javascriptEnabled': True
                                                                 }
                                           )
        else:
            pass

    def open_browser(self):
        """
    打开URL设置窗口最大化并等待全部元素加载完成
        """
        self.driver.get(get_config_info(self.system, "URL"))
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def quit_browser(self):
        """
    关闭driver
        """
        self.driver.quit()


if __name__ == '__main__':
    dr = Driver("firefox", "baidu")
    from time import sleep

    sleep(3)
    dr.quit_browser()
