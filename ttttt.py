import requests

# r = requests.Session()
# filePate = "C:\\Users\\jiyanan\\Desktop\\appium-hub-start.bat"
# file = {'uploadFile': open(filePate, 'rb')}
# dd = {"login_name":"admin","passwd":"newland@1234"}
# r.post(url="http://120.52.96.35:49000/autotest_sv/login",data=dd)
#
# data = {"pageNum":1,"pageSize":10,"totalRecord":51,"testSystemName":"测试报告用","testSystemIp":""}
# cc = r.post(url="http://120.52.96.35:49000/autotest_sv/testSystem/queryPage",json=data)
# print(cc.text)


data = '{"pageNum":1,"pageSize":10,"totalRecord":51,"testSystemName":"测试报告用","testSystemIp":""}'
print(type(data))
print(type(eval(data)))

