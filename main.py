from PyQt5 import Qt, QtGui
import pyqtgraph as pg
import numpy as np
import sys
import math


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
    print("Введите вероятность проникновения через первое окно")
    window1_prob = float(input())
    print("Введите вероятность проникновения через второе окно")
    window2_prob = float(input())
    N = 100
    k1 = 2
    k2 = 0.5
    window_range = abs(x_window1 - x_window2)
    if x_window1 > x_window2:
        x_build1 = x_window2 - window_range
        x_build2 = x_window1 + window_range
    else:
        x_build1 = x_window1 - window_range
        x_build2 = x_window2 + window_range
    y_build2 = y_window
    y_build1 = y_inf - 5
    iter_fence = x_fence / 100
    temp = 0
    array_dot = []
    while temp < x_fence:
        array_dot.append(round(temp,2))
        temp += iter_fence
    P = [(k1 / np.linalg.norm(np.array([x_window1,y_window]) - np.array([i,y_fence])) * window1_prob * k2 / np.linalg.norm(np.array([x_inf,y_inf]) - np.array([x_window1,y_window])), k1 / np.linalg.norm(np.array([x_window2,y_window]) - np.array([i,y_fence])) * window2_prob * k2 / np.linalg.norm(np.array([x_inf,y_inf])- np.array([x_window2,y_window]))) for i in array_dot]
    P_min = 1
    iter_p = 0
    num_p = 0
    for prob in P:
        for window in prob:
            if window < P_min:
                P_min = window
                num_p = iter_p
        iter_p += 1
    x_danger = array_dot[(math.floor(num_p / 2))]
    if num_p // 2 == 0:
        num_window = 1
    else:
        num_window = 2
    print("Минимальная вероятность проникновения - %s, x проникновения - %s, %s - ое окно" % (P_min, x_danger, num_window))
    full_list = [x_build1,x_build2,y_build1,y_build2,x_fence,y_fence,x_window1,x_window2,y_window,x_inf,y_inf,x_danger,num_window]
    return full_list

class Window(Qt.QWidget):

    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        view.setBackground(QtGui.QColor('green'))
        self.curve = view.plot(name="Line1")
        self.curve2 = view.plot(name="Line2")
        self.curve3 = view.plot(name="Line3")
        self.curve4 = view.plot(name="Line4")
        self.curve5 = view.plot(name="Line5")
        self.cuver6 = view.plot(name="Line6")
        self.btn = Qt.QPushButton("Построить схему проникновения")
        self.btn.clicked.connect(self.random_plot)

        layout.addWidget(Qt.QLabel("Вероятность проникновения"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

    def random_plot(self):
        full = pen_prob()
        self.curve.setData(x = [full[0],full[1],full[1],full[0],full[0]], y = [full[2],full[2],full[3],full[3],full[2]], pen = 'd')
        self.curve2.setData(x = [0,full[4],full[4],0,0], y = [full[5],full[5],0,0,full[5]])
        if full[12] == 1:
            x_window = full[6]
        else:
            x_window = full[7]
        self.curve3.setData(x = [full[11],x_window,full[9]], y = [full[5], full[8], full[10]],pen = 'r')
        self.curve4.setData(x=[full[6] - (full[6] - full[0]) / 5, full[6] + (full[6] - full[0]) / 5],
                            y=[full[8], full[8]], pen='b')
        self.curve5.setData(x=[full[7] - (full[1] - full[7]) / 5, full[7] + (full[1] - full[7]) / 5],
                            y=[full[8], full[8]], pen='b')
        self.cuver6.setData(x=[full[9] - 1, full[9] - 1, full[9] + 1, full[9] + 1, full[9] - 1],
                            y=[full[10] - 1, full[10] + 1, full[10] + 1, full[10] - 1, full[10] - 1], pen='y')

if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())
