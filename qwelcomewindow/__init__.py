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
QWelcome window is a python package that let you quickly create a home
window/widget for your PySide application.

Classes:
    - qwelcomewindow.QWelcomeWidget
    - qwelcomewindow.ColorScheme
    - qwelcomewindow.DarkColorScheme
"""
from qwelcomewindow.widget import ColorScheme, DarkColorScheme, QWelcomeWidget
__all__ = ['ColorScheme', 'DarkColorScheme', 'QWelcomeWidget']
