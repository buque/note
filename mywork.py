# -*- coding: utf-8 -*-
"""
模型层
"""
from datetime import datetime, date, timedelta
import json
import xlrd
import xlwt


class Work(object):
    """数据层"""
    dic = {}

    def GetToday(self):
        t = datetime.now().strftime("%m/%d")
        return t

    def GetYesterday(self):
        yesterday = datetime.now() + timedelta(days = -1)
        t = yesterday.strftime("%m/%d")
        return t

    def GetDataByDate(self, mydate):
        return self.dic[mydate]

    def GetDataFromExcel(self, fileName):
        '''Read excel to memory.'''
        workbook = xlrd.open_workbook(fileName)
        sheet = workbook.sheet_by_index(0)
        nrows = sheet.nrows
        data = {}
        for i in range(1, nrows):
            date_value = xlrd.xldate_as_tuple(sheet.cell_value(i,0), workbook.datemode)
            date_tmp = date(*date_value[:3]).strftime('%m/%d')
            content = sheet.row_values(i)#列表
            del content[0]
            mylist = data.get(date_tmp, None)
            if mylist == None:
                mylist = []
                data[date_tmp] = mylist
            mylist.append(content)
        self.dic = data

    def ShowDataByJson(self):
        returnJson = json.dumps(self.dic, ensure_ascii=False)
        print(returnJson)

    def PutData2Excel(self, fileName):
        '''Write excel to excel.'''
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        i = 0
        for key in self.dic.keys():
            mylist = self.dic[key]
            for content in mylist:
                sheet.write(i, 0, key)
                sheet.write(i, 1, content[0])
                sheet.write(i, 2, content[1])
                sheet.write(i, 3, content[2])
                i = i + 1
        workbook.save(fileName)