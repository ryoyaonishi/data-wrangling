import xlrd
import agate

workbook = xlrd.open_workbook('data/chp9/unicef_oct_2014.xls')

workbook.nsheets

workbook.sheet_names()

sheet = workbook.sheets()[0]

sheet.nrows

sheet.row_values(0)

for r in range(sheet.nrows):
    print(r, sheet.row(r))
