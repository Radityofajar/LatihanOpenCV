import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    frame = cv.imread('hotspot3.png')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')

    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')

    l_thres = np.array([l_h, l_s, l_v])
    u_thres = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_thres, u_thres)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('result', result)

    key = cv.waitKey(1)
    if key == 27: #tombol escape
        break

cv.destroyAllWindows()