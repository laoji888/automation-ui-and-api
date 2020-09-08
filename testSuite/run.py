# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# 运行百度测试场景

import time, unittest, os, sys
# 返回当前框架的路径并添加到环境变量，每多一层os.path.dirname（）返回的路径就少一层，
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.email_template import dircount
from BeautifulReport import BeautifulReport
from common import path
from common.report import send_test_report
import os

# 如果没有report目录会自动创建一个
if not os.path.exists(path.TEST_REPORT): os.mkdir(path.TEST_REPORT)
currentime = time.strftime("%Y-%m-%d-%H-%M-%S")  # 获取当前时间
file_path = path.TEST_REPORT  # 测试报告路径

if __name__ == "__main__":
    # 加载测试场景
    test_suite = unittest.defaultTestLoader.discover(path.TEST_CASE_DIR, pattern='test_baidu.py')

    # 运行测试场景
    result = BeautifulReport(test_suite)
    result.report(filename=currentime + '百度测试报告', description='百度测试场景', log_path=path.TEST_REPORT)

    case_count = dircount(path.TEST_CASE_DIR)
    # 将测试报告发送至邮箱
    # send_test_report("测试报告-(邮件标题)", case_count)
