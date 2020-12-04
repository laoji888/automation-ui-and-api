# -*- coding: utf-8 -*-
# @Date      : 2020-05-19
# @Author  : 纪亚男
# 读取配置文件信息


import sys, multiprocessing, os, pymysql, cx_Oracle
sys.path.append("/root/.jenkins/workspace/autotest")
from configobj import ConfigObj
from common import path

filepath = path.CONFIG_DIR


def get_config_info(section, key=None, filename="config.ini"):
    """
获取.ini文件信息,如果key为空时返回section下的所有信息，以字典的方式输出
如果key不为空时返回section下的key的值，以字符串的方式输出
    :param section: 节
    :param key: 键
    :param filename: .int文件名
    :return:
    """
    path = filepath + "/" + filename
    config = ConfigObj(path, encoding='UTF-8')
    if key == None:
        return dict(config[section])
    else:
        return config[section][key]


def operation_mysql(sql, databaseInfo="MySQL"):
    """
操作mysql数据库,如果要操作多个系统的数据库时可以在config下的configInfo配置数据库的相关信息,
    如果sql语句中有引号导致报错可以使用pymysql.escape_string(需要加引号的字符串)
    :param sql: 要执行的sql语句
    :param databaseInfo: 数据库信息（在config/.ini文件中配置）
    :return:
    使用方法：在场景中直接调用此方法，传入相应的参数即可
    """
    data = get_config_info(databaseInfo)
    try:
        host = data["host"]  # 数据库地址
        user = data["username"]  # 用户名
        pwd = data["paswd"]  # 密码
        database = data["databasename"]  # 库名
        port = int(data["port"])  # 端口号
        charset = data["encoding"]  # 字符编码
        db = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=pwd,
                             db=database)
    except Exception as e:
        raise e
    else:
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 获取操作游标
        cursor.execute(sql)  # 执行SQL语句
        results = cursor.fetchall()  # 获取所有记录列表
        db.commit()

        return results


def operation_oracle(sql, databaseInfo="Oracle"):
    """
操作Oracle数据库，如果要操作多个系统的数据库时可以在config下的configInfo配置数据库的相关信息
    :param sql: 要执行的sql语句
    :param databaseInfo: 要连接的数据库信息（在config/.ini文件中配置）
    :return:
    使用方法：在场景中直接调用此方法，传入相应的参数即可
    """

    conn = ""
    data = get_config_info(databaseInfo)
    selector = data["username"] + "/" + data["paswd"] + "@" + data["host"] + "/" + data["databasename"]
    try:
        conn = cx_Oracle.connect(selector)
    except Exception as e:
        print(e)
        pass
    # 执行sql语句
    cur = conn.cursor()
    cur.execute(sql)
    try:
        info = cur.fetchall()[0]
        return info
    except:
        pass
    # 提交后关闭游标断开与数据库的连接
    conn.commit()
    cur.close()
    conn.close()


def multiprocess(func):
    def wrapper():
        dict = get_config_info("web", filename="devices_info.ini")
        print(dict)
        for k, v in dict.items():
            print(v)
            p = multiprocessing.Process(target=func, args=(v,))
            p.start()

    return wrapper


def control_file_quantity(path):
    """
控制目录下文件的数量
    :param path: ，目录路径
    """
    count = os.listdir(path)
    if len(count) > int(get_config_info("Report_quantity", "quantity")):
        count.sort()
        ph = path + "/" + count[0]
        os.remove(ph)


if __name__ == '__main__':
    r = operation_mysql('DELETE FROM sys_user WHERE account="laoji"')
    print(r)
