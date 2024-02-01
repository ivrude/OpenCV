import cv2
import numpy as np

img = cv2.imread('img/1.jpg')
new_img = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
rozmitoe = cv2.GaussianBlur(new_img, (5,5), 5)
black = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
binare = cv2.Canny(black, 150, 150)

cv2.imshow('res', binare)
print(img.shape)
cv2.waitKey(0)
#cap = cv2.VideoCapture(0)
#cap.set(3, 500)
#cap.set(4,300)
#while True:
#    success, img = cap.read()
#    cv2.imshow('res',img)
#
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
