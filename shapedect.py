import cv2

# Load an image
image = cv2.imread('images/shapes.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize arrays to store different shape types
triangles = []
rectangles = []

# Filter contours based on the number of vertices
for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    num_vertices = len(approx)

    if num_vertices == 3:
        triangles.append(approx)
    elif num_vertices == 4:
        rectangles.append(approx)

# Draw the detected shapes on the original image
for triangle in triangles:
    cv2.drawContours(image, [triangle], -1, (0, 255, 0), 2)  # Green for triangles

for rectangle in rectangles:
    cv2.drawContours(image, [rectangle], -1, (0, 0, 255), 2)  # Red for rectangles

# Display the image with detected shapes
cv2.imshow('Detected Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
