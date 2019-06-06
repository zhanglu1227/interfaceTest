

import unittest
import time
import os
import sys
import HTMLTestRunner
from common.readConfig import ReadConfig
from common.configEmail import ConfigMyEmail
from testCase.test_case_ddt import TestCase



'''
第一步：加载所有的测试用例
第二步：执行所有的用例，并把结果写入HTML测试报告
第三步：获取最新的测试报告
第四步：发送最新的测试报告
'''



class myTest(unittest.TestCase):

    def add_case(dir = 'TestCase'):
        '''第一步：加载所有的测试用例'''
        # sys.path.append('./testcase')
        # case_path = './testcase'
        case_path = os.path.dirname() + '/' + dir  # 用例文件夹
        print(case_path)
        # 定义discover方法的参数
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern='test_case_ddt.py',
                                                       top_level_dir=None)
        return discover



if __name__ == '__main__':

    # 1 - ---------   定义个报告存放路径
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    filename = public_path + "\\Report\\" + current_time + "report.html"
    # report_path = os.getcwd() + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    print(filename)

    # 2 - ---------   定义一个文件名，以写方式打开
    fp = open(filename, "wb")

    # 3 - ---------   定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'用例执行情况：')

    # 4 - ---------   运行测试用例
    suit = unittest.TestSuite()
    # 把这个类中需要执行的测试用例加进去，有多条再加即可
    suit.addTest(myTest('add_case'))

    # 运行测试用例
    runner.run(suit)

    # 5 - ---------   关闭报告文件
    fp.close()
    c = ConfigMyEmail()
    c.send_mail()
