#no need to install anything
import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
# just change the name
from gui import Ui_MainWindow

# thu vien mo rong
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import mysql.connector

timer = QTimer()

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut an
        self.uic.Button_start.clicked.connect(self.show_diagram)
        self.uic.Button_stop.clicked.connect(self.stop_update)

    def stop_update(self):
        timer.stop()

    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart())
        elif self.uic.screen is not None:
            timer.start(2000)

    def show(self):
        # command to run
        self.main_win.show()

class show_chart(FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        timer.timeout.connect(self.loop)
        timer.start(2000)

        plt.ion()
    def loop(self):
        db = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', database='new_database')
        # lenh chay
        code_8 = 'SELECT name,km FROM distance'
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(code_8)  # make database
        result = mycursor.fetchall()

        datas = (result[0][0], result[1][0], result[2][0], result[3][0], result[4][0])
        datas1 = (result[0][1], result[1][1], result[2][1], result[3][1], result[4][1])
        explode = (0.2, 0.1, 0, 0, 0)
        print("label: ", datas)
        print("data: ", datas1)

        self.ax.clear()
        self.ax.pie(datas1, labels=datas, autopct='%1.2f%%', explode=explode,
               shadow=True, startangle=90)  # , explode=explode

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())