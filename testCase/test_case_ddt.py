

import unittest,json
from ddt import ddt,data,unpack
from common.read_excel import ReadExcel
from common.configHttp import ConfigHttp
from common.write_excel import WriteExcel

# 实例化
re = ReadExcel()
testData = re.addData()
print(testData)

ch = ConfigHttp()
we = WriteExcel()

@ddt
class TestCase(unittest.TestCase):

    @data(*testData)
    @unpack
    def test_normal(self, id, url, name, method, param, expect):
        result = ch.getRequest(url, method, param)
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertEqual(real, expect)
            print('返回结果',status)

        except Exception as msg:
            print(msg)
            status = 'Error'

        finally:
            if status == None:
                we.writeData(id, real, 'Success')

            else:
                we.writeData(id, real, 'Fail')

if __name__ == '__main__':
    unittest.main

