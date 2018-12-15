# -*- coding: utf-8 -*-
"""
模型层数据存储格式
{'2018/12/15', [['1', '完成代码测试', '1'],['1', '完成功能开发', '1']]}
"""

from datetime import datetime, date, timedelta
import json
import copy
from store import WorkStore

class Work(object):
    '''模型层'''

    def __init__(self):
        self.store = WorkStore(r'D:\WorkSpace\note\工作记录表.xls')
        self.dic = None

    def getToday(self):
        mydate = datetime.now().strftime("%m/%d")
        return mydate

    def getYesterday(self):
        yesterday = datetime.now() + timedelta(days = -1)
        mydate = yesterday.strftime("%m/%d")
        return mydate

    def showData(self):
        jsonStr = json.dumps(self.dic, ensure_ascii=False)
        print(jsonStr)

    def getDataByDate(self, mydate):
        data = self.getData()
        mylist = data.get(mydate, None)
        return mylist
    
    def getData(self):
        '''init Work data by WorkStore data.'''
        if self.dic is not None:
            return self.dic
        
        listdata = self.store.getData()
        data = {}
        for content in listdata:
            mydate = content[0]
            mylist = data.get(mydate, None)
            if mylist == None:
                mylist = []
                data[mydate] = mylist
            line = copy.deepcopy(content[1:])
            if line[0] == "一般":
                line[0] = 0
            elif line[0] == "重要":
                line[0] = 1
            elif line == "紧急":
                line[0] = 2
            else:
                line[0] = 3

            if line[2] == "未开始":
                line[2] = 0
            elif line[2] == "进行中":
                line[2] = 1
            else: 
                line[2] = 2

            mylist.append(line)
        self.dic = data
        return data

    def putData(self):
        '''init WorkStore data by Work data.'''  
        data = []
        for key in self.dic.keys():
            mylist = self.dic[key]
            for content in mylist:
                line = copy.deepcopy(content)
                if line[1] == 0:
                    line[1] = '一般'
                elif line[1] == 1:
                    line[1] = '重要'
                elif line[1] == 2:
                    line[1] = '紧急'
                else:
                    line[1] = '关键'

                if line[3] == 0:
                    line[3] = '未开始'
                elif line[3] == 1:
                    line[3] = '进行中'
                else: 
                    line[3] = '已完成'
                data.append(line)
        self.store.putData(data)
    
    def updateData(self, mylist):
        mydate = self.getToday()
        self.dic[mydate] = mylist
        self.putData()

