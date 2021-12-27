import cv2
import numpy as np 

# cv2.IMREAD_COLOR  == 1   같은 의미
source = cv2.imread('data/images/sample.jpg',1)

print(cv2.IMREAD_COLOR)

#가로는 80%로
#세로는 60%로
# 이미지 확대 / 축소

scaleX= 0.8
scaleY= 0.6

scaleDown=cv2.resize(source,None,fx=scaleX,fy=scaleY,interpolation=cv2.INTER_LINEAR)
print(scaleDown)
cv2.imshow('Scaled Down',scaleDown)
cv2.imshow('Original',source)


# CROP 이미지 자르기!!\
crop_img=source[350:500,200:550]
cv2.imshow('crop img',crop_img)


cv2.waitKey(0)                      #프로그램  wait
cv2.destroyAllWindows()                   #모든창을 없애라

