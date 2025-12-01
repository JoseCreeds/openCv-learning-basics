#Reading Images and video

import cv2 as cv
import sys

# & D:/Projects/openCV/.venv/Scripts/Activate.ps1 → pour activer venv


# img = cv.imread('Resources/Photos/cat_large.jpg')

# if img is None:
#     sys.exit("Could not read the image.")
# cv.imshow('Cat', img)
# cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()