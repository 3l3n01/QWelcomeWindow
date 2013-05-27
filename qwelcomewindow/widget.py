#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QWelcomeWindow - An easy to customize welcome window

# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
Main module: define the welcome window widget.
"""
import os
import sys
from qwelcomewindow.qt import QtGui, QtCore


class ColorScheme(object):
    """
    Define a color scheme for easy customisation of the QWelcomeWidget's
    stylesheet.

    There are 7 colors to define:
        - background color
        - title background color
        - text_color
        - border_color:
        - selection_background_color
        - selection_color
        - hover_color: The hover background color

    Color are defined as string with web/hex format: "#rrggbbb"

    The default colors define a white/light gray color scheme.
    """

    def __init__(self):
        #: widgets background
        self.background_color = "#FFFFFF"
        #: titles background (app title, recent title, quick start action title)
        self.title_background_color = "#DDDDDD"
        #: texts color
        self.text_color = "#555555"
        # frames border color
        self.border_color = "#cccccc"
        # item selection background color
        self.selection_bck_color = "#aaaaaa"
        #: selected item text color
        self.selection_color = "#FFFFFF"
        #: selected item hover background color
        self.hover_color = "#bbbbbb"


class DarkColorScheme(ColorScheme):
    """
    Define a dark color scheme for easy customization of the stylesheet.
    """

    def __init__(self):
        super(DarkColorScheme, self).__init__()
        self.background_color = "#3C3F41"
        self.title_background_color = "#4b4b4b"
        self.text_color = "#C5C5C5"
        self.border_color = "#555555"
        self.selection_bck_color = "#343434"
        self.selection_color = "#C5C5C5"
        self.hover_color = "#343434"


STYLESHEET = """
QWidget
{
    background-color: %(background_color)s;
    color: %(text_color)s;
}

QFrame
{
    border: 1px solid %(border_color)s;
}

QListWidget
{
    border: none;
}

QListView::item
{
    padding: 5px;
}

QListView::item:selected
{
    border: 1px solid %(border_color)s;
}

QListView::item:selected:!active
{
    background: %(selection_bck_color)s;
    color: %(selection_color)s;
}

QListView::item:selected:active
{
    background: %(selection_bck_color)s;
    color: %(selection_color)s;
}

QListView::item:hover
{
    background: %(hover_color)s;
}

QLabel
{
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 3px;
    padding-right: 0px;
    border: none;
    background-color: %(title_background_color)s;
};
"""


class QWelcomeWidget(QtGui.QWidget):
    """
    A QWidget used to display an application home page (Welcome to "app_name",
    with a list of quick start actions and a list of recent (filename) actions.

    Usage:
        - create the widget and tell him the application name and icon.
          Optionnaly set the color scheme.

        - add quick start action and recent action with the add_action method.

        - add the widget to your ui (for example, set it at the first page
         in a QStackedWidget)
    """

    class ActionType:
        """
        Enumerates the possible action types.
        """
        #: Defines the recent file action type
        Recent = 0
        # Defines the quick start action type
        QuickStart = 1

    # signal emitted when a quick start action is triggered
    quick_start_action_triggered = QtCore.Signal(str)
    # signal emitted when a recent action is triggered
    recent_action_triggered = QtCore.Signal(str, str)

    def set_app_icon(self, app_icon):
        if app_icon:
            self.ui.lblIcon.setPixmap(app_icon.pixmap(32, 32))

    def set_app_name(self, app_name):
        self.ui.lblTitle.setText("Welcome to %s" % app_name)

    def __init__(self, parent=None,
                 app_name="", app_icon=None, color_scheme=None):
        """
        Create the welcome window.

        It will create an empty quick start action/recent files lists that you
        must populate with your own actions (using the add_action method).

        :param app_name: Application name. The widget title label will show
                         "Welcome to <app_name>"

        :param app_icon: The application icon, displayed befor the welcome label

        :param color_scheme: A color scheme to easily customize the widget's
                             stylesheet
        """
        QtGui.QWidget.__init__(self)
        if os.environ["QT_API"] == "pyside":
            from qwelcomewindow import pyside_widget_ui
            self.ui = pyside_widget_ui.Ui_Form()
            self.ui.setupUi(self)
        else:
            from qwelcomewindow import pyqt_widget_ui
            self.ui = pyqt_widget_ui.Ui_Form()
            self.ui.setupUi(self)
        self.set_color_scheme(color_scheme)
        self.set_app_icon(app_icon)
        self.set_app_name(app_name)

    def set_color_scheme(self, color_scheme):
        """
        Sets the widget color scheme

        :param color_scheme: Color scheme instance
        :type color_scheme: ColorScheme
        """
        if color_scheme is None:
            color_scheme = ColorScheme()
        stylesheet = STYLESHEET % {
            "background_color": color_scheme.background_color,
            "title_background_color": color_scheme.title_background_color,
            "text_color": color_scheme.text_color,
            "border_color": color_scheme.border_color,
            "selection_bck_color": color_scheme.selection_bck_color,
            "selection_color": color_scheme.selection_color,
            "hover_color": color_scheme.hover_color}
        self.setStyleSheet(stylesheet)

    def add_action(self, action_type, action_txt, action_icon=None, data=None):
        """
        Adds an action to one of the two list widgets (recent or quick start
        actions).

        :param action_type: Action type:
                                - a quick start action (0)
                                - a recent file action (1)
        ;param action_type: qwelcomewindow.QWelcomeWidget.ActionType.Recent or
                            qwelcomewindow.QWelcomeWidget.ActionType.QuickStart

        :param action_txt: Text displayed in the list widget
        :type action_txt: str or unicode

        :param action_icon: Icon displayed before the action_txt, optional.
        :type action_icon: QIcon
        """
        item = QtGui.QListWidgetItem(action_txt)
        if action_icon:
            item.setIcon(action_icon)
        if data:
            item.setData(32, data)
            item.setData(3, data)
        item.setData(0, action_txt)
        if action_type == self.ActionType.QuickStart:
            self.ui.lwQuickStart.addItem(item)
        else:
            self.ui.lwRecents.addItem(item)

    def set_action_text(self, action_type, index, text):
        if action_type == self.ActionType.QuickStart:
            item = self.ui.lwQuickStart.item(index)
        else:
            item = self.ui.lwRecents.item(index)
        item.setText(text)

    def clear_recent_actions(self):
        """
        Clears the recent actions list
        """
        self.ui.lwRecents.clear()

    @QtCore.Slot(QtGui.QListWidgetItem)
    def on_lwRecents_itemClicked(self, item):
        self.ui.lwQuickStart.clearSelection()
        self.recent_action_triggered.emit(item.text(), item.data(32))

    @QtCore.Slot(QtGui.QListWidgetItem)
    def on_lwQuickStart_itemClicked(self, item):
        self.ui.lwRecents.clearSelection()
        self.quick_start_action_triggered.emit(item.text())


#///////////////////////////////////////////////////////////////////////////////
# Example
#///////////////////////////////////////////////////////////////////////////////
widget = None
theme = None

def on_recent_acton_clicked(text, data):
    """
    Shows a message box with the name of the triggered recent action.
    """
    QtGui.QMessageBox.information(None, "Recent file triggered",
                                  "You clicked on the recent item: %s" % text)


def on_quick_start_action_clicked(text):
    """
    Shows a message box with the name of the triggered quick start action.
    """
    if text == "Help":
        QtGui.QMessageBox.information(
            None, "QWelcomeWindow",
            "QWelcomeWindow is a small python package that you can use to "
            "quickly create a home window for your PySide application.")
    elif text == "Try dark theme" or text == "Try white theme":
        global widget, theme
        if theme is None:
            theme = DarkColorScheme()
            widget.set_color_scheme(theme)
            widget.set_action_text(QWelcomeWidget.ActionType.QuickStart,
                                   2, "Try white theme")
        else:
            widget.set_color_scheme(ColorScheme())
            theme = None
            widget.set_action_text(QWelcomeWidget.ActionType.QuickStart,
                                   2, "Try dark theme")
    else:
        QtGui.QMessageBox.information(
            None, "Quick start action triggered",
            "You clicked on the quick start action: %s" % text)


def main():
    """
    Simple example
    """
    app = QtGui.QApplication(sys.argv)

    # create some standard icons
    style = app.style()
    file_icon = style.standardIcon(style.SP_FileIcon)
    open_icon = style.standardIcon(style.SP_DialogOpenButton)
    help_icon = style.standardIcon(style.SP_DialogHelpButton)
    reload_icon = style.standardIcon(style.SP_BrowserReload)

    # create the widget
    global widget
    widget = QWelcomeWidget(app_name="QWelcomeWindow",
                            app_icon=style.standardIcon(style.SP_ComputerIcon))

    # add quick start actions
    widget.add_action(QWelcomeWidget.ActionType.QuickStart, "Open something",
                      open_icon)
    widget.add_action(QWelcomeWidget.ActionType.QuickStart, "Help",
                      help_icon)
    widget.add_action(QWelcomeWidget.ActionType.QuickStart, "Try dark theme",
                      reload_icon)

    # add recent file actions
    widget.add_action(QWelcomeWidget.ActionType.Recent, "File00.xyz",
                      file_icon)
    widget.add_action(QWelcomeWidget.ActionType.Recent, "File01.abc",
                      file_icon)
    widget.add_action(QWelcomeWidget.ActionType.Recent, "File14.mno",
                      file_icon)

    # connect to the widget's signals
    widget.recent_action_triggered.connect(on_recent_acton_clicked)
    widget.quick_start_action_triggered.connect(on_quick_start_action_clicked)

    # run the gui app
    widget.show()
    app.exec_()


if __name__ == "__main__":
    main()
