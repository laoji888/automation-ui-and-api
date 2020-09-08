# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 读取配置文件信息

from configparser import ConfigParser
from common import path

filepath = path.CONFIG_DIR


def get_config_info(section, key=None, filename="/configInfo.ini"):
    """
获取.ini文件信息,如果key为空时返回section下的所有信息，以字典的方式输出
如果key不为空时返回section下的key的值，以字符串的方式输出
    :param section: 节
    :param key: 键
    :param filename: .int文件名
    :return:
    """
    path = filepath + filename
    data = " "
    try:
        config = ConfigParser()
        config.read(path, encoding="utf-8")
        if key == None:
            list = config.items(section)
            data = dict(list)
        if key != None:
            data = config.get(section, key)
    except Exception as e:
        print(e)
    return data


