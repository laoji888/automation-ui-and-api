# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 主要对selenium常用的方法进行二次封装

import re, os, datetime, xlrd
from common.util import *
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from common import path
from selenium.webdriver.common.by import By


class Base_web():


    def __init__(self, driver, log):
        """
    初始化浏览器对象
        :param logname: 运行测试场景时生成的log文件名
        :param driver: 浏览器对象
        """
        self.driver = driver
        self.log = log




    def get_key(self, dict, value):
        """
        通过value获取对应的key
        :param dict:
        :param value:
        :return:
        """
        return list(filter(lambda k: dict[k] == value, dict))



    def add_style(self, *loc):
        """
    给操作元素添加样式（红框）
        :param loc: 元素信息，格式是元组
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                       ele, "border: 2px solid red;")
        except:
            pass



    def set_style(self, *loc):
        """
    操作元素后把红框改成蓝框
        :param loc:元素信息
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                       ele, "border: 2px solid blue;")
        except:
            pass



    def implicitly_wait(self, timout=30):
        """
    等待页面元素全局加载完毕(隐式等待)，超时时间默认是30秒，如果30秒后没有加载完成执行一次刷新
        :param timout: 等待元素超时时间
        :return:
        """
        try:
            self.driver.implicitly_wait(timout)
        except:
            self.driver.refresh()
            self.log.debug("全局等待超时，已刷新页面")



    def refresh(self):
        """
    刷新浏览器
        """
        self.driver.refresh()
        self.log.debug("浏览器刷新成功")



    def forward(self):
        """
    浏览器前进
        """
        self.driver.forward()
        title = self.get_title()
        self.log.debug("浏览器前进成功，当前的页面title为-->{}".format(title))



    def back(self):
        """
    浏览器后退
        """
        self.driver.back()
        title = self.get_title()
        self.log.debug("浏览器后退成功，当前的页面title为-->{}".format(title))



    def await_element(self, timeout=30, *loc):
        """
    等待某个元素出现(显式等待)
        :param timeout:等待元素超时时间
        :param loc:元素信息
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.log.error("等待元素“{}”失败，元素不存在或者时间超时".format(self.get_key(self.element, loc)))
            raise e



    def click(self, timeout=30, *loc):
        """
    定位到元素并点击,如果点击失败判断元素是否显示，如果显示尝试等待两秒再次点击，再次点击失败后写入日志。
        :param loc: 元素信息，格式为元组
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)
        try:
            self.driver.find_element(*loc).click()
            self.log.debug("点击元素-->{}成功".format(self.get_key(self.element, loc)))
        except Exception as e:
            ele = self.is_display(*loc)
            if ele:
                sleep(3)
                self.driver.find_element(*loc).click()
                self.log.debug("二次点击元素-->{}成功".format(self.get_key(self.element, loc)))
            else:
                self.log.error("点击元素-->{}失败，错误信息是：{}".format(self.get_key(self.element, loc), e))
                raise e
        self.set_style(*loc)



    def elements_click(self, index, timeout=30, *loc):
        """
    定位元素集合，用索引选择要点击的元素
        :param timeout: 等待元素超时时间
        :param index: 元素索引
        :param loc: 元素信息（元组）
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)
        try:
            self.driver.find_elements(*loc)[index].click()
            self.set_style(*loc)
            self.log.debug("选择{}集合的第{}个元素成功".format(loc, index))
        except Exception as e:
            self.log.error("选择{}集合的第{}个元素失败：{}".format(loc, index, e))
            raise e
            pass



    def clickXY(self, section="firefox", key="host", *element):
        """
    获取flash控件的坐标并点击
        :param section: 配置文件下执行机的section
        :param key: 配置文件下执行机的key
        :param element: 要点击的控件定位信息
        """
        # 工具栏和浏览器边界和屏幕边界距离
        x1 = 0
        y1 = 0
        # 框架坐标
        x2 = 0
        y2 = 0
        # 判断元素是否在框架内,如果在就退回上一层框架获取工具栏和浏览器边界和屏幕边界距离和框架坐标
        if self.driver.execute_script("if (window.frames.length != parent.frames.length) {return true;}"
                                      "else{return false}"):
            # 获取当前框架信息
            frame = self.driver.execute_script("return window.location;").get("href")
            frame1 = re.search(r":[0-9]+/.*", frame).group()
            frame2 = re.search(r"/.*jsp", frame1).group()
            xpath = "//iframe[contains(@src," + "'" + frame2 + "')]"
            self.driver.switch_to.parent_frame()

            # 计算下浏览器的工具栏和浏览器边界和屏幕边界距离
            x1 = int(self.driver.execute_script("return window.screenX;"))
            y1 = int(self.driver.execute_script("return window.screenY + window.outerHeight - window.innerHeight;"))
            self.log.debug("浏览器边界:{},{}".format(x1, y1))

            # 如果元素在框架内获取框架坐标
            currentframe = self.driver.find_element_by_xpath(xpath)
            x2 = int(self.driver.execute_script("x=arguments[0].getBoundingClientRect().left;return x", currentframe))
            y2 = int(self.driver.execute_script("y=arguments[0].getBoundingClientRect().top;return y", currentframe))
            currentframe = self.driver.find_element_by_xpath(xpath)
            self.driver.switch_to.frame(currentframe)
        else:
            # 计算下浏览器的工具栏和浏览器边界和屏幕边界距离
            x1 = int(self.driver.execute_script("return window.screenX;"))
            y1 = int(self.driver.execute_script("return window.screenY + window.outerHeight - window.innerHeight;"))
            self.log.debug("浏览器边界:{},{}".format(x1, y1))

        buttonxy = self.element_object(*element).location
        element = self.element_object(*element)
        self.log.debug("上传附件按钮坐标:" + str(buttonxy))
        self.log.debug("上传附件按钮大小:" + str(element.size))
        buttonxy["x"] = buttonxy["x"] + element.size["width"] / 2
        buttonxy["y"] = buttonxy["y"] + element.size["height"] + 5
        self.log.debug('点击坐标:{}'.format(buttonxy))

        # 元素的最终坐标 frameXY
        buttonxy["x"] += x2
        buttonxy["y"] += y2
        buttonxy["x"] += x1
        buttonxy["y"] += y1
        buttonxy["x"] = int(buttonxy["x"])
        buttonxy["y"] = int(buttonxy["y"])
        self.log.debug('元素的最终坐标:{}'.format(buttonxy))
        host = get_config_info(section, key)
        r = requests.get('http://' + host + '/webdriver/CLICK_XY', params=buttonxy)
        self.log.debug(r.text)



    def double_click(self, timeout=30, *loc):
        """
    双击鼠标左键
        :param timeout: 等待元素超时时间
        :param loc:元素信息
        """
        self.add_style(*loc)
        self.await_element(*loc, timeout=timeout)
        element = self.element_object(*loc)
        try:
            ActionChains(self.driver).double_click(element).perform()
            self.log.debug("双击{}成功".format(self.get_key(self.element, loc)))
        except Exception as e:
            ele = self.is_display(*loc)
            if ele:
                sleep(2)
                ActionChains(self.driver).double_click(element).perform()
                self.log.debug("双击{}成功".format(self.get_key(self.element, loc)))
            else:
                self.log.error("双击{}失败,报错信息是-->{}".format(self.get_key(self.element, loc), e))
                raise e



    def alert_accept(self):
        """
    接受弹窗
        """
        try:
            self.driver.switch_to.alert.accept()
            self.log.debug("弹窗处理成功")
        except Exception as e:
            self.log.error("弹窗处理失败{}".format(e))
            raise e



    def scroll_into_element(self, timeout=30, *loc):
        """
    滚动条滚动到指定元素
        :param timeout: 等待元素超时时间
        :param loc: 要滚动到的元素
        """
        self.await_element(*loc, timeout=timeout)
        ele = self.driver.find_element(*loc)
        self.add_style(*loc)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            self.set_style(*loc)
            self.log.debug("滚动到元素{}成功".format(self.get_key(self.element, loc)))
        except Exception as e:
            self.log.error("滚动到元素{}失败：{}".format(self.get_key(self.element, loc), e))
            raise e



    def element_text(self, timeout=30, *loc):
        """
    定位元素，返回对象文本
        :param timeout: 等待元素超时时间
        :param loc: 元素信息
        :return: 返回元素的对象
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)

        try:
            ele = self.driver.find_element(*loc).text
            self.log.debug("返回{}文本成功，返回的文本-->{}".format(self.get_key(self.element, loc), ele))
            return ele
        except Exception as e:
            self.log.debug("返回{}文本失败-->{}".format(self.get_key(self.element, loc), e))
            raise e



    def element_attribute(self, attribute, timout=30, *loc):
        """
    定位元素，返回对象属性值
        :param timout: 等待元素超时时间
        :param loc: 元素信息
        :param attribute: 元素属性
        :return: 返回元素的对象
        """
        res = self.is_display(*loc)
        if res:
            WebDriverWait(self.driver, timout).until(EC.visibility_of_element_located(loc))
        else:
            sleep(2)
        self.add_style(*loc)

        try:
            ele = self.driver.find_element(*loc).get_attribute(attribute)
            self.log.debug("返回{}属性值{}成功，返回的属性值-->{}".format(loc, attribute, ele))
            return ele
        except Exception as e:
            self.log.error("返回{}属性值失败-->{}".format(loc, e))
            raise e



    def element_object(self, timeout=30, *loc):
        """
    定位元素，返回对象
        :param loc: 元素信息
        :return: 返回元素的对象
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)

        try:
            ele = self.driver.find_element(*loc)
            self.log.debug("返回对象成功{}".format(self.get_key(self.element, loc)))
            return ele
        except Exception as e:
            self.log.error("返回{}对象失败,错误信息是-->{}".format(self.get_key(self.element, loc), e))
            raise e



    def select(self, index, timeout=30, *loc):
        """
    操作select下拉框
        :param timeout: 等待元素超时时间
        :param index:要选择的options元素索引
        :param loc: 元素信息
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)
        ele = self.driver.find_element(*loc)
        try:
            Select(ele).select_by_index(index)
            self.log.debug("下拉框选择成功")
        except Exception as e:
            ele = self.is_display(*loc)
            if ele:
                try:
                    sleep(2)
                    Select(ele).select_by_index(index)
                    self.log.debug("下拉框选择成功")
                except Exception as e:
                    self.log.error("下拉框{}选择失败-->{}".format(self.get_key(self.element, loc), e))
                    raise e



    def execute_js(self, js):
        """
        执行js代码
        :param js: 要执行的js代码
        :return:
        """
        result = self.driver.execute_script(js)
        self.log.debug("执行js成功")
        return result

        # self.get_key(self.element)



    def send_keys(self, value, timeput=30, *loc):
        """
        等待元素出现后清空并输入数据
        :param value: 输入的数据
        :param loc: 元素信息
        """
        print(*loc)
        self.await_element(*loc, timeout=timeput)
        self.add_style(*loc)
        self.driver.find_element(*loc).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*loc).send_keys(Keys.BACKSPACE)

        try:
            self.driver.find_element(*loc).send_keys(value)
            self.set_style(*loc)
            self.log.debug("信息输入成功，内容是:{}".format(value))
        except Exception as e:
            self.log.error("信息输入失败{}".format(e))
            raise e



    def input_file_upload(self, file_path, timeout=30, *loc):
        """
    input文件上传，file_path是要上传的文件目录名和文件名称，比如"pms_upload/excell.xlsx"，pms_upload对应框架中testData目录下的子目录，
    excell.xlsx是文件名。每个被测系统都有一个单独的子目录，用于存放需要上传的文件
        :param timeout: 等待元素超时时间
        :param file_path: 待上传的文件目录和文件名
        :param loc: 元素信息
        """
        self.await_element(*loc, timeout=timeout)
        self.add_style(*loc)

        try:
            self.driver.find_element(*loc).send_keys(path.UPLOAD_DIR + file_path)
            self.set_style(*loc)
            self.log.debug("文件输入成功，内容是:{}".format(file_path))
        except Exception as e:
            self.log.error("文件输入失败{}".format(e))
            raise e



    def switch_to_frame(self, timeout=30, *loc):
        """
    切换frame框架
        :param timeout: 等待元素超时时间
        :param loc: frame框架对象
        """
        self.await_element(*loc, timeout=timeout)
        ele = self.driver.find_element(*loc)
        try:
            self.driver.switch_to.frame(ele)
            self.log.debug("切换到框架{}".format(self.get_key(self.element, loc)))
        except Exception as e:
            if self.is_display(ele):
                try:
                    sleep(2)
                    self.driver.switch_to.frame(ele)
                    self.log.debug("切换到框架{}".format(self.get_key(self.element, loc)))
                except Exception as e:
                    self.log.error("框架不存在或者未显示{}".format(e))
                    raise e



    def switch_to_default(self):
        """
    切换到默认框架
        """
        self.driver.switch_to_default_content()
        self.log.debug("已切换到默认框架")



    def switch_to_parent(self):
        """
    切换到上一级框架
        """
        self.driver.switch_to.parent_frame()
        self.log.debug("已切换到上一级框架")



    def switch_to_window(self, num=-1):
        """
    切换窗口,默认是切换到最新窗口
        :param num: 窗口索引
        """
        handles = self.driver.window_handles
        for i in range(10000):
            self.driver.switch_to.window(handles[num])
            self.log.debug("窗口切换成功，当前窗口title是-->{}".format(self.driver.title))
            break



    def get_title(self):
        """
    获取当前页面的title并返回
        :return:
        """
        title = self.driver.title
        self.log.debug('当前窗口的title是:%s' % title)
        return title



    def mouse_hover(self, timeout=30, *loc):
        """
        鼠标悬停到指定元素,如果失败等待两秒后再次操作，再次失败后将错误写入日志
        :param timeout: 等待元素超时时间
        :param loc: 元素信息
        """
        self.await_element(*loc, timeout=timeout)
        ele = self.driver.find_element(*loc)
        self.add_style(*loc)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            self.set_style(*loc)
            self.log.debug("鼠标悬停至{}成功".format(self.get_key(self.element, loc)))
        except Exception as e:
            if self.is_display(*loc):  # 判断元素是否显示
                try:
                    sleep(2)
                    ActionChains(self.driver).move_to_element(ele).perform()
                    self.set_style(*loc)
                    self.log.debug("鼠标悬停至{}成功".format(self.get_key(self.element, loc)))
                except Exception as e:
                    self.log.error("鼠标悬停至{}失败-->{}".format(self.get_key(self.element, loc), e))
                    raise e



    def element_info(self, sheetname, file_name="it_workOrder.xlsx"):
        """
    读取xlsx文件内的元素信息，以字典的方式输出
        :param file_name: 文件名
        :param sheetname: sheet页名
        :return:
        """
        data = {}
        data_key = " "
        data_value = " "

        datapath = path.ELEMENT_DIR + "/" + file_name
        xls1 = xlrd.open_workbook(datapath)
        table = xls1.sheet_by_name(sheetname)

        for i in range(0, table.nrows):
            data_key = table.cell_value(i, 0)
            data_value = table.cell_value(i, 1)
            ele = tuple(eval(data_value))
            data[data_key] = ele
        xls1.release_resources()
        return data



    def is_display(self, *loc):
        """
    判断元素是否显示，显示返回True，不显示返回False
        :param loc：要检验的元素
        :return:
        """
        try:
            self.driver.find_element(*loc).is_displayed()
            return True
        except:
            return False



    def run_command(self, filepath, section, key):
        """
    执行exe文件（此方法适用于IE浏览器）
        :param section: 配置文件中的section
        :param key: 配置文件中的key
        :param filepath: 需要执行的exe文件路径
        """
        payload = {'osType': 'window',
                   'content': filepath}
        r = requests.post('http://' + get_config_info(section, key) + '/execCommand', data=payload)
        self.log.debug("执行cmd成功")



    def keys_down(self):
        """
    键盘敲击'↓’键
        """
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        self.log.debug('键盘敲击↓键')



    def keys_tab(self):
        """
    键盘敲击'TAB’键
        """
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.log.debug('键盘敲击"TAB"键')



    def keys_enter(self):
        """
    键盘敲击回车
        """
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.log.debug('键盘敲击回车')



    def keys_esc(self):
        """
    键盘敲击ESC
        """
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.log.debug('键盘ESC')



    def linux_file_upload(self, file_path=None, section="firefox", key="host"):
        """
    linux下的非input上传功能，file_path是要上传的文件目录名和文件名称，比如"pms_upload/excell.xlsx"，pms_upload对应框架中testData目录下的子目录，
    excell.xlsx是文件名。每个被测系统都有一个单独的子目录，用于存放需要上传的文件
        :param filename:要上传的目录名和文件名
        :param section:ini配置文件的节点
        :param key:ini配置文件的键
        """
        filepath = path.UPLOAD_DIR + file_path
        payload = {'FilePath': filepath}
        host = get_config_info(section, key)
        r = requests.get('http://' + host + '/webdriver/UPLOAD_ROBOT', params=payload)
        self.log.debug("文件上传成功-->{}".format(r.text))



    def screenshot(self, imgname):
        """
    主动截图，并将图片附到测试报告中
        :param imgname: 图片名称
        """
        self.driver.get_screenshot_as_file(path.IMG_DIR + "/" + imgname)
        HTML_IMG_TEMPLATE = """
            <a href="data:image/png;base64, {}">
            <img src="data:image/png;base64, {}" width="800px" height="500px"/>
            </a>
            <br></br>
        """
        # 图片路径
        png = path.IMG_DIR

        # 将图片发送到Html报告里。
        data = BeautifulReport.img2base(png, imgname)
        print(HTML_IMG_TEMPLATE.format(data, data))
        print('<br></br>')

# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     aa = (By.ID, 'kw1')
#     dr = BasePage(driver)
#     sleep(2)
#     driver.find_element(By.LINK_TEXT, "hao123")
#     driver.switch_to.alert.accept()
