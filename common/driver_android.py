import time
from appium import webdriver
from common.util import get_config_info

def driver(section,appInfo,callAddress):
    """
    :param appInfo: 配置文件中应用名
    :param callAddress: 调用地址
    :param section: 配置文件的节
    :return:
    """
    #执行机信息
    capabilities = get_config_info(section, key=None, filename="/devicesInfo")
    #应用信息
    app = get_config_info(appInfo, key=None, filename="/appInfo")
    capabilities['appPackage'] = app["appPackage"]
    capabilities['appActivity'] = app["appActivity"]

    ip = get_config_info("mobile", key=callAddress, filename="/devicesInfo")

    driver =  webdriver.Remote(ip, capabilities)
    return driver


if __name__ == '__main__':
    d = driver("夜神","腾讯新闻","loction")
    time.sleep(5)
    d.quit()


