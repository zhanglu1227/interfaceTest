
# 步骤
# 1、调用read_excel模块拿到测试数据
# 2、根据接口的请求方式判断调用XX方法
# 3、校验
# 4、保存执行结果
# 5、写入excel

import requests
import json

# from common import read_excel
from common.read_excel import readExcel

# test = read_excel.readExcel
# print(test)

'''
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,params=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=params, headers=header)
        else:
            res = requests.get(url=url, params=params)
        return res.json()

    def run_main(self,method,url,data=None,header=None,params=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,params,header)
        return res

'''

class Testcase:

    def __init__(self):
        self.readExcel = readExcel

    # 获取excel行数（case个数）
    def get_case_lines(self):
        return self.readExcel.get_lines()

    # 获取url
    def get_url(self, row):
        col = readExcel.get_url()
        url = self.readExcel.get_value(row, col)
        return url

    # 获取请求方式
    def get_request_method(self, row):
        col = readExcel.get_request_method()
        request_method = self.readExcel.get_value(row, col)
        return request_method

    # 获取请求参数
    def get_data(self, row):
        col = readExcel.get_data()
        data1 = self.readExcel.get_value(row, col)
        return data1

    # 获取请求结果
    def get_expected(self, row):
        col = readExcel.get_expected()
        result = self.readExcel.get_value(row, col)
        return result

if __name__ == '__main__':
    test = Testcase()
    print(test.get_expected())

