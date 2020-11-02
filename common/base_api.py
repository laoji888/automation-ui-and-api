import datetime
from common.logger import log
import xlrd, requests, unittest, time, json, pymysql
from common import path

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
        self.sheet_name = sheet_name
        self.data = xlrd.open_workbook(self.file)
        self.nrow = 1
        self.ast = unittest.TestCase()  # 使用unittest框架下的断言

        # 接口地址
        self.url = ""  # 请求地址
        self.parameter = {}  # 请求参数
        self.method = ""  # 请求方法
        self.cmd = ""  # 获取实际结果的命令
        self.expect = ""  # 预期结果

        self.exec_queue = [self.sheet_name]  # 接口执行队列

    #  获取sheet页下的所有数据
    def _get_all_data(self, name):
        """
        读取Excel里配置好的接口数据
        """
        table = self.data.sheet_by_name(name)
        log.debug("打开:{},下的[{}]页".format(self.file, name))
        nor = table.nrows  # 行
        nol = table.ncols  # 列
        dict = {}

        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)

                value_type = table.cell(i, j).ctype
                if value_type == 2 and value % 1 == 0.0:  # 如果ctype为2且取余于1等于0.0，转换成整型
                    value = int(value)
                    log.debug("获取到的参数是小数：%s,已转换成整型" % value)
                    if value == 0.0:
                        value = int(value)
                    log.debug("获取到的参数是：%s，已转换成整型" % value)

                dict[title] = value
                log.debug("获取到的参数名是:%s,参数值是:%s" % (title, value))
            yield dict

    #  获取接口间的依赖关系
    def _get_exec_queue(self):
        """
获取执行队列
        """
        for i in self.exec_queue:
            for j in self._get_all_data(i):
                if j["rely"] != "":
                    self.exec_queue.append(j["rely"])
                else:
                    self.exec_queue.reverse()
                    break

    #  运行测试
    def run(self):
        """
根据接口文档信息自动运行对应的请求请求
        """
        self._get_exec_queue() # 获取执行队列（接口依赖关系）

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

                else: # 不是依赖执行，遍历所有测试场景
                    self.url = j["url"]
                    self.method = j["method"]
                    self.cmd = j["cmd"]
                    self.expect = j["expect"]

                    del j["url"]
                    del j["method"]
                    del j["cmd"]
                    del j["expect"]
                    self.parameter = j

                    r = requests.post(self.url, data=self.parameter)
                    print("zhixing tyikljljk")
                    print(r.text)
                    print(r.status_code)
                    self.exec_queue.remove(i)

        '''
        执行接口测试思路：
            判断是否是依赖执行的，如果是只执行第一行的正向测试用例，否则全部执行。
            判断self.exec_queue的个数实现，如果大于1个元素就是依赖执行，否则不是，执行完依赖执行后删除self.exec_queue中已执行的元素
        '''

    # 读取excl，获得实际结果命令和预期结果
    def get_assert(self, nrow, ncol=0):
        """
        读取接口的预期结果和获取实际结果的命令
        :param nrow: 要读取的行数
        :param ncol: 要读取的列数，默认是0
        :return: 返回读取的数据
        """
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheet_by_index(self.assert_sheet)
        log.debug("打开文件:%s的第%s页获取断言信息" % (self.dir_case, self.assert_sheet))
        value = table.cell_value(nrow, ncol)

        value_type = table.cell(nrow, ncol).ctype
        if value_type == 2 and value % 1 == 0.0:  # 如果ctype为2且取余于1等于0.0，转换成整型
            log.debug("获取到的断言类型是小数：%s,已装换成整型" % value)
            value = int(value)
            if value == 0.0:
                value = int(value)
            log.debug("获取到的断言是0.0，已转换成整型")
        log.info("断言信息获取成功：%s" % value)
        return value

    # 遍历字典的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”。如果不传参数Excel为空即可，如果想参数值为空就写null。
    def set_dict(self, data):
        """
        遍历字典的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”，空值不等于null,如果读取的值是time就转换成当前时间
        :param data: 要遍历的字典
        :return: 返回删除空值的键值对后的字典
        """

        t = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        xx = data
        for k in list(data.keys()):
            if not data[k]:
                log.debug("获取到的键：%s 的值为空，删除该键值对" % data[k])
                del data[k]

            elif data[k] == 'null':
                data[k] = ''
                log.debug("获取到的键：%s 的值为 null，把该键的值设置为空" % data[k])

            elif data[k] == 'time':
                data[k] = t
                log.debug("获取到的键：%s 的值为 time，把该键的值设置为当前时间" % data[k])
        log.info("参数格式化成功")

        return xx

    # 创建会话对象
    def add_session(self):
        log.debug("获取到登录url为：%s" % (self.s_url))
        log.debug("获取到登录的参数为：%s" % (self.s_data))
        s = requests.session()
        log.debug("登录请求成功")
        response = s.get(url=self.s_url, params=self.s_data)
        response_json = response.json()

        try:
            token = response_json['data']['token']
            self.header['token'] = token
            log.debug("获取到的token是：%s" % token)
            log.info("token已添加到heder")
        except:
            log.debug("返回值中没有token")
            pass

        return s

    # 运行get请求
    def run_get(self):
        s = self.add_session()
        for i in Base_api.get_data(self):
            url = self.get_url()
            data = Base_api.set_dict(self, i)
            response = s.get(url, params=data, headers=self.header)
            result = self.get_assert(self.nrow)  # 实际结果命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            self.nrow = self.nrow + 1
            ast = self.nrow - 1  # 现在调用的行数
            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                log.info(result)
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("get请求成功")

    # 运行post请求
    def run_post(self):
        s = self.add_session()
        for i in Base_api.get_data(self):
            url = self.get_url()
            data = Base_api.set_dict(self, i)  # 调用函数，清除值为空的键值对
            response = s.post(url, data=data)
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
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")

    # 运行post请求，参数为json
    def run_post_json(self):
        """
        post请求，请求参数为json，参数以字典的方式存在每行的第一列
        :return:
        """
        self.header['Content-Type'] = "application/json;charset=UTF-8"
        s = self.add_session()
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheets()[self.param]
        nrows = table.nrows
        url = self.get_url()

        for i in range(1, nrows):
            data_list = table.row_values(i)
            data_str = str(data_list)
            data_str = data_str.strip("[]")
            data_str = data_str.strip("'")
            data_dict = json.loads(data_str)

            response = s.post(url=url, json=data_dict, headers=self.header)
            result = self.get_assert(self.nrow)  # 获取实际结果的命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            log.info("调用第%s行，命令是：%s，预期结果是：%s" % (self.nrow, result, expect))
            self.nrow = self.nrow + 1
            ast = self.nrow - 1
            log.info(response.json())
            log.info(response.text)

            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")

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
    run = Base_api('autotest.xlsx', "add_app")
    run.run() # 现在可以获取文档依赖关系。


