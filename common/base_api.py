import datetime
from common.logger import log
import xlrd, requests, unittest, time, json
from common import path
from common.util import get_config_info, operation_mysql, operation_oracle

log = log(logname="api")


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
        self.rely_data = {}                  # 获取接口返回数据的表达式
        self.rely = {}                       # 存放接口的依赖数据
        self.session = ""                    # 会话对象
        self.uploadFile = False              # 是否上传文件
        self.data_type = "data"              # 请求数据的类型
        self.parameter = ""                  # 请求传递的数据
        self.upload_file = ""                # 要上传的文件
        self.url = ""                        # 请求地址
        self.method = ""                     # 请求方法
        self.assert_data = ""                # 断言数据
        self.response_json = ""              # 接口返回的json数据

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
        row = table.nrows   # 行数
        ncol = table.ncols  # 列数
        data = {}           # 请求参数
        dict = {}           # 请求时需要的其他参数

        for i in range(1, row):
            for j in range(ncol):
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

    # 获取执行队列
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
        log.info("获取的执行队列是：{}".format(self.exec_queue))
        log.info("当前的接口依赖数据是： {}".format(self.rely_data))

    # post请求
    def post(self):
        response = ""
        try:
            # 参数是字典，不上传文件
            if self.data_type == "data" and self.upload_file == "":
                response = self.session.post(url=self.url, data=self.parameter)

            # 参数是字典，上传文件
            elif self.data_type == "data" and self.upload_file != "":
                response = self.session.post(url=self.url, data=self.parameter, files=self.upload_file)

            # 参数是json，上传文件
            elif self.data_type == "json" and self.upload_file != "":
                response = self.session.post(url=self.url, json=self.parameter, files=self.upload_file)

            # 参数是json，不上传文件
            elif self.data_type == "json" and self.upload_file == "":
                response = self.session.post(url=self.url, json=self.parameter)
            log.debug("运行post请求成功，请求的参数是：{}".format(self.parameter))
            log.info("运行post请求成功")
        except Exception as e:
            log.error("post请求失败！，错误信息是：{}".format(e))
            log.error("post请求失败！，请求的参数是：{}".format(self.parameter))
            raise e

        return response.json()

    # get请求
    def get(self):
        response = ""
        try:
            response = self.session.get(url=self.url, params=self.parameter)
            log.info("运行get请求成功")
        except Exception as e:
            log.error("get请求失败！，错误信息是：{}".format(e))
            log.error("get请求失败！，请求参数是：{}".format(self.parameter))

        return response.json()

    # 检查点
    def verify(self):
        assert_data = self.assert_data.split(" ")
        expect = ""
        if assert_data[2].isdigit():
            expect = int(assert_data[2])
        else:
            expect = assert_data[2]

        try:
            if assert_data[1] == "==":
                assert eval(assert_data[0]) == expect

            elif assert_data[1] == "<":
                assert eval(assert_data[0]) < expect

            elif assert_data[1] == ">":
                assert eval(assert_data[0]) > expect

            elif assert_data[1] == "in":
                assert expect in eval(assert_data[0])

            elif assert_data[1] == "!=":
                assert eval(assert_data[0]) != expect
            log.info("检查点校验成功")
            log.info("\n")
        except Exception as e:
            log.error("检查点检验失败！预期结果是：{}，实际结果是：{}".format(self.assert_data,
                                                         assert_data[0] + " " + assert_data[1] + " " +  eval(assert_data[0])))
            raise e

    # 运行测试
    def run(self):
        """
根据接口文档信息自动运行对应的请求请求
        """
        self._get_exec_queue()  # 获取执行队列（接口依赖关系）

        # 遍历执行队列
        for i in self.exec_queue:
            # 遍历单个接口所有数据
            for j in self._get_all_data(i):

                self.assert_data = j["ASSERT"]

                # 判断传递的参数是否是json
                if "json" in j["data"]:
                    self.parameter = eval(j["data"]["json"])
                    self.data_type = "json"
                else:
                    self.parameter = j["data"]

                # 判断是否需要上传文件
                if j["FILE"] != "":
                    self.uploadFile = True
                    upload_info = j["FILE"].split("-")
                    filePate = path.UPLOAD_DIR + "/" + upload_info[1]
                    self.upload_file = {upload_info[0]: open(filePate, 'rb')}

                # 初始化环境
                if j["INITIALIZE"] != "":
                    database = j["INITIALIZE"].split("-")
                    if database[0] == "mysql":
                        operation_mysql(database[1])
                    else:
                        operation_oracle(database[1])

                # 请求地址和请求方法在单个用例内数据持久化
                if j["URL"] != "":
                    self.url = j["URL"]
                    self.method = j["METHOD"]

                # 判断是否需要使用特定的用户登录后操作
                if j["RELY_USER"] == "":
                    self.session = requests.Session()
                else:
                    userInfo = j["RELY_USER"].split("-")
                    self.session = self.add_session(userInfo)

                # 将被依赖接口的返回数据添加到对应的接口请求参数中
                for before in j["data"].keys():
                    for existing in self.rely.keys():
                        if existing == before:
                            j["data"][before] = self.rely[existing]

                # 判断是否是依赖执行，如果是只执行正向的测试数据
                if self.exec_queue[-1] != i:
                    # 判断是否是正向测试用例
                    if j["TYPE"] != "":

                        # 判断请求的方法
                        if self.method == "get":
                            self.response_json =self.get()

                            self.verify()

                        elif self.method == "post":
                            self.response_json = self.post()

                            self.verify()

                        # 获取依赖数据
                        for key in self.rely_data.keys():
                            if key == i:
                                get_result_str = self.rely_data[i].split("-")  # 获取返回数据的表达式
                                if len(get_result_str) > 2:  # 大于2时证明获取数据需要条件
                                    where = get_result_str[2].split("=")
                                    # 获取结果的条件
                                    where_key = where[0]
                                    where_value = where[1]

                                    # 判断获取数据的元素是否是列表或者字典
                                    if type(eval(get_result_str[0])) == list:
                                        for v in eval(get_result_str[0]):
                                            if v[where_key] == where_value:
                                                self.rely[get_result_str[1]] = v[get_result_str[1]]

                                else:  # 没有符合条件的接口，未验证
                                    self.rely[get_result_str[1]] = eval(get_result_str[0])[get_result_str[1]]



                else:  # 不是依赖执行，遍历所有测试参数
                    print("当前运行的接口是：{}".format(i))
                    if self.method == "post":
                        self.response_json = self.post()

                        self.verify()

                    elif self.method == "get":
                        self.response_json = self.get()

                        self.verify()


                # 数据库断言
                if j["DATABASE_ASSERT"] != "":
                    result = ""
                    try:
                        database = j["DATABASE_ASSERT"].split("-")
                        if database[0] == "mysql":
                            result = operation_mysql(database[1])
                        else:
                            result = operation_oracle(database[1])

                        for l in result:
                            for ii in l.keys():
                                assert l[ii] == database[2]
                        log.info("数据库检查点校验成功")
                    except Exception as e:
                    # 单独封装数据库检查点
                        raise e

                # 环境还原
                if j["RESTORE"] != "":
                    database = j["RESTORE"].split("-")
                    if database[0] == "mysql":
                        operation_mysql(database[1])
                    else:
                        operation_oracle(database[1])
            log.info("当前请求的接口是：{},参数传递方式是：{}".format(i,self.data_type))
            log.info("当前的接口请求数据是：{}".format(self.parameter))
            log.info("当前接口返回数据是：{}".format(self.response_json))

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
    data = Base_api('guns.xlsx', "del_user")
    # data = Base_api('ui-autotest.xlsx', "login")
    # data = Base_api('ui-autotest.xlsx', "upload")
    # data = Base_api('performance-autotest.xlsx', "login")
    # data = Base_api('performance-autotest.xlsx', "search-system")
    data.run()

