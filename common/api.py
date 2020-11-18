
import requests,time


class Api:
    def __init__(self,username="admin",passwd="000000"):
        self.heads = {'User-Agent':
                          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                      "Content-Type": "application/x-www-form-urlencoded"}

        self.username = username
        self.passwd = passwd
        self.session = self.get_session()



    def get_session(self):
        s = requests.Session()
        s.verify = False
        r = s.post(url="http://42.192.22.244:8899/zentao/user-login.html",
                            data={"account":"admin","password":"1qaz@WSX","zentaosid":"d2kg377sdubbo18jk71jm39nd2"},
                            headers=self.heads)
        print(r.text)



    def post(self,url,data,default_timeout=10):
        r = self.session().post(url=url,
                          data=data,timeout=default_timeout)

        return r


if __name__ == '__main__':
    # Api().post("http://42.192.22.244:8080/AppAutoTest/appinfo/deleteAppInfo.do",
    #           {
    #               "model": "{'appId':'231'}"})
    Api().get_session()