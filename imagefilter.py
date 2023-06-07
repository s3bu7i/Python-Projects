import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply sepia filter
sepia_image = cv2.transform(image, np.array([[0.272, 0.534, 0.131],
                                              [0.349, 0.686, 0.168],
                                              [0.393, 0.769, 0.189]]))

# Apply negative filter
negative_image = cv2.bitwise_not(image)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Filter', gray_image)
cv2.imshow('Sepia Filter', sepia_image)
cv2.imshow('Negative Filter', negative_image)

# Wait for key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
