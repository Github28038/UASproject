import cv2
import numpy as np

def color_change(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define color ranges for brown and green
    brown_lower = np.array([10, 50, 50])
    brown_upper = np.array([30, 255, 255])
    
    green_lower = np.array([35, 50, 50])
    green_upper = np.array([85, 255, 255])
    
    # Create masks for brown and green portions
    brown_mask = cv2.inRange(hsv, brown_lower, brown_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    
    # Change brown to yellow and green to blue
    image[brown_mask > 0] = [0, 255, 255]  # Yellow (BGR format)
    image[green_mask > 0] = [230,216,173]   # light Blue (BGR format)
    
    return image

# Load an image
input_image = cv2.imread('images/10.png')
image = cv2.imread('images/10.png')
# Apply color changes
output_image = color_change(image)

# Display the original and modified images
cv2.imshow('Original Image', input_image)
cv2.imshow('Modified Image', output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# I have bean able to complete till here .