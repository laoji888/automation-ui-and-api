

from common.base_api import Base_api

import unittest, warnings


class Api_tese(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.url = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
        self.data = {'username': 'qiaolin', 'password': '8579173b7f0ad165551bf8e892d3dee7'}

    # 登录接口测试
    def test_login(self):
        run = Base_api(self.url, self.data, 'single.xlsx', 0, 1)
        run.run_get()

    #  添加商机 参数是json数据
    # def test_as(self):
    #     run = base(self.url, self.data, 'single.xlsx', 2, 3)
    #     run.run_post_json()

    # 文件上传
    # def test_as(self):
    #     run = api_base.base(self.url, self.data, 'single.xlsx', 4, 5)
    #     run.run_post_upload()


    # def test_changjing(self):
    #
    #     run = base(self.url, self.data, 'single.xlsx', 6, 7)
    #     run.run_post_json()

    # 商机查询接口


    # 商机查询接口

    # 遍历商机查询接口
    def test_s(self):
        run = base(self.url, self.data, 'single.xlsx', 8, 9)
        run.run_get()

    # 遍历合作成果查询接口
    def test_ss(self):
        run = base(self.url, self.data, 'single.xlsx', 10, 11)
        run.run_post_json()


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
