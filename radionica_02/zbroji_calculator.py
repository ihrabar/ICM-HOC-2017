import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic
 
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()     	
        #load gui from .ui file
        uic.loadUi('zbroji_calculator.ui', self)
        #add buttons, boxes, widgets ... and attach functions
        self.sum_button.clicked.connect(self.ispisi_zbroj)
    def ispisi_zbroj(self):
        num1=float(self.first_box.toPlainText())
        num2=float(self.sec_box.toPlainText())
        self.result_box.setText(str(num1+num2))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


