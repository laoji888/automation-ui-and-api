import time
from appium import webdriver
from selenium.webdriver.common.by import By

from common.util import get_config_info

def driver(section,appInfo,callAddress):
    """
    :param appInfo: 配置文件中应用名
    :param callAddress: 调用地址
    :param section: 配置文件的节
    :return:
    """
    #执行机信息
    capabilities = get_config_info(section, key=None, filename="/devices_info.ini")
    #应用信息
    app = get_config_info(appInfo, key=None, filename="/app_info.ini")
    capabilities['appPackage'] = app["appPackage"]
    capabilities['appActivity'] = app["appActivity"]


    ip = get_config_info("mobile", key=callAddress, filename="/devices_info.ini")

    driver =  webdriver.Remote(ip, capabilities)
    return driver


if __name__ == '__main__':
    d = driver("夜神","boss","appium01")
    time.sleep(15)
    # d.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ImageView"
    # ).click()
    d.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/img_icon' and @class='android.widget.ImageView']").click()
    time.sleep(5)
    d.quit()


