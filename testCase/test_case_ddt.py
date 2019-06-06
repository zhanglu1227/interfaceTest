'''
功能：
    1.获取excel返回数据
    2.请求requests方法
    3.断言
    4.写入excel
'''

import unittest,json
from ddt import ddt,data,unpack
from common.read_excel import ReadExcel
from common.configHttp import ConfigHttp
from common.write_excel import WriteExcel

# 实例化
# 第一步：读取excel数据
re = ReadExcel()
testdata = re.addData()
# print(testdata)

# 实例化，以备调用封装好的requests方法
ch = ConfigHttp()
# 实例化，以备调用写入excel的方法
we = WriteExcel()

@ddt
class TestCase(unittest.TestCase):

    @data(*testdata)  # *args可变参数，传列表或元祖
    @unpack  # 分发
    def test_normal(self, id, url, name, method, param, expect):
        result = ch.getRequest(url, method, param)
        # 将response解码成python对象：dict
        real = str(json.loads(result)['errorCode'])
        try:
            self.assertEqual(real, expect)

            we.writeData(id, real, 'Success')

        except AssertionError as msg:
            print(msg)
            we.writeData(id, real, 'Fail')

if __name__ == '__main__':
    unittest.main




