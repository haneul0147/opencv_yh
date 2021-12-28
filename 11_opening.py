import cv2

image = cv2.imread('data/images/opening.png')

cv2.imshow('original',image)

openingsize = 3 

element =cv2.getStructuringElement(cv2.MORPH_RECT
                    ,(2*openingsize,2*openingsize))

imageOpened = cv2.morphologyEx(image,cv2.MORPH_OPEN,
                            element,iterations=5)

cv2.imshow('open',imageOpened)

cv2.waitKey(0)
cv2.destroyAllWindows()