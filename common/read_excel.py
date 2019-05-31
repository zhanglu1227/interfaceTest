# 步骤
# 1、导入包
# 2、找到excel文件并打开
# 3、定位sheet页
# 4、定位行和列
# 5、读取excel数据
# 6、组装测试数据变为一条正确的匹配的接口测试数据
# 7、return data给testcase模块

# 创建公共readExcl类，封装读取testdata包数据的方法
import xlrd

class ReadExcel:
    # 将打开excel方法实例化为readsheet
    readsheet = xlrd.open_workbook(r'/Users/cola/Desktop/testcode/interfaceTest/testData/data.xls')
    # 通过实例化的readsheet变量获取所有sheet页名称
    sheets = readsheet.sheet_names()
    # print(sheets) # 调试语句
    # 创建存放每个sheet页数据的列表
    urlSheet = []
    paramSheet = []
    assertSheet = []

    # 创建读取excel数据的方法
    def getData(self):
        for i in self.sheets:
            # 通过name获取sheet页
            sheet = self.readsheet.sheet_by_name(i)

            # 获取sheet页最大行数
            nrows = sheet.nrows
            for j in range(nrows):
                # 获取行数据
                sheet_row = sheet.row_values(j)
                # 如果i是urlSheet页
                if i == 'urlSheet':
                    # 添加行数据
                    self.urlSheet.append(sheet_row)
                elif i == 'paramSheet':
                    self.paramSheet.append(sheet_row)
                elif i == 'assertSheet':
                    self.assertSheet.append(sheet_row)

    # 创建一个组装数据的方法
    # 组装数据，将三个列表按照id进行匹配
    # 组装所有的接口请求参数为一个list，一个元素包含：id,url,methode,param,expect
    def addData(self):
        # 定义一个空列表用来装获取的数据
        datalist = []
        for i in range(1,len(self.urlSheet)):
            data = self.urlSheet[i] + self.paramSheet[i][1:] + list(self.assertSheet[i][1])
            datalist.append(data)
        return datalist

# 防止下面代码运行
if __name__ == '__main__':

    read = ReadExcel()
    read.getData()
    read.addData()

    # 调试
    # print(read.addData())