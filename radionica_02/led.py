import sys
import pyqtgraph as pg
import serial
from PyQt5 import QtGui, QtCore, uic


ser=serial.Serial("COM38",115200)
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        #load gui from .ui file
        uic.loadUi('led.ui', self)

        self.btn_led.clicked.connect(self.send_value)

    def send_value(self):
        led_value=self.sld_led.sliderPosition()
        print(led_value)
        ser.write(bytes([led_value]))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())