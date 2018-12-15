# -*- coding: utf-8 -*-
"""
数据存储层，屏蔽底层存储细节
"""

from datetime import datetime, date, timedelta
import xlrd
import xlwt

class WorkStore():
    def __init__(self, fileName):
        self.fileName = fileName

    def getData(self):
        '''Read excel to memory.'''
        workbook = xlrd.open_workbook(self.fileName)
        sheet = workbook.sheet_by_index(0)
        nrows = sheet.nrows
        mylist = []
        for i in range(1, nrows):
            date_value = xlrd.xldate_as_tuple(sheet.cell_value(i,0), workbook.datemode)
            date_tmp = date(*date_value[:3]).strftime('%m/%d')
            content = sheet.row_values(i)#列表
            content[0] = date_tmp
            mylist.append(content)
        return mylist

    def putData(self, data):
        '''Write data to excel.'''
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        line = ['日期','级别','事物','状态']
        sheet.write(0, 0, line[0])
        sheet.write(0, 1, line[1])
        sheet.write(0, 2, line[2])
        sheet.write(0, 3, line[3])
        i = 1
        datastyle = xlwt.XFStyle()
        datastyle.num_format_str = '%Y/%m/%d'
        for content in data:
            sheet.write(i, 0, '2018/'+content[0], datastyle)
            for j in range(1, 4):
                sheet.write(i, j, content[j])
            i = i + 1
        workbook.save(self.fileName)

