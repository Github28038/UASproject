import cv2
import numpy as np

# Load an image
image = cv2.imread('images/10.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for red (lower and upper thresholds)
red_lower = np.array([0, 100, 100])   # Adjust these values based on your desired color range
red_upper = np.array([10, 255, 255])  # Adjust these values based on your desired color range

# Create a binary mask that isolates the red pixels
red_mask = cv2.inRange(hsv, red_lower, red_upper)

# Bitwise-AND the original image and the mask to extract the red regions
red_detected = cv2.bitwise_and(image, image, mask=red_mask)

# Display the original image and the detected red regions
cv2.imshow('Original Image', image)
cv2.imshow('Detected Red', red_detected)

cv2.waitKey(0)
cv2.destroyAllWindows()
