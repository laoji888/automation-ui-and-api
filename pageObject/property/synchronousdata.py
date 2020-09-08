# -*- coding: utf-8 -*-
# @Date      : 2020-05-18
# @Author  : 高广东
# 物业系统同步数据

import requests


#物业系统同步数据
class Synchronous_Data():



        def synchronousdata(self):
                try:
                        sessionRequest = requests.session()  # 实例化会话对象
                        # 物业验收环境登录接口
                        loginUrl = "http://120.52.96.35:48080/default/main/login/cn.chinatowercom.pcms.main.login.login.flow"

                        # 请求参数
                        data = {"original_url": "/main/login/login.jsp",
                                "userId": "zhaosy",
                                "password": "000000"}

                        headers = {"Content-Type": "application/x-www-form-urlencoded"}

                        # 同步数据接口地址
                        synchronousUrl = 'http://120.52.96.35:48080/default/cn.chinatowercom.pcms.intf.itfmsgmgr.bl.dispatcher.dispatcher.run.biz.ext'

                        # 登录
                        te = sessionRequest.post(url=loginUrl, data=data, headers=headers)
                        # print(te.text)
                        # 请求同步数据接口
                        response = sessionRequest.get(url=synchronousUrl)

                        # 返回响应码,响应文本
                        #print("同步数据成功,响应内容是:{}".format(response.text))
                        return response.text

                except Exception as e:
                        print("同步数据失败，{}".format(e))







s = Synchronous_Data()
s.synchronousdata()
