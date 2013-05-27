# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Mon May 27 10:20:21 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(842, 513)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayoutHeader = QtGui.QHBoxLayout()
        self.horizontalLayoutHeader.setSpacing(0)
        self.horizontalLayoutHeader.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutHeader.setObjectName(_fromUtf8("horizontalLayoutHeader"))
        self.lblIcon = QtGui.QLabel(Form)
        self.lblIcon.setText(_fromUtf8(""))
        self.lblIcon.setObjectName(_fromUtf8("lblIcon"))
        self.horizontalLayoutHeader.addWidget(self.lblIcon)
        self.lblTitle = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setStyleSheet(_fromUtf8("font: 20pt \"Verdana\";"))
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.horizontalLayoutHeader.addWidget(self.lblTitle)
        self.gridLayout.addLayout(self.horizontalLayoutHeader, 0, 0, 1, 1)
        self.horizontalLayoutMain = QtGui.QHBoxLayout()
        self.horizontalLayoutMain.setSpacing(0)
        self.horizontalLayoutMain.setMargin(9)
        self.horizontalLayoutMain.setObjectName(_fromUtf8("horizontalLayoutMain"))
        self.frameRecents = QtGui.QFrame(Form)
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
        self.lblRecents = QtGui.QLabel(self.frameRecents)
        self.lblRecents.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRecents.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRecents.setObjectName(_fromUtf8("lblRecents"))
        self.verticalLayout_2.addWidget(self.lblRecents)
        self.lwRecents = QtGui.QListWidget(self.frameRecents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lwRecents.sizePolicy().hasHeightForWidth())
        self.lwRecents.setSizePolicy(sizePolicy)
        self.lwRecents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lwRecents.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.lwRecents.setObjectName(_fromUtf8("lwRecents"))
        self.verticalLayout_2.addWidget(self.lwRecents)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayoutMain.addWidget(self.frameRecents)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutMain.addItem(spacerItem)
        self.framequickStart = QtGui.QFrame(Form)
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
        self.lblQuickStart = QtGui.QLabel(self.framequickStart)
        self.lblQuickStart.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblQuickStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQuickStart.setObjectName(_fromUtf8("lblQuickStart"))
        self.verticalLayoutQuickStart.addWidget(self.lblQuickStart)
        self.lwQuickStart = QtGui.QListWidget(self.framequickStart)
        self.lwQuickStart.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.lwQuickStart.setObjectName(_fromUtf8("lwQuickStart"))
        self.verticalLayoutQuickStart.addWidget(self.lwQuickStart)
        self.verticalLayout_5.addLayout(self.verticalLayoutQuickStart)
        self.horizontalLayoutMain.addWidget(self.framequickStart)
        self.gridLayout.addLayout(self.horizontalLayoutMain, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lblTitle.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Welcome to %s</span></p></body></html>", None))
        self.lblRecents.setText(_translate("Form", "Recents", None))
        self.lblQuickStart.setText(_translate("Form", "Quick start Actions", None))

