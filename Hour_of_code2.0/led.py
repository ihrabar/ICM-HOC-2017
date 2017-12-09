import sys
#import pyqtgraph as pg
import serial
from PyQt5 import QtGui, QtCore, uic, QtWidgets

# Provjeri u Device manageru ili Arduino IDEu na koji je port spojen Arduino
ser=serial.Serial("COM8",115200)

#QtWidgets.QMainWindow
#QtWidgets.QAp

class MainWindow(QtWidgets.QMainWindow):#QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        #load gui from .ui file
        uic.loadUi('led.ui', self)

        self.btn_led.clicked.connect(self.send_value)

    def send_value(self):
        print(self.sld_led.sliderPosition())
        ser.write(bytes([self.sld_led.sliderPosition()]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)#QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())