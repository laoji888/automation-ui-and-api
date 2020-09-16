import unittest
from pageObject.tencent.home import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep

class Test_01(unittest.TestCase):

    def test(self):
        dr = driver("huaweip20","腾讯新闻","appium01")
        loger = log("baidutest")
        home1 = home(dr, loger)
        sleep(15)
        home1.test01()
        sleep(10)
        dr.quit()


if __name__ == '__main__':
    unittest.main()
