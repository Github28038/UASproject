import cv2

img = cv2.imread('Lenna.png',-1)# read image
cv2.imshow('imgage', img) # image
k= cv2.waitKey(0) # wait for

if k == 27: # After opening the image if we click on (esc key) it will destroy all windows.
    cv2.destroyAllWindows()#destroy all windows
elif k == ord('c'): # After opening the image if we click on ('c' key) it will create a coopy image in the folder.
    cv2.imwrite('lena_copy.png',img)#create a copy
    cv2.destroyAllWindows()