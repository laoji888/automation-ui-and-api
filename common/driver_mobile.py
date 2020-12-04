


import sys ,re, xlrd, requests, time
sys.path.append("/root/.jenkins/workspace/autotest")
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.util import get_config_info


def driver(section,appName,url="http://127.0.0.1:4444/wd/hub"):
    """
    :param appInfo: 配置文件中应用名
    :param callAddress: 调用地址
    :param section: 配置文件的节(执行机信息)
    :return:
    """
    #执行机信息
    capabilities = get_config_info(section, key=None, filename="/devices_info.ini")
    #应用信息
    app = get_config_info(appName, key=None, filename="/app_info.ini")
    capabilities['appPackage'] = app["appPackage"]
    capabilities['appActivity'] = app["appActivity"]

    driver = webdriver.Remote(url, capabilities)
    return driver


if __name__ == '__main__':

    d = driver("mumu","腾讯新闻")
    time.sleep(5)
    d.quit()


