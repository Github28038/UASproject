import cv2
import numpy as np

img = cv2.imread("images/cards.jpg")

width, height = 250,350

pts1 = np.float32([[89,206],[236,179],[291,386],[123,416]]) # tracing a object in image using its coordinates
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgoutput)

cv2.waitKey(0)