
# 引用requests库
import requests

# 创建ReadHttp类
class ConfigHttp:

    # 创建get方法
    def get(self, url, param):
        # try不仅捕获异常，而且会恢复执行
        try:
            response = requests.get(url=url, params=param)
            result = response.text
            return result
        # Exception常规错误
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建post方法
    def post(self, url, param):
        try:
            response = requests.post(url=url, data=param)
            result = response.text
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建一个getrequest方法根据传入参数判断调用哪个方法
    def getRequest(self, url, method, param):
        if method == 'get':
            return self.get(url, param)
        elif method == 'post':
            return self.post(url, param)
