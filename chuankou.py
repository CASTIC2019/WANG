import numpy as np
import cv2
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" or "Serial" in p[1]:
        ser=serial.Serial(port=p[0])
    else :
        print ("No Arduino Device was found connected to the computer")
time.sleep(3)
ser.write("y".encode())
