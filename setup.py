from setuptools import setup

setup(
    name='QWelcomeWindow',
    version='0.1',
    packages=['qwelcomewindow'],
    package_data={'qwelcomewindow': ["*.ui"]},
    url='https://github.com/ColinDuquesnoy/QDarkStyleSheet',
    license='LGPL',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A welcome window for PySide/PyQt applications. Quickly create'
                'a home window with a list of recent files and a list of quick'
                'start actions.',
    entry_points={
        'gui_scripts':
            ['QWelcomeWindow_Example = '
             'qwelcomewindow.example:main']},
)
