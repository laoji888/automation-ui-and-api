import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.util import get_config_info

def driver(section,appName):
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

    driver = webdriver.Remote(capabilities["appium"], capabilities)
    return driver


if __name__ == '__main__':
    from selenium.webdriver.support import expected_conditions as EC
    d = driver("夜神","boss")
    try:
        WebDriverWait(d, 20).until(EC.visibility_of_element_located((By.ID,"com.hpbr.bosszhipin:id/iv_tab_4")))
        print("等待元素成功")
    except Exception as e:
        print(e)
    d.find_element(By.ID,"com.hpbr.bosszhipin:id/iv_tab_4").click()
    d.get_clipboard_text()
    time.sleep(5)


