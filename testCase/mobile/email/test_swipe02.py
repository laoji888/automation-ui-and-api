import unittest, pytest, multiprocessing
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info


class Test1(unittest.TestCase):

    def t_1(self, device="mumu"):
        dr = driver(device, "邮箱大师")
        loger = log("baidutest1")
        home1 = home.Home(dr, loger)
        sleep(5)
        home1.clilk_text()
        sleep(2)
        dr.quit()

    def test_2(self):
        l = []
        # 实验多进程
        dict = get_config_info("exec", filename="/devices_info.ini")
        for k, v in dict.items():
            p = multiprocessing.Process(target=Test1().t_1, args=(v,))
            l.append(p)

        for i in l:
            i.start()

        for i in l:
            i.join()



if __name__ == '__main__':
    Test1().test_2()
