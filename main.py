
# CREATED BY EDUARDO PEREZ REGIN, 2020/05/20

#!usr/bin/env python3

import sys
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
