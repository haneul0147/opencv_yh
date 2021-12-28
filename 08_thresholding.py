import cv2
import numpy as np

image =cv2.imread('data/images/truth.png')

#구분 값을 먼저 설정
thresh =120
#위에 특정 값보다 큰 값들은 모두 255 변경
maxvalue= 255

cv2.imshow('original',image)

# 쓰레숄딩 적용된 이미지 만들기
th,dst = cv2.threshold(image,thresh,maxvalue,cv2.THRESH_BINARY)

cv2.imshow('thresholded image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()