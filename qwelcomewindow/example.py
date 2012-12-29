#! /usr/bin/env python2.7
# coding: latin-1
#-------------------------------------------------------------------------------
# Copyright 2012, QWelcomeWindow
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#-------------------------------------------------------------------------------
"""
Contains a simple example of use of the QMainWindow
"""
import sys

from PySide.QtGui import QApplication
from PySide.QtGui import QLabel
from PySide.QtGui import QMainWindow
from PySide.QtGui import QStyle

from qwelcomewindow.welcome_window import QWelcomeWindow


class ExampleApp(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        style = self.app.style()
        assert isinstance(style, QStyle)
        self.welcome_win = QWelcomeWindow(
            "Welcome",
            style.standardIcon(style.SP_ComputerIcon),
            ["Test\n ~/usr/test", "Other\n ~/usr/other"],
            [(style.standardIcon(style.SP_DialogOpenButton), "Open"),
             (style.standardIcon(style.SP_DialogHelpButton), "Help")])
        self.welcome_win.recent_clicked.connect(self.open_main_window)
        self.welcome_win.action_clicked.connect(self.open_main_window)
        self.main_win = QMainWindow()
        lbl = QLabel()
        lbl.setText("Test welcome window")
        self.main_win.setCentralWidget(lbl)

    def open_main_window(self, index):
        print index
        self.welcome_win.hide()
        self.main_win.show()

    def run(self):
        self.welcome_win.show()
        self.main_win.hide()
        return self.app.exec_()


def main():
    app = ExampleApp()
    sys.exit(app.run())


if __name__ == "__main__":
    main()