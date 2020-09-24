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

# capabilities = get_config_info("huaweip20", key=None, filename="/devices_info.ini")
capabilities = get_config_info("huaweip20", key=None, filename="/devices_info.ini")
#应用信息
app = get_config_info("邮箱大师", key=None, filename="/app_info.ini")
capabilities['appPackage'] = app["appPackage"]
capabilities['appActivity'] = app["appActivity"]

#获取执行机调用地址

driver =  webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
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

# import threading
# from time import sleep
#
# from testCase.mobile.email.swipe import Test_01
# aaa1 = ["mumu","夜神"]
#
# for i in aaa1:
#     aa = threading.Thread(target=Test_01().test,args=(i,))
#
#     aa.start()
# from common.util import get_config_info
# exec_dict = get_config_info("exec", filename="/devices_info.ini")
# exec_list = []
# for k, v in exec_dict.items():
#     exec_list.append(v)
#
# print(exec_list)



