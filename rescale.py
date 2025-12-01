#Resizing and Rescaling

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Image, Video and Live video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

# Reading image
image = cv.imread('Resources/Photos/cat.jpg')

image_resized = rescaleFrame(image, scale=.2) 


cv.imshow('Image', image)
cv.imshow('Image Resized', image_resized)

# Reading video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2) 

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()