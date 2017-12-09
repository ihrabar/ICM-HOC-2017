import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic
 

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()     	
        #load gui from .ui file
        uic.loadUi('izbornik_calculator.ui', self)
        #add buttons, boxes, widgets ... and attach functions
        self.calc_button.clicked.connect(self.calculate)
        self.izbornik.addItems(["+", "-", "*","/"])
        #self.izbornik.currentIndexChanged.connect(self.odabir_operacije)
        #global operation

    #def odabir_operacije(self):
        #global operation
        #operation=self.izbornik.currentText()
        #print(operation)
    def calculate(self):
        global operation
        num1=int(self.first_box.toPlainText())
        num2=int(self.sec_box.toPlainText())
        operation=self.izbornik.currentText()
        if operation=="+":
            result=num1+num2
        elif operation=="-":
            result=num1-num2
        elif operation=="*":
            result=num1*num2
        else:
            result=num1/num2
        self.result_box.setText(str(result))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


