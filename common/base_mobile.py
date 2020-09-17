
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























