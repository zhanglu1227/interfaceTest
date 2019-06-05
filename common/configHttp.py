
# 引用requests库
import requests

# 创建ReadHttp类
class ConfigHttp:

    # 创建get方法
    def get(self, url, param, cookie=None, header=None, timeout=3):
        # try不仅捕获异常，而且会恢复执行
        try:
            # headers,cookies,timeout是可选参数
            response = requests.get(url=url, params=eval(param), headers=header, coookies=cookie, timeout=timeout)
            result = response.text
            return result
        # Exception常规错误
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建post方法
    def post(self, url, param, cookie=None, header=None, timeout=3):
        try:
            # 如果post请求里有get参数，加上params='XXX'
            response = requests.post(url=url, data=eval(param), params=None, headers=header, coookies=cookie, timeout=timeout)
            result = response.text
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建一个getrequest方法根据传入参数判断调用哪个方法
    def getRequest(self, url, method, param):
        if str(method) == 'get':
            return self.get(url, param)
        elif str(method) == 'post':
            return self.post(url, param)
