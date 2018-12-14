from PyQt5.QtWidgets import *
from mywork import Work


class WorkView(QTableWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("biaoge")
        # self.setWindowIcon(QIcon("2.png"))
        columName = ['时间', '优先级', '内容', '状态']
        self.setColumnCount(len(columName))
        self.setHorizontalHeaderLabels(columName)
        self.setView()

    def newLine(self):
        rowCnt = self.table.rowCount()
        self.table.insertRow(rowCnt)
    
    def delLine(self):
        rowCnt = self.table.currentRow()
        self.table.removeRow(rowCnt)

    def setView(self):
        '''Show Today && Yesterday's works.'''
        work = Work()
        work.GetDataFromExcel(r'D:\WorkSpace\note\工作记录表.xls')
        mydate = work.GetToday()#显示今日数据
        mylist = work.GetDataByDate(mydate)
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
            if data[0][0] == "一般":
                j = 0
            elif data[0][0] == "重要":
                j = 1
            elif data[0][0] == "紧急":
                j = 2
            else:
                j = 3
            levelComb.setCurrentIndex(j)
            self.setCellWidget(i, 1, levelComb)

            
            self.setItem(i, 2, QTableWidgetItem(data[0][1]))  #事物
            #self.table.setItem(i, 3, QTableWidgetItem(data[0][2]))  #状态
            stateComb = self.createStateCombox()
            if data[0][0] == "未开始":
                j = 0
            elif data[0][0] == "进行中":
                j = 1
            else: 
                j = 2
            stateComb.setCurrentIndex(j)
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