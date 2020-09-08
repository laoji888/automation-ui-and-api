# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 纪亚男
# 封装操作数据库方法
import pymysql, cx_Oracle, sys
from common.util import get_config_info


def operation_mysql(log, sql, databaseInfo="MySQL"):
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
        log.info('数据库已连接')
    except Exception as e:
        log.error("数据库连接失败-->{}".format(e))
    else:
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 获取操作游标
        cursor.execute(sql)  # 执行SQL语句
        results = cursor.fetchall()  # 获取所有记录列表
        log.info('sql语句执行成功')
        return results


def operation_oracle(log, sql, databaseInfo="Oracle"):
    """
操作Oracle数据库，如果要操作多个系统的数据库时可以在config下的configInfo配置数据库的相关信息
    :param sql: 要执行的sql语句
    :param databaseInfo: 要连接的数据库信息（在config/.ini文件中配置）
    :return:
    使用方法：在场景中直接调用此方法，传入相应的参数即可
    """

    conn = " "
    data = get_config_info(databaseInfo)
    selector = data["username"] + "/" + data["paswd"] + "@" + data["host"] + "/" + data["databasename"]
    try:
        conn = cx_Oracle.connect(selector)
        log.info("数据库连接成功")
    except Exception as e:
        log.error("数据库连接错误-->{}".format(e))
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
    log.info("操作Oracle数据库成功-->{}".format(sql))

