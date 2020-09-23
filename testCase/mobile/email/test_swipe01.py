import unittest,pytest,threading,multiprocessing
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info,run_thread
from time import sleep

class Test(unittest.TestCase):
    def tt001(self,device):
        dr = driver(device,"邮箱大师")
        loger = log("baidutest")
        home1 = home.Home(dr, loger)
        sleep(1)
        home1.swipe()
        dr.quit()

    def test_1(self):
        #多线程执行测试用例
        # run_thread(Test().tt001)
        # 实验多进程
        dict = get_config_info("exec",filename="/devices_info.ini")
        for k,v in dict.items():
            p = multiprocessing.Process(target=Test().tt001, args=(v,))
            p.daemon = False
            p.start()


if __name__ == '__main__':
    unittest.main()
