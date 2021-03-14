import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

cv.namedWindow('trackbar')
# create trackbars for color change
cv.createTrackbar('R','threshold',127,255,nothing)

while True:

    img = cv.imread('hotspot3.png',0)
    img = cv.medianBlur(img,5)
    dst = cv.equalizeHist(img)

    r = cv.getTrackbarPos('R','threshold')

    ret,th1 = cv.threshold(dst,188,255,cv.THRESH_TOZERO)
    th2 = cv.adaptiveThreshold(dst,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,r,2)
    th3 = cv.adaptiveThreshold(dst,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,r,2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    cv.imshow('th1', th1)
    cv.imshow('th2', th2)
    cv.imshow('th3', th3)

    key = cv.waitKey(1)
    if key == 27: #tombol escape
        break
cv.destroyAllWindows()
'''
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''