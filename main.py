import random

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt6.QtGui import QPainter, QColor
from mainUI import PyQi

import io
import sys
class MainWindow(PyQi):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.SetupUI()


    def run(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.begin(self)
            self.draw_sirc(painter)

    def draw_sirc(self, painter):
        painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        size = random.randint(0, 50)
        painter.drawEllipse(QPoint(random.randint(50, 250), random.randint(50, 250)), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())