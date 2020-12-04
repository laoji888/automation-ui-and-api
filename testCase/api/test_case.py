from common import path
from common.base_api import Base_api
import pytest, os, sys

class Test_case():

    def test_t01(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        sys.path.append(BASE_DIR)
        if not os.path.exists(path.TEST_REPORT): os.mkdir(path.TEST_REPORT)
        if not os.path.exists(path.AULLURE_RESULT): os.mkdir(path.AULLURE_RESULT)
        data = Base_api('guns.xlsx', "del_user")
        data.run()

if __name__ == '__main__':

    pass
