# check this program if work then Enjoy , this will probably work on all  high end games(Direct X games)

import serial
import time
from directkey  import PressKey, ReleaseKey, W, A, S, D

ser = serial.Serial('COM14', baudrate=9600,  timeout=1)   # change COM3 to your port in which arduino is connected
while True:
    portdata = ser.readline().decode('ascii')           # read the data comming  from arduino
    if len(portdata) == 0:
        print("no data comming........",  end = "\
")    # port is connected but no data is avaliable on serial port
        ser.flushInput()
    if len(portdata) != 0:                              #  if data is avaliable on the serial port
        if portdata[0] == 'w':
            PressKey(W)
            time.sleep(0.2)
            ReleaseKey(W)
            ser.flushInput()
        elif portdata[0]  == 's':
            PressKey(S)
            time.sleep(0.2)
            ReleaseKey(S)
            ser.flushInput()
        elif portdata[0] == 'a':
            PressKey(A)
            time.sleep(0.2)
            ReleaseKey(A)
            ser.flushInput()
        elif portdata[0] == 'd':
            PressKey(D)
            time.sleep(0.2)
            ReleaseKey(D)
            ser.flushInput()
