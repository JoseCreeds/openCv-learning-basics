#Essential Functions

import cv2 as cv
import sys

img = cv.imread('Resources/Photos/park.jpg')

if img is None:
    sys.exit('Could not read the image')

cv.imshow('Cat', img)

#Converting to grayScale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding the image
eroded = cv.dilate(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)