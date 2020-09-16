import unittest
from pageObject.boss.boss_home import  BossHome
from common.driver_mobile import driver
from common.logger import log
from time import sleep

class Test_01(unittest.TestCase):

    def test(self):
        dr = driver("huaweip20","腾讯新闻","appium01")
        loger = log("baidutest")
        home = BossHome(dr, loger)
        # home.home_search("自动化测试")
        sleep(15)
        home.enter_my()
        sleep(10)
        dr.quit()


if __name__ == '__main__':
    unittest.main()
