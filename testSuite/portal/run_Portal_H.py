# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 马文静
# 执行 统一系统 高优先级测试场景，生成测试报告

import time, unittest, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append("/usr/local/oracle_client/instantclient_19_6")
from BeautifulReport import BeautifulReport
from common.report import send_test_report
from lib.email_template import dircount
from common import path
import os

# 如果没有report目录会自动创建一个
if not os.path.exists(path.TEST_REPORT): os.mkdir(path.TEST_REPORT)
currentime = time.strftime("%Y-%m-%d-%H-%M-%S")  # 获取当前时间
file_path = path.TEST_REPORT  # 测试报告路径

if __name__ == "__main__":
    casepath = path.TEST_CASE_DIR + "/portal/"
    # 加载测试场景
    test_suite = unittest.defaultTestLoader.discover(casepath, pattern='test*.py')

    # 运行测试场景
    result = BeautifulReport(test_suite)
    result.report(filename=currentime + '统一业务平台-UI自动化测试报告', description='统一业务平台-UI自动化测试报告', log_path=path.TEST_REPORT)
    case_count = dircount(casepath)
    # 将测试报告发送至邮箱，收件人，有多个时用逗号隔开
    send_test_report("统一业务平台-UI自动化测试报告", case_count)