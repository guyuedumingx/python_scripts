import requests
import json

"""
提供教务系统相关服务
需要一个管理者账号用来登录教务系统
"""
class Data:

    def __init__(self, admin_account, admin_password):
        self.account = admin_account
        self.password = admin_password
        self.url = "http://jwxt.gduf.edu.cn/app.do?"
        self.info = self.admin_login()
        self.token = self.info['token']
        self.headers = {
            "token" : self.token
        }

    # 管理员账号登录
    def admin_login(self):
        data = {
            "method" : "authUser",
            "xh"  : self.account,
            "pwd" : self.password
        }
        text = self.get_response(data)
        info = json.loads(text)
        print(info['msg'])
        return info

    def get_response(self, data, headers={}):
        response = requests.get(self.url,params=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text


    # 根据成员学号获取成员的课程信息
    def get_kc_data_by_xh(self, xh):
        data = {
            "method" : "getKbcxAzc",
            "xh"     : xh,
            "zc"     : 1
        }
        text = self.get_response(data, self.headers)
        return json.loads(text)
    
    # 根据学号获取成员的成绩信息
    def get_score_by_xh(self, xh):
        data = {
            "method" : "getCjcx",
            "xh"     : xh
        }
        text = self.get_response(data, self.headers)
        return json.loads(text)

    # 获取空教室信息 time的格式为: 2021-03-12 
    # idleTime 的格式为 allday am, pm, night, 0102(意为第一小节，第二小节)
    # info 
    def get_empty_classroom(self, time, idleTime, info={}):
        data = {
            "method" : "getKxJscx",
            "time" : time, 
            "idleTime" : idleTime
        }
        data.update(info)
        text = self.get_response(data, self.headers)
        return json.loads(text)
    
    # 获取成员考试信息
    def get_exam_data_by_xh(self, xh):
        data = {
            "method" : "getKscx",
            "xh" : xh
        }
        text = self.get_response(data, self.headers)
        return json.loads(text)



"""
成员类
"""
class Member:

    def __init__(self, xh):
        self.xh = xh
    
    def generate_info(self, data):
        self.name = data['']



xh = 191543430
pwd = "76750jww"
data = Data(xh, pwd)        

info = data.get_kc_data_by_xh(xh)
print(info)
