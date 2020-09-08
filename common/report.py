# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 封装发送最新的测试报告到邮箱功能
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os, smtplib
from common.util import get_config_info
from common import path
from lib.email_template import get_report_info, email_temp

def send_test_report(title, case_count):
    """
以附件方式把最新的测试报告发送给指定的人，发件人邮箱信息、接收人的邮箱信息、
测试报告的最大数量都可以在config/configInfo.ini文件中配置
    :param case_count: 系统的测试场景个数
    :param title: 邮件标题
    """
    # 控制报告的数量以及返回最新的测试报告
    report_path = path.TEST_REPORT
    lists = os.listdir(report_path)  # 返回list
    lists.sort(key=lambda a: os.path.getatime(report_path + '/' + a))  # 以时间排序
    file_path = os.path.join(report_path, lists[-1])  # 返回测试报告路径
    count = os.listdir(report_path)
    if len(count) > int(get_config_info("Report_quantity", "quantity")):
        count.sort()
        ph = report_path + "/" + count[0]
        os.remove(ph)

    # 读取配置文件中的接收者邮箱地址
    mail = []
    data = get_config_info("Acceptor")
    for i in data:
        mail.append(data[i])

    s_server = 'smtp.163.com'  # 定义邮箱服务
    user = get_config_info("Mail", "username")  # 读取配置文件的用户名
    password = get_config_info("Mail", "password")  # 读取配置文件的密码(授权密码)
    msg_total = MIMEMultipart()  # 定义类型
    # multipart类型主要有三种子类型：mixed、alternative、related  默认mixed
    msg_total['From'] = user  # 发送方邮箱
    msg_total['To'] = ','.join(mail)  # 接受者邮箱
    msg_total['Subject'] = title  # 邮件的标题
    # 正文模块
    # msg_raw = open(file_path, "r", encoding='utf-8').read()  # 打开要发送的测试报告
    msg_raw = email_temp(title, case_count, file_path)
    msg = MIMEText(msg_raw, 'html',"utf-8")
    msg_total.attach(msg)
    # 附件模块
    mfile = MIMEApplication(open(file_path, "rb").read())  # 读取测试报告内容
    mfile.add_header('Content-Disposition', 'attachment', filename=file_path)  # 添加附件的头信息
    # 添加附件
    msg_total.attach(mfile)
    smtp = smtplib.SMTP_SSL(s_server, 465)
    smtp.login(user, password)
    smtp.sendmail(user, mail, msg_total.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_test_report("统一业务平台-UI自动化测试报告", 1)
