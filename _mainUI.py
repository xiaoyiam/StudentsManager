# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(710, 10, 61, 31))
        self.searchButton.setObjectName("searchButton")
        self.searchBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(640, 10, 61, 31))
        self.searchBox.setWhatsThis("")
        self.searchBox.setObjectName("searchBox")
        self.searchBox.addItem("")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(10, 10, 631, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.searchList = QtWidgets.QTreeWidget(self.centralwidget)
        self.searchList.setGeometry(QtCore.QRect(10, 50, 761, 481))
        self.searchList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.searchList.setObjectName("searchList")
        item_0 = QtWidgets.QTreeWidgetItem(self.searchList)
        item_0 = QtWidgets.QTreeWidgetItem(self.searchList)
        self.searchList.header().setVisible(True)
        self.searchList.header().setSortIndicatorShown(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(790, 50, 201, 301))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 72, 15))
        self.label_6.setObjectName("label_6")
        self.indexLabel = QtWidgets.QLabel(self.groupBox)
        self.indexLabel.setGeometry(QtCore.QRect(100, 50, 91, 16))
        self.indexLabel.setText("")
        self.indexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.indexLabel.setObjectName("indexLabel")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setGeometry(QtCore.QRect(100, 80, 91, 16))
        self.nameLabel.setText("")
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.birthLabel = QtWidgets.QLabel(self.groupBox)
        self.birthLabel.setGeometry(QtCore.QRect(100, 110, 91, 16))
        self.birthLabel.setText("")
        self.birthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.birthLabel.setObjectName("birthLabel")
        self.majorLabel = QtWidgets.QLabel(self.groupBox)
        self.majorLabel.setGeometry(QtCore.QRect(100, 140, 91, 16))
        self.majorLabel.setText("")
        self.majorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.majorLabel.setObjectName("majorLabel")
        self.gradeLabel = QtWidgets.QLabel(self.groupBox)
        self.gradeLabel.setGeometry(QtCore.QRect(100, 170, 91, 16))
        self.gradeLabel.setText("")
        self.gradeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gradeLabel.setObjectName("gradeLabel")
        self.classLabel = QtWidgets.QLabel(self.groupBox)
        self.classLabel.setGeometry(QtCore.QRect(100, 200, 91, 16))
        self.classLabel.setText("")
        self.classLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classLabel.setObjectName("classLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生学籍管理系统"))
        self.searchButton.setText(_translate("MainWindow", "搜索"))
        self.searchBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>匹配含有所有指定标签的资源</p><p>and: 匹配所有指定标签</p><p>or: 匹配任一指定标签</p></body></html>"))
        self.searchBox.setItemText(0, _translate("MainWindow", "学号"))
        self.searchList.setSortingEnabled(True)
        self.searchList.headerItem().setText(0, _translate("MainWindow", "学号"))
        self.searchList.headerItem().setText(1, _translate("MainWindow", "姓名"))
        self.searchList.headerItem().setText(2, _translate("MainWindow", "出生日期"))
        self.searchList.headerItem().setText(3, _translate("MainWindow", "院系"))
        self.searchList.headerItem().setText(4, _translate("MainWindow", "年级"))
        self.searchList.headerItem().setText(5, _translate("MainWindow", "班级"))
        __sortingEnabled = self.searchList.isSortingEnabled()
        self.searchList.setSortingEnabled(False)
        self.searchList.topLevelItem(0).setText(0, _translate("MainWindow", "201507321"))
        self.searchList.topLevelItem(0).setText(1, _translate("MainWindow", "zc"))
        self.searchList.topLevelItem(0).setText(2, _translate("MainWindow", "1997.03"))
        self.searchList.topLevelItem(0).setText(3, _translate("MainWindow", "555"))
        self.searchList.topLevelItem(0).setText(4, _translate("MainWindow", "2015"))
        self.searchList.topLevelItem(0).setText(5, _translate("MainWindow", "151"))
        self.searchList.topLevelItem(1).setText(0, _translate("MainWindow", "201507320"))
        self.searchList.topLevelItem(1).setText(1, _translate("MainWindow", "zzy"))
        self.searchList.topLevelItem(1).setText(2, _translate("MainWindow", "1997.08.16"))
        self.searchList.topLevelItem(1).setText(3, _translate("MainWindow", "555"))
        self.searchList.topLevelItem(1).setText(4, _translate("MainWindow", "2015"))
        self.searchList.topLevelItem(1).setText(5, _translate("MainWindow", "151"))
        self.searchList.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "学生信息"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.label_3.setText(_translate("MainWindow", "出生日期"))
        self.label_4.setText(_translate("MainWindow", "院系"))
        self.label_5.setText(_translate("MainWindow", "年级"))
        self.label_6.setText(_translate("MainWindow", "班级"))
        self.action.setText(_translate("MainWindow", "\\"))

