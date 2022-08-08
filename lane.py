import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
# avoid modification to original image
lane_image = np.copy(image)
# convert to grayscale (3 channel -> 1 channel)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
# reduce noise with Gaussian filter (avoid false edge)
blur = cv2.GaussianBlur(gray, (5,5), 0)
# compute gradient to detect edges
canny = cv2.Canny(blur, 50, 150)

cv2.imshow('result', canny)
cv2.waitKey(0)
