# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\WorkSpace\note\note.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mywork import Work



class NoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(500)
        self.setFixedWidth(350)
        self.setupNote()
        self.show()

    def setupNote(self):
        self.table = self.initTable()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.table)
        self.setLayout(hbox)
        self.setCentralWidget(self.table)

    def initTable(self):
        table = QTableWidget(5, 4)
        table.setWindowTitle("biaoge")
        table.setWindowIcon(QIcon("2.png"))
        columName = ['时间', '优先级', '内容', '状态']
        table.setHorizontalHeaderLabels(columName)
        self.setTableInitData(table)
        table.setAlternatingRowColors(True)#交替使用颜色
        table.setShowGrid(False)#表格线隐藏
        table.resizeColumnsToContents()
        table.resizeColumnToContents(1)
        # table.verticalHeader().setFrameShadow(table.verticalHeader(), QFrame.NoFrame)
        #table.setFrameShadow(table, QFrame.NoFrame)#边框隐藏

        return table

    def setTableInitData(self, table):
        '''Show Today && Yesterday's works.'''
        work = Work()
        work.GetDataFromExcel(r'D:\WorkSpace\note\工作记录表.xlsx')
        mydate = work.GetToday()#显示今日数据
        mylist = work.GetDataByDate(mydate)
        for i in range(len(mylist)):
            table.setItem(i, 0, QTableWidgetItem(mydate))
            table.setItem(i, 1, QTableWidgetItem(mylist[0][0]))
            table.setItem(i, 2, QTableWidgetItem(mylist[0][1]))
            table.setItem(i, 3, QTableWidgetItem(mylist[0][2]))
