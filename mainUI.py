


import random

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt6.QtGui import QPainter, QColor
class PyQi(QMainWindow):
    def SetupUI(self):
        self.setGeometry(300, 300, 300, 300)

        self.yellow_button = QPushButton(self)
        self.yellow_button.setText('нарисовать круг')
        self.yellow_button.setGeometry(150, 150, 100, 35)
        self.yellow_button.clicked.connect(self.run)