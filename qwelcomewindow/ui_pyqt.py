# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sat Dec 29 17:36:19 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 550)
        MainWindow.setStyleSheet(_fromUtf8("QWidget\n"
"{\n"
"    background-color: rgb(60, 63, 65);\n"
"    color: rgb(197, 197, 197);\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QListWidget\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QListView::item\n"
"{\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"     border: 1px solid #555555;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QListView::item:selected:!active {\n"
"     background: #343434;\n"
" }\n"
"\n"
" QListView::item:selected:active {\n"
"     background: #343434;\n"
" }\n"
"\n"
" QListView::item:hover {\n"
"     background: #343434;\n"
" }\n"
"\n"
"QLabel\n"
"{\n"
"    padding: 8px;\n"
"    border: none;\n"
"    background-color: #4b4b4b\n"
"};\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayoutHeader = QtGui.QHBoxLayout()
        self.horizontalLayoutHeader.setSpacing(0)
        self.horizontalLayoutHeader.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutHeader.setObjectName(_fromUtf8("horizontalLayoutHeader"))
        self.labelIcon = QtGui.QLabel(self.centralwidget)
        self.labelIcon.setText(_fromUtf8(""))
        self.labelIcon.setObjectName(_fromUtf8("labelIcon"))
        self.horizontalLayoutHeader.addWidget(self.labelIcon)
        self.labelTitle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setStyleSheet(_fromUtf8("font: 20pt \"Verdana\";"))
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.horizontalLayoutHeader.addWidget(self.labelTitle)
        self.verticalLayout.addLayout(self.horizontalLayoutHeader)
        self.horizontalLayoutMain = QtGui.QHBoxLayout()
        self.horizontalLayoutMain.setSpacing(0)
        self.horizontalLayoutMain.setMargin(9)
        self.horizontalLayoutMain.setObjectName(_fromUtf8("horizontalLayoutMain"))
        self.frameRecents = QtGui.QFrame(self.centralwidget)
        self.frameRecents.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameRecents.setFrameShadow(QtGui.QFrame.Raised)
        self.frameRecents.setObjectName(_fromUtf8("frameRecents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frameRecents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelRecents = QtGui.QLabel(self.frameRecents)
        self.labelRecents.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRecents.setObjectName(_fromUtf8("labelRecents"))
        self.verticalLayout_2.addWidget(self.labelRecents)
        self.listWidgetRecents = QtGui.QListWidget(self.frameRecents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetRecents.sizePolicy().hasHeightForWidth())
        self.listWidgetRecents.setSizePolicy(sizePolicy)
        self.listWidgetRecents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidgetRecents.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.listWidgetRecents.setObjectName(_fromUtf8("listWidgetRecents"))
        self.verticalLayout_2.addWidget(self.listWidgetRecents)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayoutMain.addWidget(self.frameRecents)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutMain.addItem(spacerItem)
        self.framequickStart = QtGui.QFrame(self.centralwidget)
        self.framequickStart.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framequickStart.setFrameShadow(QtGui.QFrame.Raised)
        self.framequickStart.setObjectName(_fromUtf8("framequickStart"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.framequickStart)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayoutQuickStart = QtGui.QVBoxLayout()
        self.verticalLayoutQuickStart.setSpacing(0)
        self.verticalLayoutQuickStart.setObjectName(_fromUtf8("verticalLayoutQuickStart"))
        self.labelQuickStart = QtGui.QLabel(self.framequickStart)
        self.labelQuickStart.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuickStart.setObjectName(_fromUtf8("labelQuickStart"))
        self.verticalLayoutQuickStart.addWidget(self.labelQuickStart)
        self.listWidgetQuickStart = QtGui.QListWidget(self.framequickStart)
        self.listWidgetQuickStart.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.listWidgetQuickStart.setObjectName(_fromUtf8("listWidgetQuickStart"))
        self.verticalLayoutQuickStart.addWidget(self.listWidgetQuickStart)
        self.verticalLayout_5.addLayout(self.verticalLayoutQuickStart)
        self.horizontalLayoutMain.addWidget(self.framequickStart)
        self.verticalLayout.addLayout(self.horizontalLayoutMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QWelcomeWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTitle.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Welcome to %s</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRecents.setText(QtGui.QApplication.translate("MainWindow", "Recents", None, QtGui.QApplication.UnicodeUTF8))
        self.labelQuickStart.setText(QtGui.QApplication.translate("MainWindow", "Quick start Actions", None, QtGui.QApplication.UnicodeUTF8))

