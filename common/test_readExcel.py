
'''
import xlrd

# 打开excel文件并获取所有sheet
workbook = xlrd.open_workbook(r'/Users/cola/Desktop/testcode/interfaceTest/testData/data.xls')

print(workbook.sheet_names())

# 根据下标获取sheet名称
sheet3_name = workbook.sheet_names()[2]
print(sheet3_name)

# 根据sheet索引或者名称获取sheet内容，同时获取sheet名称、行数、列数
sheet3 = workbook.sheet_by_index(2)
print(sheet3.name, sheet3.nrows, sheet3.ncols)
sheet2 = workbook.sheet_by_name('paramSheet')
print(sheet2.name, sheet2.nrows, sheet2.ncols)

# 根据sheet名称获取整行或整列的值
sheet1 = workbook.sheet_by_name('urlSheet')
rows = sheet1.row_values(3)
cols = sheet1.col_values(2)
print(rows)
print(cols)

# 获取指定单元格内容(三种)
print(sheet1.cell(1, 3).value)
print(sheet1.cell_value(1, 3))
print(sheet1.row(1)[3].value)
'''

# 导入xlrd模块
import xlrd

# 打开文件
workbook = xlrd.open_workbook(r'/Users/cola/Desktop/testcode/interfaceTest/testData/data.xls')

def Dataexcel():

    sheets = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheets)

    nrows = sheet.nrows
    for i in range(nrows):
        print(sheet.row_values(i))




