import cv2
import numpy as np
photo = cv2.imread("img/1.jpg")
photo = cv2.resize(photo,(photo.shape[1]*2,photo.shape[0]*2))
print(photo.shape)
img = np.zeros((photo.shape[0], photo.shape[1]), dtype="uint8")
circle = cv2.circle(img.copy(), (175,175),50, (255,100,10), -1)
square = cv2.rectangle(img.copy(), (100,100),(200,200),(200,1,122), -1)
print(circle.shape)
img = cv2.bitwise_and(photo, photo, mask=circle)
cv2.imshow("res", img)
cv2.waitKey(0)