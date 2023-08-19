import cv2
import numpy as np
img = cv2.imread('images/lenna.png')

imghor = np.hstack((img,img)) # horizontal stacking
imgver = np.vstack((img,img)) # vertical stacking

cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgver)

cv2.waitKey(0)