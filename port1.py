# this is port1.py, first python program if this doesn't work on your  game then use port2.py

import time
import pyautogui as pg
import serial

print("i  wil give input after 5s so")
for i in range(5):
    print(i, end = "\
")
    time.sleep(1)
ser = serial.Serial('COM14', baudrate=9600, timeout=1)   # change  COM3 to your port in which arduino is connected
while True:
    portdata =  ser.readline().decode('ascii')           # read the data comming from arduino
    if len(portdata) == 0:
        print("no data comming........", end = "\
")    # port is connected but no data is avaliable on serial port
        ser.flushInput()
    if len(portdata) != 0:                              # if data is avaliable on  the serial port
        if portdata[0] == 'w':
            pg.keyDown('w')
            time.sleep(0.1)
            pg.keyUp('w')
            ser.flushInput()
        elif portdata[0]  == 's':
            pg.keyDown('s')
            time.sleep(0.1)
            pg.keyUp('s')
            ser.flushInput()
        elif portdata[0] == 'a':
            pg.keyDown('a')
            time.sleep(0.1)
            pg.keyUp('a')
            ser.flushInput()
        elif portdata[0] == 'd':
            pg.keyDown('d')
            time.sleep(0.2)
            pg.keyUp('d')
            ser.flushInput()
