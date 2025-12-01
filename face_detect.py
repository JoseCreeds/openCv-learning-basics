#Edge detection

import cv2 as cv
import sys
import numpy as np

img = cv.imread('Resources/Photos/group 1.jpg')

if img is None:
    sys.exit('Couldn\'t find the image')

cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

#passer le classifier à utiliser
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

#Print number of faces found by faces_rect
print(f'Number of faces found: {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)

cv.waitKey(0)