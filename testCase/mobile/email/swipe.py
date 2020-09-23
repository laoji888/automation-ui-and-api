import unittest,pytest
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep

class Test_01():
    def test_1(self):
        dr = driver("mumu","邮箱大师")
        loger = log("baidutest")
        home1 = home.Home(dr, loger)
        sleep(1)
        home1.swipe()
        dr.quit()


if __name__ == '__main__':
    unittest.main()
