import cv2
import numpy as np 

img = np.zeros((512,512,3),np.uint8) # defining the size of image
# print(img)
# img[:] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # line in the image
cv2.rectangle(img,(0,0,),(250,350),(0,0,255),2) # rectangle in the image
cv2.circle(img,(400,50),30,(255,255,0),5) # circle in the image
cv2.putText(img,"Opencv",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,150),2)
# puting text in the image

cv2.imshow("Image",img)

cv2.waitKey(0)