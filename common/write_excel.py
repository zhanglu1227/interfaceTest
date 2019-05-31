'''
功能：
1、找到excel，读取数据
2、复制excel对象
'''

import xlrd
import os

# 操作 Excel 文件的实用工具，如复制、分割、筛选等
from xlutils.copy import copy

class WriteExcel(object):

    dir = 'testData'
    excel_dir = os.path.dirname(os.getcwd()) + '/' + dir
    excel_dir = os.getcwd() + '/' + dir
    print('excel_dir',excel_dir)
    rb = xlrd.open_workbook(excel_dir + '/' + 'data.xls')
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(2)

    def writeData(self,id,real,status):
        try:
            print('写入')
            # 根据id写入对应的实际结果和接口测试状态
            self.ws.write(id, 2, real)
            self.ws.write(id, 3, status)
            self.wb.save(self.excel_dir + '/' + 'data.xls')
            return 'ok'

        except Exception as msg:
            print(msg)

# print(os.getcwd())
# print(os.path.abspath(sys.argv[0]))
# print(os.path.dirname(os.path.realpath(__file__)))

