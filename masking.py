#Masking

import cv2 as cv
import sys
import numpy as np

img = cv.imread('Resources/Photos/cats 2.jpg')

if img is None:
    sys.exit('Couldn\'t find the image')

cv.imshow('Cat', img)

# blank = np.zeros((300,300), dtype='uint8')
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked',masked)




cv.waitKey(0)