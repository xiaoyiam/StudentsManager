# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentBox(object):
    def setupUi(self, StudentBox):
        StudentBox.setObjectName("StudentBox")
        StudentBox.resize(243, 293)
        self.label_2 = QtWidgets.QLabel(StudentBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(StudentBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(StudentBox)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 61, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(StudentBox)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 61, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(StudentBox)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(StudentBox)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 61, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.okButton = QtWidgets.QPushButton(StudentBox)
        self.okButton.setGeometry(QtCore.QRect(90, 250, 71, 28))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(StudentBox)
        self.cancelButton.setGeometry(QtCore.QRect(162, 250, 71, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.indexEdit = QtWidgets.QLineEdit(StudentBox)
        self.indexEdit.setGeometry(QtCore.QRect(80, 40, 151, 21))
        self.indexEdit.setDragEnabled(False)
        self.indexEdit.setClearButtonEnabled(True)
        self.indexEdit.setObjectName("indexEdit")
        self.nameEdit = QtWidgets.QLineEdit(StudentBox)
        self.nameEdit.setGeometry(QtCore.QRect(80, 70, 151, 21))
        self.nameEdit.setClearButtonEnabled(True)
        self.nameEdit.setObjectName("nameEdit")
        self.majorEdit = QtWidgets.QLineEdit(StudentBox)
        self.majorEdit.setGeometry(QtCore.QRect(80, 160, 151, 21))
        self.majorEdit.setClearButtonEnabled(True)
        self.majorEdit.setObjectName("majorEdit")
        self.gradeEdit = QtWidgets.QLineEdit(StudentBox)
        self.gradeEdit.setGeometry(QtCore.QRect(80, 190, 151, 21))
        self.gradeEdit.setClearButtonEnabled(True)
        self.gradeEdit.setObjectName("gradeEdit")
        self.classEdit = QtWidgets.QLineEdit(StudentBox)
        self.classEdit.setGeometry(QtCore.QRect(80, 220, 151, 21))
        self.classEdit.setClearButtonEnabled(True)
        self.classEdit.setObjectName("classEdit")
        self.birthEdit = QtWidgets.QLineEdit(StudentBox)
        self.birthEdit.setGeometry(QtCore.QRect(80, 130, 151, 21))
        self.birthEdit.setClearButtonEnabled(True)
        self.birthEdit.setObjectName("birthEdit")
        self.msg = QtWidgets.QLabel(StudentBox)
        self.msg.setGeometry(QtCore.QRect(11, 10, 221, 20))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.label_7 = QtWidgets.QLabel(StudentBox)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.maleButton = QtWidgets.QRadioButton(StudentBox)
        self.maleButton.setGeometry(QtCore.QRect(90, 100, 51, 19))
        self.maleButton.setObjectName("maleButton")
        self.famaleButton = QtWidgets.QRadioButton(StudentBox)
        self.famaleButton.setGeometry(QtCore.QRect(150, 100, 51, 19))
        self.famaleButton.setObjectName("famaleButton")

        self.retranslateUi(StudentBox)
        QtCore.QMetaObject.connectSlotsByName(StudentBox)
        StudentBox.setTabOrder(self.indexEdit, self.nameEdit)
        StudentBox.setTabOrder(self.nameEdit, self.maleButton)
        StudentBox.setTabOrder(self.maleButton, self.famaleButton)
        StudentBox.setTabOrder(self.famaleButton, self.birthEdit)
        StudentBox.setTabOrder(self.birthEdit, self.majorEdit)
        StudentBox.setTabOrder(self.majorEdit, self.gradeEdit)
        StudentBox.setTabOrder(self.gradeEdit, self.classEdit)
        StudentBox.setTabOrder(self.classEdit, self.okButton)
        StudentBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, StudentBox):
        _translate = QtCore.QCoreApplication.translate
        StudentBox.setWindowTitle(_translate("StudentBox", "学生信息盒"))
        self.label_2.setText(_translate("StudentBox", "姓名"))
        self.label.setText(_translate("StudentBox", "学号"))
        self.label_5.setText(_translate("StudentBox", "年级"))
        self.label_4.setText(_translate("StudentBox", "专业"))
        self.label_3.setText(_translate("StudentBox", "出生日期"))
        self.label_6.setText(_translate("StudentBox", "班级"))
        self.okButton.setText(_translate("StudentBox", "确定"))
        self.cancelButton.setText(_translate("StudentBox", "取消"))
        self.msg.setText(_translate("StudentBox", "提示信息"))
        self.label_7.setText(_translate("StudentBox", "性别"))
        self.maleButton.setText(_translate("StudentBox", "男"))
        self.famaleButton.setText(_translate("StudentBox", "女"))

