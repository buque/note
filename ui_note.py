# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\WorkSpace\note\note.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(233, 352)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setEnabled(True)
        self.listView.setGeometry(QtCore.QRect(0, 0, 231, 351))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "便签"))

