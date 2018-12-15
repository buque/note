from PyQt5.QtWidgets import *
from mywork import Work


class WorkView(QTableWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("biaoge")
        # self.setWindowIcon(QIcon("2.png"))
        self.work = Work()
        columName = ['时间', '优先级', '内容', '状态']
        self.setColumnCount(len(columName))
        self.setHorizontalHeaderLabels(columName)
        self.setupView()

    def newLine(self):
        rowCnt = self.rowCount()
        self.insertRow(rowCnt)
        
        #时间
        mydate = self.work.getToday()
        self.setItem(rowCnt, 0, QTableWidgetItem(mydate))

        levelComb = self.createLevelCombox()
        self.setCellWidget(rowCnt, 1, levelComb)
        stateComb = self.createStateCombox()
        self.setCellWidget(rowCnt, 3, stateComb)

    
    def delLine(self):
        rowCnt = self.currentRow()
        self.removeRow(rowCnt)

    def setupView(self):
        '''Show Today && Yesterday's works.'''
        mydate = self.work.getToday()
        mylist = self.work.getDataByDate(mydate)
        self.fillTable(mydate, mylist)

        self.setAlternatingRowColors(True)#交替使用颜色
        self.setShowGrid(True)#表格线隐藏
        self.resizeColumnsToContents()
        self.resizeColumnToContents(1)
        self.setSelectionBehavior(QTableWidget.SelectRows)

    def fillTable(self, mydate, data):
        if data is None:
            return
        
        for i in range(len(data)):
            self.insertRow(i)
            self.setItem(i, 0, QTableWidgetItem(mydate))  #日期
            #self.table.setItem(i, 1, QTableWidgetItem(data[0][0]))  #优先级
            levelComb = self.createLevelCombox()
            levelComb.setCurrentIndex(data[0][0])
            self.setCellWidget(i, 1, levelComb)

            
            self.setItem(i, 2, QTableWidgetItem(data[0][1]))  #事物
            #self.table.setItem(i, 3, QTableWidgetItem(data[0][2]))  #状态
            stateComb = self.createStateCombox()
            stateComb.setCurrentIndex(data[0][2])
            self.setCellWidget(i, 3, stateComb)

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