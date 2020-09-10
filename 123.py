
import yaml
import os
from selenium.webdriver.common.by import By



# def get_yaml_data(yaml_file):
#     # 打开yaml文件
#     print("***获取yaml文件数据***")
#     file = open(yaml_file, 'r', encoding="utf-8")
#     file_data = file.read()
#     file.close()
#
#     # 将字符串转化为字典或列表
#     print("***转化yaml数据为字典或列表***")
#     data = yaml.load(file_data)
#     print(data)
#     print("类型：", type(data))
#     return data
#
#
#
# aa = get_yaml_data("E:\\python_script\\automation-ui-and-api\\config\\devicesInfo.yaml")
# print(aa)
# # a1 = (aa["输入框"][0],aa["输入框"][1])
# # print(a1)
# # print(type(a1))

from common.util import get_config_info

aa = get_config_info("da", key=None, filename="/aaa.ini")
print(aa)
# bb = list(eval(aa["app"]))
# print(bb)

