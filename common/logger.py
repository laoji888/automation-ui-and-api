# -*- coding: utf-8 -*-
# @Date      : 2020-05-20
# @Author  : 纪亚男
# 封装log日志功能

import logging, time, os
from common import path

'''
多进程下日志解决方案：日志将在
'''
# 日志存放文件夹，如不存在，则自动创建一个logs目录

def log(logname="自动化测试", system=""):
    """
生成日志，控制日志的总数量.在pageObject或者testCase中也可以使用此方法进行日志的输出
    :param logname: log文件名
    :return:
    """
    file = system
    if system == "":
        file = "interfase"
    # 如果没有对应的日志目录和文件就新建
    if not os.path.exists(path.LOG_DIR): os.mkdir(path.LOG_DIR)
    LOG_DIR = os.path.join(path.LOG_DIR, file).replace('\\', '/')
    if not os.path.exists(LOG_DIR): os.mkdir(LOG_DIR)

    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 设置日志文件名
    all_log_name = path.LOG_DIR + "/" + system + "/" + logname + '.log'

    # 创建一个handler写入所有日志
    #fh = logging.FileHandler(all_log_name, mode='w', encoding='utf-8')
    fh = logging.FileHandler(all_log_name,encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    all_log_formatter = logging.Formatter('%(asctime)s - '
                                          '%(levelname)s - '
                                          '%(filename)s[line:%(lineno)d] - '
                                          '%(funcName)s - %(message)s')

    # 这两行代码是为了避免日志输出重复问题
    logger.removeHandler(ch)
    logger.removeHandler(fh)

    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
