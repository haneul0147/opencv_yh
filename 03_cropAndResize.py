import cv2
import numpy as np 

# cv2.IMREAD_COLOR  == 1   같은 의미
source = cv2.imshow('data/images/sample.jpg',1)

print(cv2.IMREAD_COLOR)

#가로는 80%로
#세로는 60%로
# 이미지 확대 / 축소

scaleX= 0.8
scaley= 0.6

cv2.resize(source)