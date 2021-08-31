# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 791, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 8, 181, 541))
        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(10, 40, 154, 21))
        self.openBtn = QPushButton(self.groupBox)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setGeometry(QRect(40, 190, 91, 41))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 81, 21))
        self.limitNum = QSpinBox(self.groupBox)
        self.limitNum.setObjectName(u"limitNum")
        self.limitNum.setGeometry(QRect(120, 90, 42, 22))
        self.scanBtn = QPushButton(self.groupBox)
        self.scanBtn.setObjectName(u"scanBtn")
        self.scanBtn.setGeometry(QRect(40, 140, 91, 41))
        self.listTab = QTabWidget(self.frame)
        self.listTab.setObjectName(u"listTab")
        self.listTab.setGeometry(QRect(190, 10, 601, 541))
        self.detailTab = QWidget()
        self.detailTab.setObjectName(u"detailTab")
        self.detailTable = QTableView(self.detailTab)
        self.detailTable.setObjectName(u"detailTable")
        self.detailTable.setGeometry(QRect(0, 0, 641, 521))
        self.listTab.addTab(self.detailTab, "")
        self.blackTab = QWidget()
        self.blackTab.setObjectName(u"blackTab")
        self.blackTable = QTableView(self.blackTab)
        self.blackTable.setObjectName(u"blackTable")
        self.blackTable.setEnabled(True)
        self.blackTable.setGeometry(QRect(0, 0, 601, 521))
        self.blackTable.setTabletTracking(False)
        self.listTab.addTab(self.blackTab, "")

        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.listTab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6253\u5f00\u52a8\u6001", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u52a8\u6001", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9650\u5236\u7f51\u9875\u6570", None))
        self.scanBtn.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf", None))
#if QT_CONFIG(accessibility)
        self.detailTab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.listTab.setTabText(self.listTab.indexOf(self.detailTab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.listTab.setTabText(self.listTab.indexOf(self.blackTab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

