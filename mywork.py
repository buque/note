# -*- coding: utf-8 -*-

import os
from datetime import datetime, date, timedelta
import xlrd, xlwt
import json


class Work(object):
    dic = {}

    def GetToday():
        t = datetime.now().strftime("%Y/%m/%d")
        return t

    def GetYesterday():
        yesterday = datetime.now() + timedelta(days = -1)
        t = yesterday.strftime("%Y/%m/%d")
        return t

    def GetDataByDate(self, mydate):
        return self.dic[mydate]

    def GetDataFromExcel(self, fileName):
        '''Read excel to memory.'''
        workbook = xlrd.open_workbook(fileName)
        sheet = workbook.sheet_by_index(0)
        nrows = sheet.nrows
        data = {}
        i = 1
        while i < nrows:
            date_value = xlrd.xldate_as_tuple(sheet.cell_value(i,0), workbook.datemode)
            date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
            content = sheet.row_values(i)#列表
            del content[0]
            mylist = data.get(date_tmp, None)
            if mylist == None:
                mylist = []
                data[date_tmp] = mylist
            mylist.append(content)
            i =i + 1
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