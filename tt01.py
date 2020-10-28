
import time
from test01 import multiprocess

class aa:

    @multiprocess
    def tt(self,name):
        print(name)

if __name__ == '__main__':
    aa().tt()