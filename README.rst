QWelcomeWindow
---------------------

*1.1*

A generic welcome window for PySide and PyQt applications.

It display a list of recent files/documents and a list of quick start actions 
(icons associated with a text).

The purpose of this python package is to provide a class to quickly create nice
looking home window to use in any PySide applications.

It comes with two color scheme, a white/light gray theme (default) and a dark
color scheme.

*Since version 1.0 the welcome window is just a regular QWidget that you can drop wherever you want, in a stacked widget for example*

License
----------------------

The software is licensed under the LGPL version 3 as specificied in the file
COPYING.

Installation
---------------------

*Requires python-setuptools and python-pyside to be installed.*


From **pypi**::

    sudo easy_install QWelcomeWindow


or from **source**::

    python setup.py install

Usage
---------------------

You can run the example script by running the following command::

    QWelcomeWindow_Example

Here is an example sample code::

    import qwelcomewindow

    # create the widget, give it the app name, icon and a color scheme (you can
    # create your own)
    widget = qwelcomewindow.QWelcomeWidget(app_name="Your app name",
        app_icon:QIcon("Your_AppIcon.png"),
        color_scheme=qwelcomewindow.ColorScheme())

    # add a recent action
    widget.add_action(qwelcomewindow.QWelcomeWidget.ActionType.Recent,
        "~/file.dat", QIcon("Your_fileIcon.png"))

    # add a quick start action
    widget.add_action(qwelcomewindow.QWelcomeWidget.ActionType.QuickStart,
        "Create a new file", QIcon("Your_newFileIcon.png"))

    # connect to the widget signals
    widget.recent_action_triggered.connect(self.on_recent_clicked)
    widget.quick_start_action_triggered.connect(self.on_quick_start_clicked)

    # add the widget to your ui, for example:
    self.ui.stackedWidget.insertWidget(0, widget)


PyQt note
----------

QWelcomeWindow requires **QString and QVariant API v2**. If you are using PyQt, **import qwelcomewindow before any other 
PyQt modules** or setup the sip api yourself before importing qwelcomewindow.


Forcing a specific Qt bindings
------------------------------------

There are two ways to select a specific qt bindings:

  * import PySide or import PyQt4 before import QWelcomeWindow
  * append ["--pyside"] or ["--pyqt"] to sys.argv




