
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
        # actions.move_to(x=width*end_x, y=height*end_y).wait(2)
        # actions.release()
        # actions.perform()
        self.driver.swipe(width*start_x, height*start_y, width*end_x, height*end_y)



    def swipe_to_element(self):
        self.driver.Scroll()














