
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from common.base_web import Base_web



'''手机端基类，继承Base_web'''
class Base_mobile(Base_web):
    def __init__(self,driver,log):
        super().__init__(driver,log)
        self.driver = driver
        self.log = log


    def swipe_screen(self,start_x, start_y,end_x, end_y):
        """
滑动屏幕，
        :param start_x: 开始x轴（屏幕比例）
        :param start_y: 开始y轴（屏幕比例）
        :param end_x: 结束x轴（屏幕比例）
        :param end_y: 结束x轴（屏幕比例）
        :param duration: 滑动动作持续的时间
        """
        #获取屏幕宽高
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        #滑动屏幕

        # actions = TouchAction(self.driver)
        # actions.press(x=width*start_x, y=height*start_y).wait(2)
        # actions.move_to(x=width*end_x, y=height*end_y)
        # actions.release()
        # actions.perform()
        self.driver.swipe(width*start_x, height*start_y, width*end_x, height*end_y)


    def swipe_to_element(self, element1, element2):
        self.driver.scroll(element1, element2)

    def buttons(self, type):
        """
模拟安卓手机按钮（仅限安卓）
KEYCODE_HOME (按键Home) : 3
KEYCODE_MENU (菜单键) : 82
KEYCODE_SEARCH 搜索键84
KEYCODE_BACK (返回键) : 4
KEYCODE_POWER 电源键26
KEYCODE_ENTER 回车键66
KEYCODE_DEL 退格键67
KEYCODE_FORWARD_DEL 删除键112
        :param type: 对应时间的数字
        """
        self.driver.keyevent(type)


    def swipe_bottom(self, id):
        """
滑动到底部
        :param id: 要滑动页面的列表id
        """
        #获取屏幕尺寸
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        swipe = True
        while (swipe):
            # 滑动前元素列表
            list1 = self.driver.find_elements_by_id(id)
            # 滑动前最后一个元素信息
            info1 = list1[-1].text
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3)
            sleep(2)
            # 滑动后元素列表
            list2 = self.driver.find_elements_by_id(id)
            # 滑动后最后一个元素信息
            info2 = list2[-1].text
            print(info1 + "------" + info2)
            if info1 != info2:
                print("未滑动到底部，继续滑动")
                self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3)
            else:
                print("已经滑动到底部了")
                swipe = False























