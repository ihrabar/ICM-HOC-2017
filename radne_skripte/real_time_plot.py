import sys 
from PyQt5 import QtGui 
import pyqtgraph as pg
import numpy as np
import serial
import time, random
import math
from collections import deque  #!!!! 

recording_time=20 # in seconds
recording_period=0.2 # in seconds
screen_time=10 # in seconds
plot_data_nr=int(screen_time/recording_period)

data_volt=[]
data_time=[]
plot_time=[]
plot_data=[]

# moved here to beginning
app = QtGui.QApplication(sys.argv)
win = pg.GraphicsWindow(title="Plotting examples")
p = win.addPlot(title="Serial input plot")
#curve = p.plot() 
p.setLabel( 'left', text="Serial value", units="V")
p.setLabel( 'bottom', text="Time", units="sec")
p.showGrid(x=True, y=True)

# check the Arduino IDE to see what serial port it's attached to
ser = serial.Serial("COM34", 115200) #'/dev/ttyACM0'
print("connected to: " + ser.portstr)
# flush any junk left in the serial buffer
ser.reset_input_buffer()

start = time.time()

global plotting_flag
plotting_flag=True

def main():
	global plotting_flag

	while plotting_flag==True:
		#data = ser.readline().decode().split('\r\n') 
		data=np.random.random_integers(1,1000,size=1)
		data_scale=float(data[0])*5.0/1024 
		current_time=time.time()-start
	
		data_volt.append(data_scale)
		data_time.append(current_time)

		p.clear()
		p.plot(data_time, data_volt, pen=(0,0,255))
		#plot_data=data_volt[-plot_data_nr:]
		#plot_time=data_time[-plot_data_nr:]
		#p.plot(plot_time, plot_data, pen=(0,0,255))
		app.processEvents()

		if (current_time>recording_time):
			plotting_flag=False
		time.sleep(recording_period)

	ser.close()
	status = app.exec_()
	sys.exit(status)
		

if __name__ == "__main__": main()
