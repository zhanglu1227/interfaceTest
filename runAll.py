

import unittest
import time
import os
import sys
import HTMLTestRunner
from common.sendMail import SendMail


'''
第一步：加载所有的测试用例
第二步：执行所有的用例，并把结果写入HTML测试报告
第三步：获取最新的测试报告
第四步：发送最新的测试报告
'''

def run_case():
    # 1.定义报告存放路径
    filedir = 'result' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.html'
    reportpath = 'report/' + filedir

    # 2.定义一个文件名，以写方式打
    fp = open(reportpath, 'wb')

    # 3.定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试报告',
        description=u'用例执行情况：')

    # 4.运行测试用例
    casedir = sys.path[0] + '/testCase'
    discover = unittest.defaultTestLoader.discover(start_dir=casedir, pattern="test_case_ddt.py", top_level_dir=None)
    runner.run(discover)

    # 5.关闭报告文件
    fp.close()
    # SendMail().send_email()

if __name__ == '__main__':
    c = SendMail()
    c.send_email()
    run_case()


