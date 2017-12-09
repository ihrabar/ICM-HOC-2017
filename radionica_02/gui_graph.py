import random
import sys
import serial.tools.list_ports
import time
import csv
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic

plot_data_nr=200



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        #load gui from .ui file
        uic.loadUi('gui_graph.ui', self)


        #flag for connection checking -> enables disconnection with the same button
        self.connected=False
        # callback functions for buttons
        self.btn_quit.clicked.connect(self.closeIt)
        self.btn_connect.clicked.connect(self.plotter)



        ############## Za dodati ##############

        ############## PRVO ###################
        ######### Setiranje osi grafa
        # 1) Nacrtati u Qt Designer-u dva prozora u koji se mogu upisati brojecvi
        # 2) Napisati callback funkcije koje se pozivaju kada se nova vrijednost upise u prozor
        # 3) Povezati prozore sa napisanim callback funkcijama
        # 4) Dopuni funkciju upisujuci varijable umjesto teksta u navodnicima
        #self.graphicsView.setYRange("minimalna vrijednost y osi", "maksimalna vrijednost y osi")

        ############# DRUGO ###################
        ######### Primanje podataka sa serijskog porta
        # 1) Nadi u Device manager-u ili u Arduino IDE-u i provjeri na koji serijski port je spojen Arduino
        # 2) Pogledaj u kod-u koji je programiran na Arduino na kojem baudrate-u se događa komunikacija
        # #self.ser = serial.Serial(IME PORTa, BAUDRATE)
        # 3) u funkciji "updater" umjesto uzimanja random podataka uzimajte podatke sa serijskog porta

        ############ TRECE ####################
        ######## Omoguciti spremanje grafa
        # 1) Nacrtati u Qt Designer-u gumb koji će spremati prikupljena mjerenja
        # 2) Napisati callback funkciju koda obavlja spremanje podataka u .csv file
        # 3) Dopuni sljedecu liniju tako da poziva napisanu callback funkciju
        #self.btn_save.clicked.connect("")

        ####################

### UZ PADAJUCU LISTU
    def serial_ports(self):
        return serial.tools.list_ports.comports()
####################
    def plotter(self):
        self.data = [0]
        self.curve = self.graphicsView.getPlotItem().plot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)

        self.timer.start(0)

    def updater(self):
        rand_number = random.randint(0, 1023)
        data_scale = rand_number * 5.0 / 1024
        self.data.append(data_scale)
        self.curve.setData(self.data)

    def closeIt(self):
        exit(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
