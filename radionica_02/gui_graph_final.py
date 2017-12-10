import random
import sys
import serial.tools.list_ports
import time
import csv
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        #load gui from .ui file
        uic.loadUi('gui_graph_final.ui', self)

        #serial connection
        #self.ser = serial.Serial("COM38", 115200) #SERIAL
        #print("connected to: " + self.ser.portstr) #SERIAL
        #self.ser.reset_input_buffer() #SERIAL

        # Y range 
        self.Ymin=0.0 #YRANGE
        self.Ymax=5.0 #YRANGE
        self.ln_ymin.textChanged.connect(self.Ymin_changed) #YRANGE
        self.ln_ymax.textChanged.connect(self.Ymax_changed) #YRANGE

        #set a graph plot 
        self.p=self.graphicsView.getPlotItem()
        self.p.setYRange(self.Ymin, self.Ymax)
        self.curve = self.p.plot()

        # callback functions for buttons
        self.btn_quit.clicked.connect(self.closeIt)
        self.btn_start.clicked.connect(self.plotter)
        self.btn_stop.clicked.connect(self.stop_plotter)
        self.btn_clear.clicked.connect(self.clear)

        # saveing to CSV
        self.btn_save.clicked.connect(self.save_CSV) #CSV

    def plotter(self):
        self.data = [0]
        self.data_time =[0]
        self.start = time.time()
        self.curve = self.p.plot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)

    def stop_plotter(self):
        self.timer.disconnect()

    def clear(self):
        self.p.clear()

    def updater(self):
        data = random.randint(0, 1023)
        data_scale = data * 5.0 / 1024
        current_time=time.time()-self.start
        #data = self.ser.readline().decode().split('\r\n') #SERIAL
        #data_scale = float(data[0]) * 5.0 / 1024 #SERIAL
        self.data.append(data_scale)
        self.data_time.append(current_time)
        self.curve.setData(self.data_time, self.data)

    def closeIt(self):
        exit(0)

    def Ymin_changed(self): #YRANGE
        if self.ln_ymin.text()!='':
            self.Ymin=float(self.ln_ymin.text())
            self.p.setYRange(self.Ymin, self.Ymax)
    def Ymax_changed(self): #YRANGE
        if self.ln_ymax.text()!='':
            self.Ymax=float(self.ln_ymax.text())
            self.p.setYRange(self.Ymin, self.Ymax)

    def save_CSV(self):  #CSV
        self.filename = "measurements.csv"
        self.length=len(self.data)
        # otvori csv file
        with open(self.filename, 'w', newline='') as self.csv_file:
            wr = csv.writer(self.csv_file)
            for i in range(self.length):
                this_row=[self.data_time[i], self.data[i]]
                wr.writerow(this_row)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
