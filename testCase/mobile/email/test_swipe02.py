import unittest
from common.driver import Driver
from time import sleep
from common.util import multiprocess
from common.logger import log
from pageObject.mobile.email import home


class Test1(unittest.TestCase):

    # @multiprocess
    def test_1(self):
        dr = Driver(device="mumu", system="email")
        driver = dr.driver
        logs = dr.log
        home1 = home.Home(driver, logs)
        logs.info("==========================")
        sleep(5)
        home1.clilk_text()
        sleep(2)
        driver.quit()



if __name__ == '__main__':
    unittest.main()
