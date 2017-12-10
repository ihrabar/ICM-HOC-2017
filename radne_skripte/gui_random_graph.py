import random
import sys
import serial.tools.list_ports
import time
import csv
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic

############## Za dodati ##############

############# PRVO ###################
######### Primanje podataka sa serijskog porta
# 1) Spajanje na serijski port 
#       - nadi u Device manager-u ili u Arduino IDE-u i provjeri na koji serijski port je spojen Arduino
#       - pogledaj u kod-u koji je programiran na Arduino na kojem baudrate-u se događa komunikacija
#       - dodati funkciju: self.ser = serial.Serial(IME PORTa, BAUDRATE)
#       - isprazni buffer od starih podataka: self.ser.reset_input_buffer()
# 2) Zamijeni generiranje random brojava sa citanjem brojeva sa serije 
#       - funkcija:data = self.ser.readline().decode().split('\r\n')  i data_scale = float(data[0]) * 5.0 / 1024 

############ DRUGO ####################
######## Omoguciti spremanje grafa
# 1) Nacrtati u Qt Designer-u gumb koji će spremati prikupljena mjerenja
# 2) Napisati callback funkciju koda obavlja spremanje podataka u .csv file
#       - kopirati funkciju sa prethodne radionice (pisanje u SCV), pogledati na ploci
# 3) Povezati gumb i napisanu funkciju
#       - npr. "self.btn_save.clicked.connect("napisana funkcija")

############## TRECE ###################
######### Setiranje osi grafa
# 1) Nacrtati u Qt Designer-u dva prozora u koji se mogu upisati brojecvi (vrsta "Line Edit")
# 2) Napisati callback funkcije koje se pozivaju kada se nova vrijednost upise u prozor 
#       - npr. def Ymin_changed(self):...  i Ymax_changed(self)
#       - citanje vrijednosti u prozoru  sa ".text()"
#       - vrijednost je potrebno pretvoriti u float
#       - postavljanje y range grafa se radi sa: self.p.setYRange("minimalna vrijednost y osi", "maksimalna vrijednost y osi")
# 3) Povezati prozore sa napisanim callback funkcijama
#       - pozvati napisane funkcije uz ".textChanged.connect()"

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        #load gui from .ui file
        uic.loadUi('gui_random_graph.ui', self)

        # Y range 
        self.Ymin=0.0 
        self.Ymax=5.0 

        #set a graph plot 
        self.p=self.graphicsView.getPlotItem()
        self.p.setYRange(self.Ymin, self.Ymax)
        self.curve = self.p.plot()

        # callback functions for buttons
        self.btn_quit.clicked.connect(self.closeIt)
        self.btn_start.clicked.connect(self.plotter)
        self.btn_stop.clicked.connect(self.stop_plotter)
        self.btn_clear.clicked.connect(self.clear)


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

        self.data.append(data_scale)
        self.data_time.append(current_time)
        self.curve.setData(self.data_time, self.data)

    def closeIt(self):
        exit(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
