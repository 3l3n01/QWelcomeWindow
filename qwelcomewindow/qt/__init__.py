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
Detects the qt bindings to use (PyQt4 or PySide)

If a specific qt bindings has already been imported or is specified in sys.argv,
PCEF will use this bindings.
Else PCEF will first try to import and use PyQt4, if it fails it will
attempt to import and use PySide.

You can force to use one specific bindings by appending ["--pyside"] or
["--pyqt"] to sys.argv::

    # force the use of pyside:
    import sys
    sys.argv += ["--pyside"]
    import pcef  # will use pyside


The qt package is automatically imported when importing pcef which other
application to write qt bindings independant applications::

    import os
    import sys
    import pcef


    app = pcef.QtGui.QApplication(sys.argv)
    editor = pcef.QCodeEdit()
    # show the QT api in the window title
    editor.setWindowTitle(os.environ["QT_API"])
    editor.show()
    app.exec_()
"""
import os
import sys
# check if a qt bindings has already been imported
if "PyQt4" in sys.modules or "--pyqt" in sys.argv:
    os.environ.setdefault("QT_API", "pyqt")
elif "PySide" in sys.modules or "--pyside" in sys.argv:
    os.environ.setdefault("QT_API", "pyside")
else:
    try:
        import PyQt4
    except ImportError:
        # try pyside
        try:
            import PySide
        except ImportError:
            os.environ.setdefault("QT_API", None)
            sys.exit(-1)
        else:
            os.environ.setdefault("QT_API", "pyside")
    else:
        os.environ.setdefault("QT_API", "pyqt")
# setup pyqt api to version 2
if os.environ["QT_API"] == "pyqt":
    import sip
    try:
        sip.setapi("QString", 2)
        sip.setapi("QVariant", 2)
    except:
        pass