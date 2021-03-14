import numpy as np
import cv2 as cv

imgx = np.zeros((250, 500, 3), np.uint8)
imgy = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(imgx, (200,0), (300,100), (255, 255, 255), -1)
img2 = cv.rectangle(imgy, (0, 0), (250, 250), (255,255,255), -1)

bitAnd = cv.bitwise_and(img2, img1)
bitOr = cv.bitwise_or(img2, img1)
bitXor = cv.bitwise_xor(img2, img1)
bitNot1 = cv.bitwise_not(img1)
bitNot2 = cv.bitwise_not(img2)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('bitAnd', bitAnd)
#cv.imshow('bitOr', bitOr)
#cv.imshow('bitXor', bitXor)
#cv.imshow('bitNot1', bitNot1)
#cv.imshow('bitNot2', bitNot2)

cv.waitKey(0)
cv.destroyAllWindows()