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
Setup script for install QWelcomeWidget
"""
from setuptools import setup

setup(
    name='QWelcomeWindow',
    version='1.1',
    packages=['qwelcomewindow', 'qwelcomewindow.qt'],
    package_data={'qwelcomewindow': ["*.ui"]},
    url='https://github.com/ColinDuquesnoy/QWelcomeWindow',
    license='LGPL v3',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A welcome window/widget for PySide applications. '
                'Quickly create a home window with a list of recent files and a '
                'list of quick start actions, inspired from the IntelliJ Idea '
                'welcome window (Pycharm,...)',
    entry_points={'gui_scripts':
            ['QWelcomeWindow_Example = '
             'qwelcomewindow.widget:main']},
)
