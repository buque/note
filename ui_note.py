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



class NoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(300)
        self.setFixedWidth(250)
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
        table = QTableWidget(5, 3)
        table.setWindowTitle("biaoge")
        table.setWindowIcon(QIcon("2.png"))
        
        columName = ['优先级', '内容', '状态']
        table.setHorizontalHeaderLabels(columName)
        self.setTableInitData(table)
        table.setAlternatingRowColors(True)#交替使用颜色
        table.setShowGrid(False)#表格线隐藏
        #table.verticalHeader().setFrameShadow()
        #table.setFrameShadow(table, QFrame.NoFrame)#边框隐藏

        return table
    
    def setTableInitData(self, table):
        for i in range(5):
            for j in range(3):
                table.setItem(i, j, QTableWidgetItem(str(i)+str(j)))
