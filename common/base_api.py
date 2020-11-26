import datetime
from common.logger import log
import xlrd, requests, unittest, time, json, pymysql, pytest
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
        self.nrow = 1
        self.ast = unittest.TestCase()  # 使用unittest框架下的断言
        self.sheet_name = sheet_name
        self.url = ""  # 请求地址
        self.method = ""  # 请求方法

        self.exec_queue = [self.sheet_name]  # 接口执行队列

    #  获取sheet页下的所有数据
    def _get_all_data(self, name=None):
        """
        读取Excel里配置好的接口数据
        """
        sheet_name = ""
        if name ==None:
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
                value_type = table.cell(i, j).ctype

                # 如果ctype为2且取余于1等于0.0，转换成整型
                if value_type == 2 and value % 1 == 0.0:
                    value = int(value)
                    if value == 0.0:
                        value = int(value)

                # 判断是否是参数，如果是参数就放入data内。否则放到dict中
                if title.isupper():
                    dict[title] = value
                else:
                    data[title] = value

            #参数的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”，如果读取的值是time就转换成当前时间
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
                if j["RELY_API"] != "":
                    self.exec_queue.append(j["RELY_API"])
                else:
                    self.exec_queue.reverse()
                    break

    #  运行测试
    def run(self):
        """
根据接口文档信息自动运行对应的请求请求
        """
        rely = []  # 存放接口的依赖数据
        self._get_exec_queue() # 获取执行队列（接口依赖关系）
        session = ""
        for i in self.exec_queue: # 遍历执行队列
            for j in self._get_all_data(i): # 遍历单个接口所有数据
                if self.exec_queue[-1] != i: # 依赖执行，只执行第一行
                    if j["url"] != "": # 判断是不是第一行
                        self.url = j["url"]
                        self.method = j["method"]
                        self.cmd = j["cmd"]
                        self.expect = j["expect"]

                        del j["url"]
                        del j["method"]
                        del j["cmd"]
                        del j["expect"]
                        del j["rely"]
                        self.parameter = j
                        if self.method == "post": # 判断请求的方法
                            r = requests.post(self.url, data=self.parameter)
                            print(r.text)
                            print(r.status_code)
                            print(self.exec_queue)
                            print("执行liogin")

                else: # 不是依赖执行，遍历所有测试参数
                    # 执行sql语句
                    if j["SQL"] != "":
                        database = j["SQL"].split("-")
                        if database[0] == "mysql":
                            operation_mysql(database[1])
                        else:
                            operation_oracle(database[1])

                    # 判断是否需要使用特定的用户登录后操作
                    if j["USERNAME"] == "":
                        session = requests.Session()
                    else:
                        user = {"username":j["USERNAME"],"password":j["PASSWORD"]}
                        session = self.add_session(user)

                    # 请求参数
                    url = j["URL"]
                    method = j["METHOD"]
                    data = j["data"]

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
                        try:
                            response = session.post(url=url,data=data)
                            print(response.json())
                            response_json = response.json()
                            assert eval(j["RESULT"]) == j["EXPECT"]
                        except Exception as e:
                            raise e
            self.exec_queue.remove(i)

        '''
        执行接口测试思路：
            判断是否是依赖执行的，如果是只执行第一行的正向测试用例，否则全部执行。
            判断self.exec_queue的个数实现，如果大于1个元素就是依赖执行，否则不是，执行完依赖执行后删除self.exec_queue中已执行的元素
        '''

    # 创建会话对象
    def add_session(self,user):
        r = requests.Session()
        response = r.post(url=get_config_info("API-URL",key="login",filename="api_config.ini"), data=user)
        print(response.json())
        # try:
        #     token = response_json['data']['token']
        #     self.header['token'] = token
        #     log.debug("获取到的token是：%s" % token)
        #     log.info("token已添加到heder")
        # except:
        #     log.debug("返回值中没有token")
        #     pass
        return r

    # post请求，上传文件
    def run_post_upload(self, file="file.txt"):
        """
        上传文件
        :param file: 上传的文件名
        """
        s = self.add_session()
        for i in Base_api.get_data(self):
            url = self.get_url()
            data = Base_api.set_dict(self, i)  # 调用函数，清除值为空的键值对
            filePate = path.BASE_DIR + "/" + file
            file = {'file': open(filePate, 'rb')}
            response = s.post(url=url, data=data, files=file)
            result = self.get_assert(self.nrow)  # 获取实际结果的命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            log.info("调用第%s行，命令是：%s，预期结果是：%s" % (self.nrow, result, expect))
            self.nrow = self.nrow + 1
            ast = self.nrow - 1

            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet + 1, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")


if __name__ == '__main__':
    data = Base_api('autotest-api.xlsx',"login")
    data.run()









