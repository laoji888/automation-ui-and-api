import functools, dill
import multiprocessing
import threading
import time

from common.util import get_config_info
import unittest, pytest, multiprocessing
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info
from pathos.multiprocessing import ProcessingPool as Pool
from common.util import multiprocess


class tt(unittest.TestCase):
    @multiprocess
    def test_1(self, device):
        dr = driver(device, "邮箱大师")
        loger = log("baidutest1")
        home1 = home.Home(dr, loger)
        sleep(5)
        home1.clilk_text()
        sleep(2)
        dr.quit()

if __name__ == '__main__':
    unittest.main()
    '''
        解决思路：pathos模块
        pathos是一个较为综合性的模块，既能多进程，也能多线程。其主要采用进程池/线程池方法。
    '''
