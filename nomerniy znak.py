import cv2
import numpy as np
import imutils
import easyocr
def rotate(img,degree):
    height,width=img.shape[:2]
    point = (width//2, height//2)
    mat = cv2.getRotationMatrix2D(point,degree,1)
    return cv2.warpAffine(img,mat,(width,height))
img = cv2.imread("img/3.jpg")
img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
#img=rotate(img,-9)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filter = cv2.bilateralFilter(gray, 19, 20, 28)
znak = cv2.CascadeClassifier('plate.xml')

res = znak.detectMultiScale(filter, scaleFactor=1.5, minNeighbors=3)
ovn_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
print(res)
for (x, y, w, h) in res:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), thickness=3)
    mask = cv2.rectangle(ovn_img.copy(), (x, y), (x+w, y+h), (200, 1, 122), -1)


new_res = cv2.bitwise_and(img, img, mask=mask) #find only nomerniy znak
print(new_res.shape)
cropp = new_res[y:y+h,x:x+w] #copp new photo with mask ans live only nomerniy znak

text = easyocr.Reader(['en'])
text = text.readtext(cropp)
res = text[0][-2] #get text from nomerniy znak
label = cv2.putText(img, res, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0),1)
cv2.imshow("result", label)
cv2.waitKey(0)