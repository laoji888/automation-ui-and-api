import unittest
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep

class Test_01(unittest.TestCase):


    def test(self):
        dr = driver("mumu","邮箱大师")
        # dr = driver(a,"邮箱大师")
        loger = log("baidutest")
        home1 = home.BossHome(dr, loger)
        sleep(1)
        home1.swipe()
        dr.quit()


if __name__ == '__main__':
    unittest.main()
