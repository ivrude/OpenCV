import cv2
import numpy as np

photo = cv2.VideoCapture(0)
photo.set(3, 500)
photo.set(4,300)
while True:
    success, video = photo.read()
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    res = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)

    for (x, y, w, h) in res:
        cv2.rectangle(video, (x, y), (x+w, y+h), (0,0,255), thickness=3)
    cv2.imshow("res", video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
