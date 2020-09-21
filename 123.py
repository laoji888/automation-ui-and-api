import time

# from selenium import webdriver
#
# driver = webdriver.Remote(command_executor='http://192.168.31.111:8888/wd/hub',
#                                            desired_capabilities={'platform': 'ANY',
#                                                                  'browserName': 'firefox',
#                                                                  'version': "",
#                                                                  'javascriptEnabled': True
#                                                                  })
# driver.get("http://www.baidu.com")
# time.sleep(5)
# driver.quit()

#执行机信息
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from common.util import get_config_info
from common.base_mobile import  Base_mobile
from common.logger import log

capabilities = get_config_info("mumu", key=None, filename="/devices_info.ini")
#应用信息
app = get_config_info("邮箱大师", key=None, filename="/app_info.ini")
capabilities['appPackage'] = app["appPackage"]
capabilities['appActivity'] = app["appActivity"]

#获取执行机调用地址
ip = get_config_info("mobile", key="appium01", filename="/host_config.ini")

driver =  webdriver.Remote(ip, capabilities)
time.sleep(5)
loger = log("123")
Base_mobile(driver,log=loger).swipe_bottom("com.netease.mail:id/mail_list_item_from")
time.sleep(5)
driver.quit()
# swaile = True
# while(swaile):
#     #滑动前元素列表
#     list1 = driver.find_elements_by_id("com.netease.mail:id/mail_list_item_from")
#     #最后一个元素信息
#     info1 = list1[-1].text
#
#     driver.swipe(500, 600, 500, 300)
#     time.sleep(2)
#
#     #滑动后元素列表
#     list2 = driver.find_elements_by_id("com.netease.mail:id/mail_list_item_from")
#     #滑动后最后一个元素信息
#     info2 = list2[-1].text
#     print(info1 + "------" + info2)
#     if info1 != info2:
#         print("未滑动到底部，继续滑动")
#         driver.swipe(500, 700, 500, 300)
#     else:
#         print("已经滑动到底部了")
#         swaile = False
#
#
#
# driver.quit


