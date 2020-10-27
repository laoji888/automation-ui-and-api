import unittest
from pageObject.mobile.tencent.home import home
from common.driver import Driver
from common.logger import log
from time import sleep

class Test_01(unittest.TestCase):

    def test(self):
        dr = Driver(device="huaweip20", system="腾讯新闻").driver
        loger = log("baidutest")
        home1 = home(dr, loger)
        # home1.test01()
        home1.test02()
        sleep(5)
        dr.quit()


if __name__ == '__main__':
    unittest.main()
