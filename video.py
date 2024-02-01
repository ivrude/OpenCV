import cv2
import numpy as np

cap = cv2.VideoCapture("video/IMG_1847.MOV")
cap.set(3, 500)
cap.set(4,300)
while True:
    success, img = cap.read()
    black = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binare = cv2.Canny(black, 30, 30)

    cv2.imshow('res', binare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break