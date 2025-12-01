#Color Channels

import cv2 as cv
import sys
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

if img is None:
    sys.exit('Couldn\'t find the image')

cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)


b,g,r = cv.split(img)

blue =cv.merge([b, blank, blank])
green =cv.merge([blank, g, blank])
red =cv.merge([blank, blank, r])

cv.imshow('Bleu', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)