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
    # excel_dir = os.getcwd() + '/' + dir
    print('excel_dir', excel_dir)
    # 第一步：读取原excel中的所有数据（复制对象）
    excel_path = excel_dir + '/' + 'data.xls'
    print(excel_path)
    rb = xlrd.open_workbook(excel_path)
    # 第二步：复制读取的原excel对象
    wb = copy(rb)
    # 第三步：通过get_sheet()获取复制对象的sheet页
    ws = wb.get_sheet(2)

    # def __str__(self):
    #     return '我在哪%s'%self.excel_dir

    def writeData(self, id, real, status):
        try:
            print('写入')
            # 根据id写入对应的实际结果和接口测试状态
            # 第四步：对sheet页进行写入(传入x和y坐标，和具体写入的value)
            self.ws.write(id, 2, real)
            self.ws.write(id, 3, status)

            # 第五步：保存excel（具体的excel路径+名称）
            self.wb.save(self.excel_dir + '/' + 'data.xls')
            return 'ok'

        except Exception as msg:
            print(msg)


if __name__ == '__main__':
    a = WriteExcel()
    print(a.writeData(0, 0, 'Success'))
