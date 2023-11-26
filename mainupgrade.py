import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Btn:
    def __init__(self):
        self.bt = QPushButton('Кнопка', self)
        self.bt.move(250, 50)
        self.bt.setCheckable(True)
        self.bt.clicked.connect(self.paint)


class Draw(QWidget, Btn):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(0, 0, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
