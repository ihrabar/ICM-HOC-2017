import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic
 

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()     	
        #load gui from .ui file
        uic.loadUi('button.ui', self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


