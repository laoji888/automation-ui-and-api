import unittest

from appium.webdriver.common.touch_action import TouchAction

from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.base_mobile import Base_mobile

class home(Base_mobile):
    def __init__(self, driver, log):
        self.home = self.element_info("home", file_name="/mobile/tencent/tencent_news_elements.xlsx")
        super().__init__(driver, log)
        self.log = log
        self.driver = driver

    def test01(self):
        self.click(*self.home["按钮-我的"])
        self.click(*self.home["按钮-设置"])
        self.click(*self.home["单选框-夜间模式"])
        sleep(2)
        self.click(*self.home["单选框-夜间模式"])
        sleep(1)
        self.elements_click(0,*self.home["按钮-不随位置变化"])


    def test02(self):
        self.click(*self.home["搜索框-首页搜索框"])
        self.send_keys("java", *self.home["搜索框-首页搜索框"])
        sleep(3)
        self.buttons(66)





if __name__ == '__main__':
    unittest.main()