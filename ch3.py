import cv2
import numpy as np
img = cv2.imread("images/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(1000,500)) # resize
print(imgResize.shape) 
imgCropped = img[0:200,200:500] # cropped

cv2.imshow("Images", img)
cv2.imshow("Images Resize", imgResize) 
cv2.imshow("Images Crop", imgCropped)

cv2.waitKey(0)
