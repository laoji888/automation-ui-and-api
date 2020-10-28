import multiprocessing
import unittest
from pageObject.mobile.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info


def multiprocess(func):
    def wrapper(*args, **kwargs):
        dict = get_config_info("web", filename="devices_info.ini")
        print(dict)
        for k, v in dict.items():
            print(v)
            p = multiprocessing.Process(target=func, args=(v,))
            p.start()
            p.join()
        return func(*args, **kwargs)
    return wrapper






