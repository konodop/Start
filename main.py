import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class Draw(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.showMaximized()
        self.setWindowTitle('Git')

    def initUI(self):
        self.do_paint = False

        self.button_1 = QPushButton(self)
        self.button_1.move(90, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.paint)

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
        h = random.randrange(0, 300)
        qp.setBrush(QColor(255, 207, 64))
        qp.drawEllipse(100, 100, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
