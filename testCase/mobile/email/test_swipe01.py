import unittest, pytest, threading, multiprocessing
from pageObject.email import home
from common.driver_mobile import driver
from common.logger import log
from time import sleep
from common.util import get_config_info, run_thread
from time import sleep


class Test(unittest.TestCase):
    def t_01(self, device="mumu"):
        dr = driver(device, "邮箱大师")
        loger = log("baidutest")
        home1 = home.Home(dr, loger)
        sleep(5)
        home1.swipe()
        sleep(5)
        dr.quit()



    def t_02(self, device="夜神"):
        dr = driver(device, "邮箱大师")
        loger = log("baidutest1")
        home1 = home.Home(dr, loger)
        home1.clilk_text()
        dr.quit()

    def test_1(self):
        # 实验多进程
        dict = get_config_info("exec", filename="/devices_info.ini")
        for k, v in dict.items():
            p = multiprocessing.Process(target=Test().t_01, args=(v,))
            print("运行用例01，执行机：{}，进程名称是：{}".format(v, p.name))
            p.start()


if __name__ == '__main__':
    # 获取类中所有的方法（自定义方法）
    '''
    1、获取类中所有的方法
    2、多进程调用方法。调用方法时遍历执行设备列表实现多线程
    问题：会同事启动多个进程，导致appium混乱。
    解决思路：将一个用例下的所有进程加入到列表，启动下次循环时判断上一组进程是否全部结束。结束则运行下一个用例。否则等待进程结束
    '''
    # 获取类中所有的方法
    list = dir(Test)
    list1 = []
    for i in list:
        if "test_" in i:
            ii = list.index(i)
            list1.append(list[ii])

    # 遍历测试用例和执行设备列表。多线程执行
    dict = get_config_info("exec", filename="/devices_info.ini")
    for i in list1:
        cmd = "Test()" + "." + i
        for k, v in dict.items():
            p = multiprocessing.Process(target=eval(cmd), args=(v,))
            print("运行用例02，执行机：{}，进程名称是：{}".format(v, p.name))
            p.start()
