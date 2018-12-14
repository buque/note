# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\WorkSpace\note\note.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from trayicon import TrayIcon
from workview import WorkView

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

    def setupToolBar(self):
        exitAction = QAction(QIcon('D:\\WorkSpace\\note\\quit.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        newAction = QAction(QIcon('D:\\WorkSpace\\note\\new.png'), '新建', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.view.newLine)

        delAction = QAction(QIcon('D:\\WorkSpace\\note\\del.png'), '删除', self)
        delAction.setShortcut('Ctrl+N')
        delAction.triggered.connect(self.view.delLine)

        self.toolbar = self.addToolBar('菜单栏')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(delAction)

    def setupNote(self):
        self.view = WorkView()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.view)
        self.setLayout(hbox)
        self.setCentralWidget(self.view)

    

    



            
