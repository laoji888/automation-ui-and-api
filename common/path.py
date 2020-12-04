# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 框架的全局路径

import os, sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report/").replace('\\','/')
# allure测试数据
AULLURE_RESULT = os.path.join(BASE_DIR,"allureResult/").replace('\\','/')
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs").replace('\\','/')
# 测试用例
TEST_CASE_DIR = os.path.join(BASE_DIR,"testCase").replace('\\','/')
# 配置文件目录
CONFIG_DIR = os.path.join(BASE_DIR,"config").replace('\\','/')
# 错误截图目录
IMG_DIR = os.path.join(BASE_DIR,"screenshots").replace('\\','/')
# 公共方法目录
COMMON_DIR = os.path.join(BASE_DIR,"common").replace('\\','/')
# 页面目录
PAGE_DIR = os.path.join(BASE_DIR,"pageObject").replace('\\','/')
# 元素目录
ELEMENT_DIR = os.path.join(BASE_DIR,"pageElement").replace('\\','/')
# 元素目录
PATH_DIR = os.path.join(BASE_DIR,"common","/path.py").replace('\\','/')
# 文件上传目录
UPLOAD_DIR = os.path.join(BASE_DIR,"uploads").replace('\\','/')
# html测试报告路径
HTML_REPORT_DIR = os.path.join(BASE_DIR,"html_report/").replace('\\','/')
# api接口文档路径
API_DOCUMENT = os.path.join(BASE_DIR,"apiData/").replace('\\','/')

def file_path(dir_name, file_name):
    """
    用于文件路径的获取
    :param dir_name: 文件夹名称
    :param file_name: 文件名
    :return:
    """
    FILE_PATH = os.path.join(BASE_DIR, dir_name, file_name).replace('\\','/')
    return FILE_PATH

if __name__ == '__main__':
    print(BASE_DIR)

