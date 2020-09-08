# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 运行人力资源管理系统所有高优先级的场景

import time, unittest, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
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
    casepath = path.TEST_CASE_DIR + "/" + "hr/"
    # 加载测试场景
    test_suite = unittest.defaultTestLoader.discover(casepath, pattern='test*.py')

    # 运行测试场景
    result = BeautifulReport(test_suite)
    result.report(filename=currentime + '人力资源管理系统自动化测试报告', description='自动化测试报告', log_path=path.TEST_REPORT)
    case_count = dircount(casepath)
    # 将测试报告发送至邮箱，收件人，有多个时用逗号隔开

    send_test_report("人力资源管理系统-UI自动化测试报告", case_count)
