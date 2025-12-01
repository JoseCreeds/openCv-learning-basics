#Thresholding/Binarizing Imagesg

import cv2 as cv
import sys
import numpy as np

img = cv.imread ('Resources/Photos/cats.jpg')

if img is None:
    sys.exit('Could\'n find image')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
#si pixel > seuil → blanc, sinon noir
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) 
cv.imshow('Simple thresholded', thresh)

#inverse : blanc devient noir et vice-versa
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) 
cv.imshow('Simple thresholded Inverse', thresh_inv)

#Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)