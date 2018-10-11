# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\WorkSpace\note\note.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mywork import Work



class NoteWindow(QTableWidget):
    def __init__(self):
        super().__init__()
        self.UpdateTableView()
        self.show()
        self.CreateSystemIcon()
        self.tray.show()


    def CreateSystemIcon(self):
        self.tray = QSystemTrayIcon()
        self.icon = QIcon("21.png")
        self.tray.setIcon(self.icon)
        self.tray.activated.connect(self.TuoPanEvent)
        self.QuitAction = QAction("退出", self, triggered=self.quit)
        self.RestoreAction = QAction(u'还原 ', self, triggered=self.show) #添加菜单动作选项(还原主窗口)
        self.tray_menu = QMenu(QApplication.desktop()) #创建菜单
        self.tray_menu.addAction(self.RestoreAction) #为菜单添加动作        
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu) #设置系统托盘菜单

    def TuoPanEvent(self):
        self.tray.show()
    
    # def QuitAction(self, QAction):
    #     pass

    # def RestoreAction(self, QAction):
    #     pass

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.parent().exit()
        # qApp.quit()
        # sys.exit()

    def SetTableProperty(self):
        self.setWindowTitle("Note")
        # self.setWindowIcon(QIcon("2.png"))
        columName = ['日期', '等级', '工作内容', '工作量', '状态']
        self.setHorizontalHeaderLabels(columName)
        self.setAlternatingRowColors(True)#交替使用颜色
        self.setShowGrid(False)#表格线隐藏
        self.setFrameShape(QFrame.Box)
        self.verticalHeader().setVisible(False)#隐藏垂直表头
        self.horizontalHeader().setVisible(False)#隐藏水平表头
        self.setSelectionBehavior(QAbstractItemView.SelectRows)#设置整行选择
        self.resizeColumnsToContents()#将列调整到跟内容大小相匹配
        self.resizeRowsToContents()#将行大小调整到跟内容的大小相匹配
        self.setAcceptDrops(True)#设置允许拖放
        self.setDragEnabled(True)#设置允许拖放
        self.setFixedHeight(500)
        self.setFixedWidth(400)



        
    def getDataSource(self, mydate):
        work = Work()
        work.GetDataFromExcel(r'D:\WorkSpace\note\工作记录表.xlsx')
        mylist = work.GetDataByDate(mydate)
        return mylist

    def UpdateTableView(self):
        mydate = Work.GetToday()#显示今日数据
        mylist = self.getDataSource(mydate)
        if mylist:
            self.setColumnCount(5)
            self.setRowCount(len(mylist))
            self.DrawTableView(mydate, mylist)
            self.SetTableProperty()

    def DrawTableView(self, mydate, mylist):
        '''Show Today && Yesterday's works.'''      
        for i in range(len(mylist)):
            self.setItem(i, 0, QTableWidgetItem(mydate))
            self.setItem(i, 1, QTableWidgetItem(mylist[i][0]))
            self.setItem(i, 2, QTableWidgetItem(mylist[i][1]))
            self.setItem(i, 3, QTableWidgetItem(mylist[i][2]))
            self.setItem(i, 4, QTableWidgetItem(mylist[i][3]))
