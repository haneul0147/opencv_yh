import cv2
import numpy as np

image = cv2.imread('data/images/truth.png')

cv2.imshow('original',image)

# 이미지 침식 : erode

erodesize=6

element =cv2.getStructuringElement(cv2.MORPH_RECT,
                (2*erodesize , 2*erodesize))

imageErode=cv2.erode(image,element)

cv2.imshow('erode',imageErode)

cv2.waitKey(0)
cv2.destroyAllWindows()
