
import unittest
from common.read_excel import readExcel
from common.configHttp import ConfigHttp
from ddt import ddt,data,unpack
import json

d = readExcel()
testda = d.assembleData()
re = ConfigHttp


@ddt
class MyTestCase1(unittest.TestCase):

    @data(*testda)
    @unpack
    def test_normal(self,id,url,method,param,expect):
        result = re.getRequest(url,method,param)
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertAlmostEqual(real,expect)
            print('返回结果',status)
        except ArithmeticError as msg:
            print(msg)
            status = 'Error'

        finally:
            if status == None:
                pass
