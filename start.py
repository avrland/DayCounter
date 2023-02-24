import sys
import json
import time
import subprocess
import traceback
import asyncio
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog

class MainApp:
    def __init__(self):
        pass

    def ShowMainWindow(self):
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = MainApp()
    controller.ShowMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()