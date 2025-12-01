#Blurring techniques

import cv2 as cv
import sys
import numpy as np

# https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
#Il s'agit de flouter...

img = cv.imread('Resources/Photos/cats.jpg')

if img is None:
    sys.exit('Couldn\'t find the image')

cv.imshow('Cat', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img,5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)