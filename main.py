import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Draw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.showMaximized()
        self.setWindowTitle('Git')
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def run(self, qp):
        h = random.randrange(0, 500)
        qp.setBrush(QColor(255, 207, 64))
        qp.drawEllipse(0, 0, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())

