#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mywork import Work

if __name__ == '__main__':
    work = Work()
    work.GetDataFromExcel(r'E:\WorkSpace\note\工作记录表.xls')
    work.ShowDataByJson()
    work.PutData2Excel(r'E:\WorkSpace\note\工作记录表1.xls')