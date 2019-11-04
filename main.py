from PyQt5 import Qt
import pyqtgraph as pg
import numpy as np
import sys


def pen_prob():
    print("Введите Xзабора < 50")
    x_fence = int(input())
    while x_fence >= 50:
        print("Введите Xзабора < 50")
        x_fence = int(input())
    print("Введите Yзабора < 50")
    y_fence = int(input())
    while y_fence >=50:
        print("Введите Yзабора < 50")
        y_fence = int(input())
    print("Введите y окна")
    y_window = int(input())
    print("Введите x окна 1")
    x_window1 = int(input())
    print("Введите x окна 2")
    x_window2 = int(input())
    print("Введите x информации")
    x_inf = int(input())
    print("Введите y информации")
    y_inf = int(input())
    N = 100
    k1 = 2
    k2 = 0.5
    iter = x_fence / 100
    temp = 0
    array_dot = []
    while temp < x_fence:
        array_dot.append(round(temp,2))
        temp += iter





class Window(Qt.QWidget):

    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line1")
        self.curve2 = view.plot(name="Line2")

        self.btn = Qt.QPushButton("Построить графики")
        self.btn.clicked.connect(self.random_plot)

        layout.addWidget(Qt.QLabel("Вероятность проникновения"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

    def random_plot(self):
        pen_prob()
        self.curve.setData(x = [0,1], y = [4,7])
        self.curve2.setData(x = [1,0], y = [6,5])


if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())
