# 步骤
# 1、导入包
# 2、找到excel文件并打开
# 3、定位sheet页
# 4、定位行和列
# 5、读取excel数据
# 6、组装测试数据变为一条正确的匹配的接口测试数据
# 7、return data给testcase模块

# 导入包
import xlrd

class readExcel:

    # 找到并打开excel
    readbook = xlrd.open_workbook(r'/Users/cola/Desktop/testcode/interfaceTest/testData/data.xls')
    print(readbook)

    # 获取所有sheet页
    sheetlist = readbook.sheet_names()

    sheetData = []

    sheetUrl = []

    sheetParam = []

    sheetAssert = []

    # 读取excelsheet页中数据

    def getData(self):

        for n in self.sheetlist:
            print('sheet页名称：', n)

            # 读取sheet页数据

            sheet = self.readbook.sheet_by_name(n)

            sheet_nrows = sheet.nrows  # 行
            sheet_ncols = sheet.ncols  # 列

            # print('************',sheet.ncols,sheet_ncols)

            for i in range(1, sheet_nrows):
                row_values = sheet.row_values(i)
                if self.sheetlist.index(n) == 0:
                    self.sheetUrl.append(row_values)
                    print(row_values)

                elif self.sheetlist.index(n) == 1:
                    self.sheetParam.append(row_values)
                    print(row_values)

                elif self.sheetlist.index(n) == 2:
                    self.sheetAssert.append(row_values)
                    print(row_values)

            print('*****', self.sheetUrl,self.sheetParam,self.sheetAssert)

    # 组装数据，将三个列表按照id进行匹配
    def assembleData(self):
        data = self.sheetUrl[0] + self.sheetParam[0][1:]
        print(data)
        pass




read = readExcel()
read.getData()
read.assembleData()
