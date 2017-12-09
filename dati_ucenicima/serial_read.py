import serial

ser = serial.Serial("COM38", 115200) 
print("connected to: " + ser.portstr)

# flush any junk left in the serial buffer
ser.flushInput()
ser.reset_input_buffer()
while True:
	data = ser.readline().decode().split('\r\n')
	print(data[0])


ser.close()

