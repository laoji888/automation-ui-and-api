# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 选择并启动对应的浏览器

from selenium import webdriver
from common.util import get_config_info


class Driver_web():
    """
    启动浏览器
    利用get_config_info方法读取url地址和执行机信息，先判断要启动的浏览器类型在启动对应的浏览器,
    关闭浏览器需要调用driver_quit方法
    ps:要在config下的configInfo下配置执行机的ip
    """

    def __init__(self, browser, system, section, key, timeout=30):
        """
    初始化driver类
        :param browser: 要启动的浏览器类型
        :param system: 要打开的系统（配置文件中的section）
        :param section: 要启动的执行机（配置文件中的section）
        :param key: 要启动的执行机IP和端口（配置文件中的key）
        :param timeout: 超时时间
        """
        self.url = get_config_info(system, "URL")
        self.browser = browser
        self.driver = " "
        self.section = section
        self.key = key
        self.timeout = timeout
        self.browser_type()
        self.open_browser()

    def browser_type(self):
        """
    根据参数“browser”判断要启动的执行机的类型后启动对应的执行机
        """
        if self.browser == "firefox":
            option = webdriver.FirefoxProfile()
            # 其中plugin.state.flash后的数值可以为0,1,2； 0：禁止，1：询问，2：允许。
            option.set_preference('plugin.state.flash', 2)
            self.host = 'http://' + get_config_info(self.section, self.key) + '/wd/hub'
            self.driver = webdriver.Remote(command_executor=self.host,
                                           desired_capabilities={'platform': 'ANY',
                                                                 'browserName': 'firefox',
                                                                 'version': "",
                                                                 'javascriptEnabled': True
                                                                 },
                                           browser_profile=option
                                           )
        elif self.browser == "ie":
            self.host = 'http://' + get_config_info(self.section, self.key) + '/wd/hub'
            self.driver = webdriver.Remote(command_executor=self.host,
                                           desired_capabilities={'platform': 'ANY',
                                                                 'browserName': 'internet explorer',
                                                                 'version': "",
                                                                 'javascriptEnabled': True
                                                                 }
                                           )
        elif self.browser == "chrome":
            self.host = 'http://' + get_config_info(self.section, self.key) + '/wd/hub'
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
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def quit_browser(self):
        """
    关闭driver
        """
        self.driver.quit()


if __name__ == '__main__':
    dr = Driver_web("firefox")
    from time import sleep

    sleep(120)
    dr.quit_browser()
