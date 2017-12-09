import sys 
from PyQt5 import QtGui 
import pyqtgraph as pg
import numpy as np

#1. niz brojeva  
#x = [0, 1, 2, 4, 3, 5, 1, 2]
#pg.plot(x)

#2. pravac + definiranje boje 
x=np.linspace(1,100,300)
y=5*x
pg.plot(x,y,pen=(0,255,0))

#3. generiranje random brojeva 
x = np.random.normal(size=200)
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
x = np.random.random_integers(1,30,size=200)
#pg.plot(x)

#4. generiranje dva random niza 
x=np.random.random_integers(1,30,size=200)
y=np.random.random_integers(10,70,size=200)
pg.plot(x,y,pen=(255,255,0)) # zuta

#5. nema linije, ali ima tocke oznacene 
#pg.plot(x,y, pen=None, symbol="x") 
# kruzici, symbolBrush- unutarnja boja kruzica, symbolPen - vanjski obrub
#pg.plot(x,y, pen=(0,0,255), symbol="o", symbolBrush=(255,0,0), symbolPen=(255,255,0)) 



app = QtGui.QApplication(sys.argv)
status = app.exec_()
sys.exit(status)