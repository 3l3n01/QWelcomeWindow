#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QWelcomeWidget - An easy to customize welcome window

# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
Bindings independant QtGui module
"""
import os
if os.environ['QT_API'] == 'pyqt':
    from PyQt4.QtGui import *
else:
    from PySide.QtGui import *