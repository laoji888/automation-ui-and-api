from common.base_mobile import Base_mobile


# 继承BasePage类
class BossHome(Base_mobile):
    def __init__(self, driver, log):
        self.home = self.element_info("home", file_name="/mobile/boss/boss_elements.xlsx")
        super().__init__(driver, log)
        self.log = log
        self.driver = driver


    def enter_my(self):
        # self.click(*self.home["按钮-我的"])
        self.swipe_screen(0.9,0.8,0.1,0.8)

    def home_search(self,value):
        self.click(*self.home["按钮-首页搜索按钮"])
        self.click(*self.home["搜索框-首页搜索框"])
        self.send_keys(value, *self.home["搜索框-首页搜索框"])
        # result = self.driver.execute_script('mobile: shell', {
        #     'adb shell input keyevent 66': 'echo',
        #     'args': ['arg1', 'arg2'],
        #     'includeStderr': True,
        #     'timeout': 5000
        # })


# appium -p 4723 --relaxed-security --allow-insecure=adb_shell