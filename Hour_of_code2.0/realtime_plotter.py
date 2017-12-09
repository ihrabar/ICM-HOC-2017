import sys
from PyQt5 import QtGui
import pyqtgraph as pg
import numpy as np
import serial
import time, random
import math
from collections import deque  # !!!!

max_entries = 1000
recording_time = 10  # in seconds
recording_period = 0.2  # in seconds

data_volt = deque(maxlen=max_entries)
data_time = deque(maxlen=max_entries)

start = time.time()

global plotting_flag
plotting_flag = True


def main():
    global plotting_flag
    while plotting_flag == True:
        # data = ser.readline().decode().split('\r\n')
        data = np.random.random_integers(1, 1000, size=1)
        data_scale = float(data[0]) * 5.0 / 1024
        current_time = time.time() - start
        print(str(current_time) + ": " + str(data_scale))
        # appending to the data input deques
        data_volt.append(data_scale)
        data_time.append(current_time)
        if (current_time > recording_time):
            plotting_flag = False
        time.sleep(recording_period)



    win = pg.GraphicsWindow()
    p1 = win.addPlot()
    p1.plot(data_time, data_volt, pen=(0, 0, 255))
    p1.setLabel('left', text="Serial value", units="V")
    p1.setLabel('bottom', text="Time", units="sec")
    p1.showGrid(x=True, y=True)

#    ser.close()
    app = QtGui.QApplication(sys.argv)
    status = app.exec_()
    sys.exit(status)


if __name__ == "__main__": main()