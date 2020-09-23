from time import sleep
from common.base_mobile import Base_mobile


# 继承BasePage类
class Home(Base_mobile):
    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log
        self.driver = driver


    def swipe(self):
        sleep(5)
        self.swipe_bottom("com.netease.mail:id/mail_list_item_from")