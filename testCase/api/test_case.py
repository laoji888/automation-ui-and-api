from common.base_api import Base_api
import pytest

class Test_case():

    def test_t01(self):
        data = Base_api('guns.xlsx', "del_user")
        data.run()

    def test_t02(self):
        data = Base_api('guns.xlsx', "del_user")
        data.run()

if __name__ == '__main__':

    pytest.main(" --html report.html")
