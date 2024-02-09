import cv2
import numpy as np

img = cv2.imread("img/2.jpg")
img = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
#img = cv2.flip(img,1)
def rotate(img,degree):
    height,width=img.shape[:2]
    point = (width//2, height//2)
    mat = cv2.getRotationMatrix2D(point,degree,1)
    return cv2.warpAffine(img,mat,(width,height))

def transform(img,x,y):
    mat = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img,mat,(img.shape[1],img.shape[0]))

img=rotate(img,-9)
img = cv2.imshow("res",img)
cv2.waitKey(0)