#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
        break
    else :
        print ("No Arduino Device was found connected to the computer")

time.sleep(3)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imgface = cv2.imread('face.jpg')
cap = cv2.VideoCapture(0)
while(True):
    cv2.imwrite('face.jpg',imgface[0:10,0:10])
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.imwrite('face.jpg',img[y:y+h,x:x+w])
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
    cv2.imshow('img',img)
    imgface = cv2.imread('face.jpg')
    (w,h,ctrl)=imgface.shape
    if w*h>40000:
        ser.write("y".encode())
        print('yes!!!!!')
    else:
        ser.write("x".encode())
        print('no!!!!!')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# In[ ]:





# In[ ]:




