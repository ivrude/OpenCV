import cv2
import numpy as np

img = cv2.imread("img/1.jpg")
img = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
new_img = np.zeros(img.shape, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 60, 180)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

new_img = cv2.drawContours(new_img, con, -1, (225,0,0),1)

cv2.imshow("res",new_img)
cv2.waitKey(0)