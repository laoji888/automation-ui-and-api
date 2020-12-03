# -*- coding: utf-8 -*-
# @Date      : 2020-05-20
# @Author  : 纪亚男
# 封装log日志功能

import logging, time, os
from common import path

def log(logname="自动化测试"):
    """
    记录日志
    :param logname: 日志文件的名称
    :return:
    """
    current_time = time.strftime("%Y-%m-%d")
    file = logname + "-" + current_time + ".log"

    # 如果没有对应的日志目录和文件就新建
    if not os.path.exists(path.LOG_DIR): os.mkdir(path.LOG_DIR)
    LOG_DIR = os.path.join(path.LOG_DIR, file).replace('\\', '/')
    if not os.path.isfile(LOG_DIR):  # 无文件时创建
        fd = open(LOG_DIR, "w+")
        fd.close()


    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建一个handler写入所有日志
    #fh = logging.FileHandler(all_log_name, mode='w', encoding='utf-8')
    fh = logging.FileHandler(LOG_DIR,encoding='utf-8')
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
