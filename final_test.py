import pip
import numpy as np
import cv2
import numpy as np
from time import time, sleep
from datetime import datetime, timedelta
from random import seed,randint
seed(4713983)

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
starttime=time()
stoptime=time()
na=[]
flag=1

#a=0
#b=0
def addnmbr():
    
    a=randint(20,100)
    b=randint(20,100)
    print("enter ",a ,'+',b)
    inp=int(input())
    if inp==a+b:
        print("okie!!!")
    else:
        addnmbr()
        
#====================================== Infinite loop to capture imG===================================
while(cap.isOpened()):
    # check !
    # capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1,0)

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        #nowtime=time()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1)
     #   Draw rectangle around faces
     
       
        for (x, y, w, h) in faces:
            #for m in range(80):
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2,5)
            p=cv2.circle(frame,(x+w//2,y+h//2+10),100,(0, 0, 0))
            cv2.imshow('frame',frame)
            if p.any:
                flag=0
                na.append(0)
                nowtime=time()
            else :
                flag=1
                na.append(1)
                stoptime=time()
                #cv2.circle(frame,(x+w//2,y+h//2+10),m,(0, 0, 0))
            cv2.imshow('frame',frame)
       
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done release the capture
cap.release()
cv2.destroyAllWindows()

print(na)

