import sys 
from PyQt5 import QtGui 
import pyqtgraph as pg
import numpy as np


win = pg.GraphicsWindow(title="Plotting examples")
win.resize(1000,600)

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

p1 = win.addPlot(title="Basic plot")
p1.plot(x, pen=(0,0,255))  ## setting pen=None disables line drawing
p1.setLabel( 'left', text="x", units="m", unitPrefix=None)


p2 = win.addPlot(title="Drawing with points")
p2.plot(y, pen=(255,0,0), symbol="o", symbolBrush=(255,0,0), symbolPen='w', symbolSize=5)

win.nextRow()

p3 = win.addPlot(title="Multiple curves - random")
p3.plot(x, pen=(255,0,0))
p3.plot(y, pen=(0,255,0))
p3.showGrid(x=True, y=True)

t=np.linspace(0,100,1000)
x=5*t
y=3*t
p4 = win.addPlot(title="Multiple curves - lines")
p4.addLegend(size=(0, 30), offset=(10, 10))
p4.plot(x, pen=(255,0,0), name="Slope 5")
p4.plot(y, pen=(0,255,0), name="Slope 3")
p4.showGrid(x=True, y=True)

win.nextRow()

x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))

p5 = win.addPlot(title="Multiple curves - sin/cos")
p5.addLegend(size=(30, 30), offset=(360, 20))
p5.plot(x, pen=(255,0,0), name="Sinus")
p5.plot(y, pen=(0,255,0), name="Cosinus")
p5.showGrid(x=True, y=True)


p6 = win.addPlot(title="Parametric sin/cos")
p6.plot(x, y)
p6.showGrid(x=True, y=True)
p6.setLabel( 'bottom', text="sin", units="m")
p6.setLabel( 'left', text="cos", units="m")

app = QtGui.QApplication(sys.argv)
status = app.exec_()
sys.exit(status)