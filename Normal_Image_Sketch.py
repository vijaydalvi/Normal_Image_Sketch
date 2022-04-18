import cv2
from cv2 import invert
image=cv2.imread('2.jpg')
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert1=cv2.bitwise_not(gray_img)
blur=cv2.GaussianBlur(invert1,(21,21),0)
in_blur=cv2.bitwise_not(blur)
sketch=cv2.divide(gray_img,in_blur,scale=256.0)
cv2.imwrite('sketch.png')