import cv2
import numpy as np

# Load the image
img = cv2.imread('face.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the contour of the head
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask where white is what we want to keep and black is otherwise
mask = np.zeros_like(img)
cv2.drawContours(mask, contours, 0, 255, -1)

# Extract the object and place it into an output image
out = np.zeros_like(img)
out[mask == 255] = img[mask == 255]

# Crop the image along the contour of the head
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
x, y, w, h = cv2.boundingRect(mask)
out = out[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
