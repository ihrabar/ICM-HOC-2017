import sys
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore, uic
 
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()     	
        #load gui from .ui file
        uic.loadUi('prepis_teksta.ui', self)
        #add buttons, boxes, widgets ... and attach functions
        self.button_stisni.clicked.connect(self.ispisi_tekst)
    def ispisi_tekst(self):
    	tekst=self.unos_teksta.toPlainText()
    	self.ispis_teksta.setText("Unesen tekst: " + tekst)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


