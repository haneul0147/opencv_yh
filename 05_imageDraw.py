import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img',image)

#선그리기 
imageLine =image.copy()
cv2.line(imageLine,(322,179),(400,183),(255,0,0),3,cv2.LINE_AA)
# (350,200) -> 시작 점          (400,183) -> 끝점
# (0,0,255) -> 색상(BGR)   3-> 두께
cv2.imshow('imageLine',imageLine)

# 원그리기 
imageCircle=image.copy()
cv2.circle(imageCircle,(350,200),150,(255,0,0),3,cv2.LINE_AA)
#(350,200)-> 중심원    150->  반지름
# (255,0,0) -> 색       3 -> 두께
cv2.imshow('imagerCircle',imageCircle)

#타원 그리기
imageEllipse = image.copy()
cv2.ellipse(imageEllipse,(360,200),(100,170),45,0,360,(0,255,0),2)
cv2.ellipse(imageEllipse,(360,200),(100,170),153,0,360,(0,0,255),thickness=2)
cv2.imshow('ellipse',imageEllipse)

# 사각형 그리기 
imageRectangle = image.copy()
cv2.rectangle(imageRectangle,(208,55),(450,355),(250,0,0),3)
cv2.imshow('Rectangle',imageRectangle)

# 글자 넣기
imageText = image.copy()
cv2.putText(imageText,'Mark Zuckerberg',(205,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow('Text',imageText)


cv2.waitKey(0)
cv2.destroyAllWindows()
