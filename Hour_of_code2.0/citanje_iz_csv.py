import csv

import sys
from PyQt5 import QtGui
import pyqtgraph as pg



# Napisi ime .csv file-a iz kojih ces citati podatke
filename='13.csv'

podaci=[]
# otvori csv file
with open(filename, 'r') as csv_file:

    # otvori .csv file u notebook-u i pogledaj koji delimiter se koristi
    wr = csv.reader(csv_file, delimiter=',')
    # zapisi podatke u .csv
    for row in wr:
        podaci.append(row)

# promjena liste stringova u listu floatova
mjerenja=list(map(float,podaci[0]))
vrijeme=list(map(float,podaci[1]))



win = pg.GraphicsWindow()
p1 = win.addPlot()
p1.plot(vrijeme, mjerenja)

app=QtGui.QApplication(sys.argv)
status=app.exec_()
sys.exit(status)

