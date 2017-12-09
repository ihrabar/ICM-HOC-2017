import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from proba import Ui_MainWindow

from collections import deque



#******************************************************************
import matplotlib
matplotlib.use("Qt5Agg")
#******************************************************************
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import time
#******************************************************************
start = time.time()

### Pokretanje glavnog prozora i odredivanje callback funkcija
class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self,MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        self.m = PlotCanvas(MainWindow, width=5, height=4)
        self.m.move(0,0)


        self.btn_bok.clicked.connect(self.m.plot)
        self.btn_quit.clicked.connect(self.closeIt)

    def fja(self):
        print("button clicked")
    def closeIt(self):
        MainWindow.close()  


### Crtanje grafa
class PlotCanvas(FigureCanvas): 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        #self.fig,self.axes = plt.subplots()

        self.canvas=FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
 
        ### uzeto iz RealtimePlot klase
        self.axis_x = deque(maxlen=100)
        self.axis_y = deque(maxlen=100)
        self.max_entries = 100
        self.lineplot, = self.axes.plot([], [], "ro-")
        self.axes.set_autoscaley_on(True)


    def plot(self):
        while True:
            self.add(time.time() - start, random.random() * 100)
            print("ok")
            plt.pause(0.1)
        ################################
  #      self.plot()
  #
  #  def plot(self):
  #      data = [random.random() for i in range(25)]
  #      ax = self.figure.add_subplot(111)
  #      ax.plot(data, 'r-')
  #      self.draw()


    ### uzeto iz RealtimePlot klase
    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim(); self.axes.autoscale_view() # rescale the y-axis

    ###################################################################



### Glavni baja
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyFirstGuiProgram(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



