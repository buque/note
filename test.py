#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mywork import Work

if __name__ == '__main__':
    work = Work()
    work.GetDataFromExcel(r'D:\WorkSpace\note\工作记录表.xlsx')
    #work.ShowDataByJson()
    work.PutData2Excel(r'D:\WorkSpace\note\工作记录表1.xls')