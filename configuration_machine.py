import json, subprocess, requests, re


class configuration:
    # 平台已配置的设备详细信息
    equipment_list_info = []
    # 平台已配置的设备名称列表
    equipment_list = []

    # 已连接的android执行设备列表
    android_existing_equipment = []
    # 已连接的ios执行设备列表
    ios_existing_equipment = []

    # 新插入的ios设备信息
    ios_name = ""
    ios_identification = ""
    ios_version = ""
    ios_udid = ""
    ios_host = ""

    # 新的安卓设备
    android_identification = ""
    android_name = ""
    android_version = ""
    android_host = ""

    # 执行shell命令，返回结果
    def cmd(self, command):
        x = subprocess.getoutput(command)
        return x
    a = False

    # 获取ios设备信息，判断自动化测试平台是否已经配置了该设备。如果未配置将新设备配置到平台。
    def add_ios(self):
        self.ios_udid = self.cmd("idevice_id -l")
        self.ios_name = self.cmd("ideviDcename -u " + self.ios_udid)
        self.ios_version = self.cmd("ideviceinfo -u " + self.ios_udid + " -k ProductVersion")

        # 获取平台已配置的ios设备列表
        self.get_equipment_info(equipment_type="ios")

    # 获取Android设备信息，判断自动化测试平台是否已经配置了该设备。如果未配置将新设备配置到平台。
    def add_android(self):
        list1 = []
        s = self.cmd("adb devices")
        pattern = ".*"
        name = re.findall(pattern, s)
        name.remove("List of devices attached")

        # 提取已连接的设备名称
        for i in name:
            if bool(re.search('[a-z]', i)) or bool(re.search('[0-9]', i)):
                list1.append(i)

        for i in list1:
            list2 = list(i)
            for j in list2:
                if j == "\t":
                    index = list2.index(j)
                    del list2[index:]
            element = "".join(list2)
            self.android_existing_equipment.append(element)
        print("已连接的设备名称： ", self.android_existing_equipment)

        # 获取自动化测试平台已配置的设备列表
        self.get_equipment_info('android')

        # 获取没有配置到平台的设备
        new_equipment = list(set(self.android_existing_equipment).difference(set(self.equipment_list)))  # 没有配置到平台的设备名称
        print("没有配置到平台的设备名称：", new_equipment)
        if len(new_equipment) == 0:
            print("没有发现未配置到平台的android设备")
            return
        elif len(new_equipment) > 0:
            print("发现未配置到平台的Android设备", new_equipment)

        # 发送请求向自动化测试平台添加安卓设备
        for i in new_equipment:
            self.android_name = self.cmd("adb -s " + i + " shell getprop ro.config.marketing_name")
            if self.android_name.strip()=='':
                self.android_name = i
            self.android_identification = i
            self.android_version = self.cmd("adb -s " + i + " shell getprop ro.build.version.release")
            self.android_host = "http://123.127.238.246:" + self.build_host() + "/wd/hub"
            self.add_equipment("android")
        print("本次共计添加android设备:" + str(len(new_equipment)) + "台")

    # 构建调用地址
    def build_host(self):
        list01 = []
        self.get_equipment_info()

        # 构建新添加的设备调用地址的端口。规则为：端口号=现有的设备数量加一（端口号从4700-4799），
        for j in range(len(self.equipment_list_info)):
            for k, v in self.equipment_list_info[j].items():
                if k == "appiumUrl":
                    if self.equipment_list_info[j][k].find("http://123.127.238.246") != -1:
                        list01.append(self.equipment_list_info[j][k])
        num = len(list01) + 1

        if len(str(num)) == 1:
            num = "0" + str(num)

        return "47" + num

    # 获取ui自动化测试平台执行设备列表
    def get_equipment_info(self, equipment_type=""):
        # 根据平台类型配置请求信息
        key = ""
        data = {}
        if equipment_type == "android":
            key = "deviceIdentification"
            data = {
                "model": '{"platformName":"Android","pageNumber":1,"pageSize":100,"deviceName":null,"appiumUrl":null}'}
        elif equipment_type == "ios":
            key = "udid"
            data = {
                "model": '{"platformName":"iOS","pageNumber":1,"pageSize":100,"deviceName":null,"appiumUrl":null}'}
        # 不传参数时默认获取所有执行设备
        elif equipment_type == "":
            data = {
                "model": '{"pageNumber":1,"pageSize":100,"deviceName":null,"appiumUrl":null}'}

        # 请求自动化测试平台接口，获取执行设备列表，如果是安卓要提取deviceIdentification，ios要提udid，输出到equipment_name_list
        result = requests.post(url="http://119.3.193.39:8018/AppAutoTest/deviceinfo/getDeviceInfoList.do",
                               data=data)
        response = json.loads(result.text)
        self.equipment_list_info = response["rows"]

        # 将设备名称添加到列表
        self.equipment_list.clear()
        for i in self.equipment_list_info:
            for k, v in i.items():
                if k == key:
                    self.equipment_list.append(i[k])

    # 请求接口，添加执行设备
    def add_equipment(self, equipment_type):
        data = {}
        if equipment_type == "android":
            data = {
                "model":
                    '{"deviceName":"' + self.android_name +
                    '","deviceIdentification":"' + self.android_identification +
                    '","platformName":"Android","platformVersion_input_a":"' + self.android_version +
                    '","platformVersion_combox_a":null,"udid":null,"unicodeKeyboard":"true","resetKeyboard":"true",'
                    '"appiumUrl":"' + self.android_host +
                    '","platformVersion":"' + self.android_version + '"}'}
        elif equipment_type == "ios":
            data = {
                "model":
                    '{"deviceName":"' + self.ios_name +
                    '","deviceIdentification":"' + self.ios_identification +
                    '","platformName":"iOS","platformVersion_input_a":"' + self.ios_version +
                    '","platformVersion_combox_a":null,"udid":' + self.ios_udid +
                    '","unicodeKeyboard":"true","resetKeyboard":"true","appiumUrl":"' + self.ios_host +
                    '","platformVersion":"' + self.ios_version + '"}'}

        # 发送请求添加设备
        r = requests.post(url="http://119.3.193.39:8018/AppAutoTest/deviceinfo/addDeviceInfo.do",
                          data=data)
        if r.text.find("添加成功"):
            print(self.android_name + "-->添加成功")

    def get_new_equipment_info(self):
        self.ios_udid = self.cmd("idevice_id -l")


if __name__ == '__main__':
    # configuration().add_android()
    a = "http://123.127.238.246:4723/wd/hub"
    pattern = "47.+[0-9]"
    name = re.findall(pattern, a)
    print(name)
    for i in name:
        aa = int(i)
        print(aa)
        print(type(aa))
