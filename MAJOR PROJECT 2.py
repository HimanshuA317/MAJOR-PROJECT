import cv2
import numpy as np
import pandas as pd
import sys
def show_img():
    cv2.waitKey(3000)
    main()
def main():
    ch = int(input("Enter  choice"))
    if ch==1: #org image
        cv2.imshow("Original image",img)
        show_img()
        
    elif ch==2: #b&w image
        cv2.imshow("B&W image",gray)
        show_img()
        
    elif ch==3:
        ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        cv2.imshow("binary img",binary)
        show_img()
        
    elif ch==4:
        ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        cv2.imshow("binary b&w img",binary)
        show_img()
        
    elif ch==5:
        canny= cv2.Canny(img,90,200)
        cv2.imshow("Sketch",canny)
        show_img()
        
    elif ch==6:
        c=float(input("ENTER RATIO FOR BREADTH"))
        d=float(input("ENTER RATIO FOR LENGTH"))       
        img1=cv2.resize(img,None,fx=c,fy=d)
        cv2.imshow("scaled image",img1)
        show_img()
    elif ch==7:
        name = input('Enter your name:')
        c=int(input("enter  x position"))
        d=int(input("enter  y position"))
        img1=img
        img1 = cv2.putText(img1,name,(c,d),cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0),1)
#SYNTAX - src,name variable,position,font style,font size,font color,font thickness
        cv2.imshow('Text image',img1)
        show_img()
    elif ch==8:
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 9)
        cu=0
        img2=img
        for x,y,w,h in faces:
            img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),5)        
            cu+=1
        cv2.imshow("face detection",img2)
        print("total faces = ",cu)
        show_img()
    elif ch==9:
       cap = cv2.VideoCapture(0)
       while True:
            ret,frame=cap.read()
            cv2.imshow("that's me",frame)
            if cv2.waitKey(1) == 13:
                break
       cap.release()
       main()
    elif ch==10:
        cap = cv2.VideoCapture(0)
        while True:
            ret,frame = cap.read()
            canny = cv2.Canny(frame,20,150)
            cv2.imshow("my live ",canny)
            if cv2.waitKey(1)==13:
                 break
        cap.release()
        main()
    else:
         sys.exit()
         cv2.destroyAllWindows()     
a=input("Enter image address")
img=cv2.imread(a)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("IMAGE READED!")
print(" ENTER .....\n1for desplaying image\n2 for b&w image \n3 for binary image\n4 for binary b&w image \n5 for geeting sketch")
print("6 for  resizing image\n7 for entering text into image\n8 for face deetection\n9 for starting webcam\n10 for getting live sketch  ")
print("11 for exit") 
main()
cv2.destroyAllWindows()












