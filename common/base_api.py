import datetime
from common.logger import log
import xlrd, requests, unittest, time, json
from common import path
from common.util import get_config_info, operation_mysql, operation_oracle

log = log(logname="api", system="interfase")


# now_time = datetime.datetime.now() 获取时间
# t1 = (now_time + datetime.timedelta(seconds=+3)).strftime("%Y-%m-%d %H:%M:%S") # 当前时间+3
# t2 = (now_time + datetime.timedelta(seconds=+15)).strftime("%Y-%m-%d %H:%M:%S") # 当前时间+15


# 接口测试类
class Base_api():

    #  初始化方法
    def __init__(self, filepath, sheet_name):
        """
        初始化方法
        :param filepath:  存放参数的Excel文件名及后缀
        :param sheet_name: 要遍历的参数sheet页名字
        """
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*'}
        self.file = path.API_DOCUMENT + '/' + filepath
        self.data = xlrd.open_workbook(self.file)
        self.sheet_name = sheet_name

        self.exec_queue = [self.sheet_name]  # 接口执行队列
        self.rely_data = {}  # 获取接口返回数据的表达式
        self.rely = {}  # 存放接口的依赖数据

        """
        1、把post单独封装，在函数内判断应该使用什么样的请求。所需的判断条件全部放在初始化方法中
        2、把断言单独封装，实现将断言< > =写在文档中。
        """




    #  获取sheet页下的所有数据
    def _get_all_data(self, name=None):
        """
        读取Excel里配置好的接口数据
        """
        sheet_name = ""
        if name == None:
            sheet_name = self.sheet_name
        else:
            sheet_name = name

        table = self.data.sheet_by_name(sheet_name)
        nor = table.nrows  # 行
        nol = table.ncols  # 列
        data = {}
        dict = {}
        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)
                value_type = table.cell(i, j).ctype  # ctype : 0 空,1 字符串, 2 数字, 3 date, 4 布尔, 5 错误

                # 如果ctype为2，转换成整型
                if value_type == 2 and value % 1 == 0.0:
                    value = int(value)
                    if value == 0.0:
                        value = int(value)
                # 如果ctype为3，格式化日期
                elif value_type == 3:
                    value = xlrd.xldate_as_datetime(table.cell(i, j).value, 0).strftime("%Y/%m/%d")

                # 判断是否是参数，如果是参数就放入data内。否则放到dict中
                if title.isupper():
                    dict[title] = value
                else:
                    data[title] = value

            # 参数的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”，如果读取的值是time就转换成当前时间
            t = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
            for k in list(data.keys()):
                # 值为空时删除该键值对，，模拟接口测试中不传该参数
                if not data[k]:
                    del data[k]

                # 如果值为null时把值改成  “”  ，模拟接口测试中该参数不传值
                elif data[k] == 'null':
                    data[k] = ''

                # 如果值中是time就转换成当前时间
                elif data[k] == 'time':
                    data[k] = t

            dict["data"] = data
            yield dict

    #  获取接口间的依赖关系
    def _get_exec_queue(self):
        """
获取执行队列
        """
        for i in self.exec_queue:
            for j in self._get_all_data(i):

                # 判断接口是否有依赖接口 如果有就将依赖的接口加入到执行队列
                if j["RELY_API"] != "":
                    self.exec_queue.append(j["RELY_API"])

                    # 判断是否需要依赖接口的返回数据，如果需要将依赖的数据添加到rely_data中
                    if j["RELY_VALUE"] != "":
                        self.rely_data[j["RELY_API"]] = j["RELY_VALUE"]
                else:
                    self.exec_queue.reverse()
                    break

    # post请求
    def post(self, session, url, data, file=None, data_type="data"):
        """
        :param session: 请求的会话对象
        :param url: 请求地址
        :param data: 请求的数据
        :param file: 要上传的文件（转码以后的）
        :param data_type: 请求的参数类型（data或者json）
        :return:
        """
        response = ""

        if data_type == "data" and file == None:
            response = session.post(url=url, data=data)

        elif data_type == "data" and file != None:
            response = session.post(url=url, data=data, files=file)

        elif data_type == "json" and file != None:
            response = session.post(url=url, json=data, files=file)

        elif data_type == "json" and file == None:
            response = session.post(url=url, json=data)

        print(response.text)
        return response.json()

    #  运行测试
    def run(self):
        """
根据接口文档信息自动运行对应的请求请求
        """
        url = ""
        method = ""
        self._get_exec_queue()  # 获取执行队列（接口依赖关系）
        print("当前的接口执行队列是： {}".format(self.exec_queue))
        print("当前的接口依赖数据是： {}".format(self.rely_data))
        session = ""  # 会话对象
        response = ""  # 接口响应
        response_json = ""  # 接口响应json
        uploadFile = False  # 是否上传文件
        data_type = "data"  # 请求数据的类型
        data = ""  # 请求传递的数据
        upload_file = ""

        for i in self.exec_queue:  # 遍历执行队列
            for j in self._get_all_data(i):  # 遍历单个接口所有数据
                # 判断传递的参数是否是json
                if "json" in j["data"]:
                    data = eval(j["data"]["json"])
                    data_type = "json"
                else:
                    data = j["data"]

                # 判断是否需要上传文件
                if j["FILE"] != "":
                    uploadFile = True
                    upload_info = j["FILE"].split("-")
                    filePate = path.UPLOAD_DIR + "/" + upload_info[1]
                    upload_file = {upload_info[0]: open(filePate, 'rb')}

                # 初始化环境
                if j["INITIALIZE"] != "":
                    database = j["INITIALIZE"].split("-")
                    if database[0] == "mysql":
                        operation_mysql(database[1])
                    else:
                        operation_oracle(database[1])

                # 请求地址和请求方法在单个用例内数据持久化
                if j["URL"] != "":
                    url = j["URL"]
                    method = j["METHOD"]

                # 判断是否需要使用特定的用户登录后操作
                if j["RELY_USER"] == "":
                    session = requests.Session()
                else:
                    userInfo = j["RELY_USER"].split("-")
                    session = self.add_session(userInfo)

                # 将被依赖接口的返回数据添加到对应的接口请求参数中
                for before in j["data"].keys():
                    for existing in self.rely.keys():
                        if existing == before:
                            j["data"][before] = self.rely[existing]

                # 判断是否是依赖执行，如果是只执行正向的测试数据
                if self.exec_queue[-1] != i:
                    # 判断是否是正向测试用例
                    if j["TYPE"] != "":
                        print("当前运行的依赖接口是{}".format(i))

                        # 判断请求的方法
                        if method == "get":
                            try:
                                response = session.get(url=url, params=data)
                                print(response.json())

                                response_json = response.json()
                                assert eval(j["RESULT"]) == j["EXPECT"]
                            except Exception as e:
                                raise e

                        elif method == "post":
                            if data_type == "json" and uploadFile == False:
                                try:
                                    response_json = self.post(session, url, data, data_type="json")
                                    print(response_json)
                                    assert eval(j["RESULT"]) == j["EXPECT"]
                                except Exception as e:
                                    raise e

                            elif data_type == "data" and uploadFile == False:
                                try:
                                    response_json = self.post(session, url, data, data_type="data")
                                    print(response_json)
                                    assert eval(j["RESULT"]) == j["EXPECT"]
                                except Exception as e:
                                    raise e

                            elif data_type == "json" and uploadFile == True:
                                try:
                                    response_json = self.post(session, url, data, file=upload_file, data_type="json")
                                    print(response_json)
                                    assert eval(j["RESULT"]) == j["EXPECT"]
                                except Exception as e:
                                    raise e

                            elif data_type == "data" and uploadFile == True:
                                try:
                                    response_json = self.post(session, url, data, file=upload_file, data_type="data")
                                    print(response_json)
                                    assert eval(j["RESULT"]) == j["EXPECT"]
                                except Exception as e:
                                    raise e

                        # 判断是否需要接口的返回数据
                        for key in self.rely_data.keys():
                            if key == i:
                                get_result_str = self.rely_data[i].split("-")  # 获取返回数据的表达式
                                if len(get_result_str) > 2:  # 大于2时证明获取数据需要条件
                                    where = get_result_str[2].split("=")
                                    # 获取结果的条件
                                    key = where[0]
                                    value = where[1]

                                    # 判断获取数据的元素是否是列表或者字典
                                    if type(eval(get_result_str[0])) == list:
                                        for v in eval(get_result_str[0]):
                                            if v[key] == value:
                                                self.rely[get_result_str[1]] = v[get_result_str[1]]

                                else:  # 没有符合条件的接口，未验证
                                    self.rely[get_result_str[1]] = eval(get_result_str[0])[get_result_str[1]]



                else:  # 不是依赖执行，遍历所有测试参数
                    print("当前运行的接口是：{}".format(i))
                    if method == "post":
                        if data_type == "json" and uploadFile == False:
                            try:
                                response_json = self.post(session, url, data, data_type="json")
                                print(response_json)
                                assert eval(j["RESULT"]) == j["EXPECT"]
                            except Exception as e:
                                raise e

                        elif data_type == "data" and uploadFile == False:
                            try:
                                response_json = self.post(session, url, data, data_type="data")
                                print(response_json)
                                assert eval(j["RESULT"]) == j["EXPECT"]
                            except Exception as e:
                                raise e

                        elif data_type == "json" and uploadFile == True:
                            try:
                                response_json = self.post(session, url, data, file=upload_file, data_type="json")
                                print(response_json)
                                assert eval(j["RESULT"]) == j["EXPECT"]
                            except Exception as e:
                                raise e

                        elif data_type == "data" and uploadFile == True:
                            try:
                                response_json = self.post(session, url, data, file=upload_file, data_type="data")
                                print(response_json)
                                assert eval(j["RESULT"]) == j["EXPECT"]
                            except Exception as e:
                                raise e

                    elif method == "get":
                        try:
                            response = session.get(url=url, params=data)
                            print(response.json())
                            response_json = response.json()
                            assert eval(j["RESULT"]) == j["EXPECT"]
                        except Exception as e:
                            raise e


                # 数据库断言
                if j["DATABASE_ASSERT"] != "":
                    result = ""
                    try:
                        database = j["DATABASE_ASSERT"].split("-")
                        if database[0] == "mysql":
                            result = operation_mysql(database[1])
                        else:
                            result = operation_oracle(database[1])
                        print(result)
                        for l in result:
                            for ii in l.keys():
                                assert l[ii] == database[2]
                    except Exception as e:
                        raise e

                # 环境还原
                if j["RESTORE"] != "":
                    database = j["RESTORE"].split("-")
                    if database[0] == "mysql":
                        operation_mysql(database[1])
                    else:
                        operation_oracle(database[1])

        self.exec_queue.clear()  # 清空执行队列

    # 创建会话对象
    def add_session(self, userInfo):
        userNameKey = userInfo[0].split("=")[0]
        userNameValue = userInfo[0].split("=")[1]

        pwdKey = userInfo[1].split("=")[0]
        pwdValue = userInfo[1].split("=")[1]
        r = ""

        for i in self._get_all_data("login"):
            if i["TYPE"] != "":
                i["data"][userNameKey] = userNameValue
                i["data"][pwdKey] = pwdValue
                r = requests.Session()
                response = r.post(url=i["URL"], data=i["data"])
        return r


if __name__ == '__main__':
    # data = Base_api('guns.xlsx', "del_user")
    # data = Base_api('ui-autotest.xlsx', "login")
    # data = Base_api('ui-autotest.xlsx', "upload")
    # data = Base_api('performance-autotest.xlsx', "login")
    data = Base_api('performance-autotest.xlsx', "search-system")
    data.run()
    # data.add_session(aa)
