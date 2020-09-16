import unittest
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
        a = self.driver.find_element(*self.home["按钮-起始元素"])
        b = self.driver.find_element(*self.home["按钮-终止元素"])
        self.driver.scroll(a, b)




if __name__ == '__main__':
    unittest.main()