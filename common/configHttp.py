

import requests

class ConfigHttp(object):

    # 定义get方法
    def get(self,url,param):
        try:
            print(url,param)
            response = requests.get(url,params=eval(param))
            result = response.text
            # 获取实际结果，进行断言
            return result
        except Exception:
            print('请求错误')
            return None
    # 定义post方法
    def post(self,url,param):
        try:
            print(url,param)
            response = requests.post(url,params=eval(param))
            result = response.text
            return result
        except Exception:
            print('请求错误')
            return None

    def getRequest(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)

        elif str(method) == 'post':
            return self.post(url,param)