import sys
from PyQt5 import QtGui, QtCore, uic, QtWidgets
 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()     	
        #load gui from .ui file
        uic.loadUi('button.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
