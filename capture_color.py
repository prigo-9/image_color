import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    frame= cv2.imread('index.jpg')
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_green=np.array([50,100,100])
    upper_green=np.array([70,255,255])
    lower_r=np.array([0,100,100])
    upper_r=np.array([20,255,255])

    # Threshold the HSV image to get only blue colors
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_g=cv2.inRange(hsv,lower_green,upper_green)
    mask_r=cv2.inRange(hsv,lower_r,upper_r)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_or(mask_b,mask_g, mask= None)
    res2=cv2.bitwise_or(res,mask_r,mask=None)
    res_r =cv2.bitwise_and(frame,frame,mask=res2)
   

    cv2.imshow('frame',frame)
    cv2.imshow('mask_b',mask_b)
    cv2.imshow('mask_g',mask_g)
   # cv2.imshow('res',res)
    cv2.imshow('res_r',res_r)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
