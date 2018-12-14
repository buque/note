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
from trayicon import TrayIcon

class NoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(500)
        self.setFixedWidth(350)
        self.setupNote()
        self.setupToolBar()
        ti = TrayIcon(self)
        ti.show()
        self.show()

    def newLine(self):
        rowCnt = self.table.rowCount()
        self.table.insertRow(rowCnt)
    
    def delLine(self):
        rowCnt = self.table.currentRow()
        self.table.removeRow(rowCnt)

    def setupToolBar(self):
        exitAction = QAction(QIcon('D:\\WorkSpace\\note\\quit.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        newAction = QAction(QIcon('D:\\WorkSpace\\note\\new.png'), '新建', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newLine)

        delAction = QAction(QIcon('D:\\WorkSpace\\note\\del.png'), '删除', self)
        delAction.setShortcut('Ctrl+N')
        delAction.triggered.connect(self.delLine)

        self.toolbar = self.addToolBar('菜单栏')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(delAction)


        # self.setGeometry(300, 300, 450, 450)
        # self.setWindowTitle('QMainWindow的ToolBar')
        # self.show()
        pass

    def setupNote(self):
        self.table = self.initTable()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.table)
        self.setLayout(hbox)
        self.setCentralWidget(self.table)

    def initTable(self):
        table = QTableWidget(0, 0)
        table.setWindowTitle("biaoge")
        table.setWindowIcon(QIcon("2.png"))
        columName = ['时间', '优先级', '内容', '状态']
        table.setColumnCount(len(columName))
        table.setHorizontalHeaderLabels(columName)
        self.table = table
        self.setTableInitData()
        
        # table.verticalHeader().setFrameShadow(table.verticalHeader(), QFrame.NoFrame)
        #table.setFrameShadow(table, QFrame.NoFrame)#边框隐藏
        return table

    def createLevelCombox(self):
        levelComb = QComboBox()
        levelComb.addItem("一般")
        levelComb.addItem("重要")
        levelComb.addItem("紧急")
        levelComb.addItem("关键")
        levelComb.setCurrentIndex(0)
        return levelComb

    def createStateCombox(self):
        StateComb = QComboBox()
        StateComb.addItem("未开始")
        StateComb.addItem("进行中")
        StateComb.addItem("已完成")
        StateComb.setCurrentIndex(0)
        return StateComb

    def fillTable(self, mydate, data):
        if data is None or self.table is None:
            return
        
        for i in range(len(data)):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(mydate))  #日期
            #self.table.setItem(i, 1, QTableWidgetItem(data[0][0]))  #优先级
            levelComb = self.createLevelCombox()
            if data[0][0] == "一般":
                j = 0
            elif data[0][0] == "重要":
                j = 1
            elif data[0][0] == "紧急":
                j = 2
            else:
                j = 3
            levelComb.setCurrentIndex(j)
            self.table.setCellWidget(i, 1, levelComb)

            
            self.table.setItem(i, 2, QTableWidgetItem(data[0][1]))  #事物
            #self.table.setItem(i, 3, QTableWidgetItem(data[0][2]))  #状态
            stateComb = self.createStateCombox()
            if data[0][0] == "未开始":
                j = 0
            elif data[0][0] == "进行中":
                j = 1
            else: 
                j = 2
            stateComb.setCurrentIndex(j)
            self.table.setCellWidget(i, 3, stateComb)


    def setTableInitData(self):
        '''Show Today && Yesterday's works.'''
        work = Work()
        work.GetDataFromExcel(r'D:\WorkSpace\note\工作记录表.xls')
        mydate = work.GetToday()#显示今日数据
        mylist = work.GetDataByDate(mydate)
        self.fillTable(mydate, mylist)

        self.table.setAlternatingRowColors(True)#交替使用颜色
        self.table.setShowGrid(True)#表格线隐藏
        self.table.resizeColumnsToContents()
        self.table.resizeColumnToContents(1)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
            
