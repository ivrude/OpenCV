import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8')

#photo[140:160, 80:100] = 105, 205, 119
cv2.rectangle(photo, (100, 100), (200,200), (105, 205, 119))
cv2.line(photo,(0,photo.shape[0]//2),(100,photo.shape[0]//2),(105, 205, 119))
cv2.circle(photo, (photo.shape[1]//2,photo.shape[0]//2),50, (105, 205, 119))
cv2.putText(photo,"Result", (10,15),cv2.FONT_HERSHEY_PLAIN, 1, (147, 205, 119))
cv2.imshow("res",photo)
cv2.waitKey(0)
