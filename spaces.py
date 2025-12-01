#Color Spaces

import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Resources/Photos/park.jpg')

if img is None:
    sys.exit('Couldn\'t find the image')

cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)