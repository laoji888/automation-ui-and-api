import unittest,pytest,threading,multiprocessing
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info,run_thread
from time import sleep
class Test():
    def tt001(self,device="mumu"):
        dr = driver(device,"邮箱大师")
        loger = log("baidutest")
        home1 = home.Home(dr, loger)
        sleep(1)
        home1.swipe()
        print("111")
        dr.quit()

    def test_1(self):
        # 实验多进程
        dict = get_config_info("exec",filename="/devices_info.ini")
        for k,v in dict.items():
            p = multiprocessing.Process(target=Test().tt001, args=(v,))
            print("运行用例01，执行机：{}，进程名称是：{}".format(v, p.name))
            p.start()
