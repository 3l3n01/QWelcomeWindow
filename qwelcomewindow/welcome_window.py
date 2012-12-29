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
"""Contains the QWelcomeWindow class.
The QWelcomeWindow is a QMainWindow made to quickly create a nice looking home
window for a PySide/PyQt4 application that shows a list of recent documents and
a list of quick start actions.
"""
import logging
import sys

# detect PySide or PyQt4
__use_py_side = True
try:
    import PySide
    print "Using PySide"
except ImportError:
    PySide = None
    __use_py_side = False
    try:
        import PyQt4
        print "Using PyQt4"
    except ImportError as e:
        PyQt4 = None
        python_qt = None
        logging.error("PyQt4 nor PySide were found... You need to install one "
                      "of these packages.")
        raise e
if __use_py_side:
    from PySide.QtCore import Signal
    from PySide.QtCore import Slot
    from PySide.QtGui import QIcon
    from PySide.QtGui import QListWidgetItem
    from PySide.QtGui import QMainWindow
    from qwelcomewindow import ui_pyside as ui
else:
    from PyQt4.QtCore import pyqtSignal as Signal
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4.QtGui import QIcon
    from PyQt4.QtGui import QListWidgetItem
    from PyQt4.QtGui import QMainWindow
    from qwelcomewindow import ui_pyqt as ui


class QWelcomeWindow(QMainWindow):
    """ A QMainWindow that shows a list of recents files/actions and a list of
    quick start actions.

    This class can be used to speed up the development of a welcome window in
    a PySide/PyQt application.

    It is built by providing the application title/icon, the list of recents
    files/documents (strings) and the list of quick start action. A quick start
    action is a tuple made up of one icon and the action string.

    It exposes two signals:
        - recent_clicked: emitted whenever the user click on a recent item.
        - action_clicked: emitted whenever the user click on a quick start
          action.
    """
    recent_clicked = Signal(int)
    action_clicked = Signal(int)

    def __init__(self, title, icon, recents, quick_start_actions,
                 parent=None):
        assert isinstance(icon, QIcon)
        QMainWindow.__init__(self, parent)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.ui.labelTitle.setText(title)
        self.ui.labelIcon.setPixmap(icon.pixmap(32, 32))
        self.setWindowIcon(icon)
        self.recents = recents
        for recent in recents:
            self.ui.listWidgetRecents.addItem(recent)
        self.qsa = quick_start_actions
        for qsa in quick_start_actions:
            assert len(qsa) == 2
            icon = qsa[0]
            txt = qsa[1]
            item = QListWidgetItem(QIcon(icon), txt)
            self.ui.listWidgetQuickStart.addItem(item)

    @Slot(QListWidgetItem)
    def on_listWidgetRecents_itemClicked(self, item):
        self.emit_recent_clicked(item)

    def emit_recent_clicked(self, item):
        for cpt, r in enumerate(self.recents):
            if r == str(item.text()):
                print "Recent clicked: %d" % cpt
                self.recent_clicked.emit(cpt)
                return
        print "Error: could not found the item in the recents list"

    @Slot(QListWidgetItem)
    def on_listWidgetQuickStart_itemClicked(self, item):
        self.emit_action_clicked(item)

    def emit_action_clicked(self, item):
        for cpt, a in enumerate(self.qsa):
            if a[1] == str(item.text()):
                print "Quick start action clicked: %d" % cpt
                self.recent_clicked.emit(cpt)
                return
        print "Error: could not found the item in the quick start action list"
