import sys 
from PyQt5 import QtGui 
import pyqtgraph as pg
import numpy as np
#from time import sleep 


app = QtGui.QApplication(sys.argv)

win = pg.GraphicsWindow(title="Plotting examples")
win.resize(1000,600)

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

p1 = win.addPlot(title="Basic plot")
p1.plot(x)  ## setting pen=None disables line drawing

p2 = win.addPlot(title="Drawing with points")
p2.plot(y, pen=(255,0,0), symbolBrush=(255,0,0), symbolPen='w')

win.nextRow()

p3 = win.addPlot(title="Parametric, grid enabled")
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p3.plot(x, y)
p3.showGrid(x=True, y=True)


p3 = win.addPlot(title="Multiple curves")
p3.plot(x, pen=(255,0,0), name="Sinus")
p3.plot(y, pen=(0,255,0), name="Cosinus")



status = app.exec_()
sys.exit(status)