from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from mywork import Work


class WorkView(QTableWidget):
    mySignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # self.setWindowTitle("biaoge")
        # self.setWindowIcon(QIcon("2.png"))
        self.work = Work()
        columName = ['时间', '优先级', '内容', '状态']
        self.setColumnCount(len(columName))
        self.setHorizontalHeaderLabels(columName)
        self.setupView()
        self.cellChanged.connect(self.updateStatus)
        
    def setupSignal(self, func):
        '''信号用于通知主窗口文本发生了变化'''
        self.mySignal.connect(func)

    def updateStatus(self, info):
        #reply = QMessageBox.information(self, "消息框标题", "这是一条消息。", QMessageBox.Yes | QMessageBox.No)
        #发一个信号给主窗口
        if info is None or isinstance(info, int):
            info = r"修改未保存"
        self.mySignal.emit(info)

    def newLine(self):
        rowCnt = self.rowCount()
        self.insertRow(rowCnt)
        
        #时间
        mydate = self.work.getToday()
        self.setItem(rowCnt, 0, QTableWidgetItem(mydate))

        levelComb = self.createLevelCombox()
        self.setCellWidget(rowCnt, 1, levelComb)
        self.setItem(rowCnt, 2, QTableWidgetItem('123'))
        stateComb = self.createStateCombox()
        self.setCellWidget(rowCnt, 3, stateComb)
        self.updateStatus(r'新增未保存')

    def delLine(self):
        rowCnt = self.currentRow()
        self.removeRow(rowCnt)
        self.updateStatus(r'删除未保存')

    def save(self):
        '''将列表显示信息格式化为对象与原有数据做合并'''
        viewlist = self.getViewData()
        self.work.updateData(viewlist)
        self.updateStatus(r'已保存')

    def getViewData(self):
        '''将列表信息格式化为Work数据，再做替换'''
        mylist = []
        rowCnt = self.rowCount()
        mydate = self.work.getToday()
        for i in range(0, rowCnt):
            #首列不用获取，更新时间即可
            line = []
            line.append(mydate)
            levelComb = self.cellWidget(i, 1)
            line.append(levelComb.currentIndex())
            line.append(self.item(i,2).text())
            stateComb = self.cellWidget(i, 3)
            line.append(stateComb.currentIndex())
            mylist.append(line)
        return mylist

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