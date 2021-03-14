import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar('Thresh', 'Tracking', 215, 255, nothing)

while True:

    img = cv.imread('hotspot2.jpg', 0)

    r = cv.getTrackbarPos('Thresh', 'Tracking')

    print(r)

    _, th1 = cv.threshold(img, r, 255, cv.THRESH_BINARY)
    _, th2 = cv.threshold(img, r, 255, cv.THRESH_BINARY_INV)
    _, th3 = cv.threshold(img, r, 255, cv.THRESH_TRUNC)
    _, th4 = cv.threshold(img, r, 255, cv.THRESH_TOZERO)
    _, th5 = cv.threshold(img, r, 255, cv.THRESH_TRIANGLE)

    mask = cv.inRange(img,20, 215)

    cv.imshow('Gambar', img)
    cv.imshow('th1', th1)
    cv.imshow('th2', th2)
    cv.imshow('th3', th3)
    cv.imshow('th4', th4)
    cv.imshow('th5', th5)
    cv.imshow('mask', mask)

    key = cv.waitKey(1)
    if key == 27: #tombol escape
        break


cv.destroyAllWindows()