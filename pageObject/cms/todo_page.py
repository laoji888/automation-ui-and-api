# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 合同系统-审批待办页面


from selenium import webdriver
from common.basePage import BasePage
from time import sleep
from common import path

from unittest import TestCase

# 审批待办页面
class Todopage(BasePage):



    #读取todo_page页面元素
    def __init__(self, driver, log):
        self.element = self.element_info("todo_page", file_name="cms/thecontract_elements.xlsx")
        super().__init__(driver, log, self.element)
        self.log = log
        self.driver = driver




    # 审批待办事项
    def our_todo1(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """

        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(10)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        #self.execute_js("window.focus();")
        self.execute_js("$('html,body').scrollTop(500);")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        #js选择下一步审批人
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '赵淑亚(zhaosy)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)





    # 审批待办事项
    def our_todo2(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        sleep(3)
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '宋日健(songrj)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo3(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '孙传毅(suncy)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo4(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("$('html,body').scrollTop(500);")

        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '李庭婷(litt3)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo5(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '罗俊强(luojq)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo6(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(3)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        sleep(2)

        self.execute_js("$('html,body').scrollTop(500);")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '李本松(libs3)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo7(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("$('html,body').scrollTop(500);")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '李坚(lijian3)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo8(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '沈风华(shenfh)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo9(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        sleep(2)
        self.execute_js("$('html,body').scrollTop(500);")
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[3]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '赵淑亚(zhaosy)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批定稿待办事项
    def our_todo10(self, serialnumber):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(8)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        sleep(3)

        # 获取合同编号
        Contractno = self.element_text(*self.element["文本-合同编号"])

        self.click(*self.element["按钮-有水印定稿"])
        sleep(8)
        self.run_command("C:\自动化\ht_Closefile.exe", "Gaogd_ie", "cms_host")
        sleep(6)
        self.click(*self.element["按钮-关闭"])
        sleep(3)
        return Contractno



    # 签订盖章
    def our_todo11(self, serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(5)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.execute_js("window.top.opener=null;window.top.open('','_top');window.top.close();")
        self.switch_to_window(-1)
        self.execute_js("window.focus();")
        sleep(3)
        self.await_element(*self.element["输入框-输入签订盖章份数"])
        self.send_keys(approvalopinions, *self.element["输入框-输入签订盖章份数"])
        self.execute_js("document.documentElement.scrollTop=10000")
        self.click(*self.element["按钮-添加附件"])
        sleep(5)

        self.run_command("C:\自动化\ht_up_file.exe", "Gaogd_ie", "cms_host")
        sleep(5)
        self.switch_to_frame(*self.element["框架-上传附件"])
        self.click(*self.element["按钮-提交（上传附件）"])
        sleep(3)
        self.switch_to_default()
        self.click(*self.element["按钮-下一步"])
        sleep(4)
        self.execute_js("iframes = document.getElementsByTagName('iframe')[1]; currentDoc = iframes.contentDocument; var s =currentDoc.getElementsByTagName('span'); for(var i=0,j=s.length; i<j;i++){ if(s[i].innerHTML === '李本松(libs3)') s[i].click();    };")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)




    # 审批待办事项
    def our_todo12(self,serialnumber, approvalopinions):
        """
        :param serialnumber: 合同流水号
        :param approvalopinions: 审批意见
        :return:

        """
        self.mouse_hover(*self.element["按钮-我的工作"])
        self.execute_js("$('#1021').mouseover();$('#1021').mouseout();$('#1021').mouseover();")
        self.click(*self.element["按钮-待办事项"])
        sleep(3)
        self.switch_to_frame(*self.element["框架-待办事项页面"])
        self.await_element(*self.element["输入框-合同流水号"])
        self.send_keys(serialnumber, *self.element["输入框-合同流水号"])
        self.click(*self.element["按钮-查询"])
        self.await_element(*self.element["链接-打开合同信息"])
        sleep(3)
        self.click(*self.element["链接-打开合同信息"])
        sleep(2)
        self.switch_to_window(-1)
        sleep(2)
        self.execute_js("$('html,body').scrollTop(500);")
        self.mouse_hover(*self.element["输入框-输入审批意见"])
        self.send_keys(approvalopinions, *self.element["输入框-输入审批意见"])
        self.click(*self.element["按钮-下一步"])
        sleep(3)
        self.execute_js("$('.jiantou').click();")
        sleep(3)
        self.switch_to_frame(*self.element["框架-切换到选择办理人框架"])
        self.click(*self.element["按钮->箭头"])
        self.click(*self.element["按钮-提交（选择办理人）"])
        sleep(5)



