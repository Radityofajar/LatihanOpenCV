import cv2 as cv
import numpy as np

l_h = 60
l_s = 0
l_v = 0
u_h = 164
u_s = 190
u_v = 255
l_h2 = 14
l_s2 = 0
l_v2 = 96
u_h2 = 60
u_s2 = 119
u_v2 = 238

citra = cv.imread("FLIR.jpg", -1)

blur = cv.GaussianBlur(citra, (5,5), 2)

hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

l_thres = np.array([l_h, l_s, l_v])
u_thres = np.array([u_h, u_s, u_v])

mask = cv.inRange(hsv, l_thres, u_thres)

kernal = np.ones((2,2),"uint8")

panel = cv.morphologyEx(mask,cv.MORPH_ELLIPSE,kernal)
panel = cv.erode(panel,cv.getStructuringElement(cv.MORPH_ELLIPSE, (8,8)))
panel = cv.dilate(panel,cv.getStructuringElement(cv.MORPH_RECT, (8,8)))
panel = cv.dilate(panel,cv.getStructuringElement(cv.MORPH_RECT, (9,9)))
panel = cv.erode(panel,cv.getStructuringElement(cv.MORPH_ERODE, (7,7)))

result = cv.bitwise_and(citra, citra, mask=panel)

contours, hierarchy = cv.findContours(panel, 1, 2)

cnt = contours[0]

modul = cv.drawContours(result, contours, 0, (255,0,0), 3)

citra2 = cv.cvtColor(result, cv.COLOR_BGR2HSV)

l_thres2 = np.array([l_h2, l_s2, l_v2])
u_thres2 = np.array([u_h2, u_s2, u_v2])

mask2 = cv.inRange(citra2, l_thres2, u_thres2)

soil = cv.morphologyEx(mask2,cv.MORPH_ELLIPSE,kernal)
soil = cv.erode(soil,cv.getStructuringElement(cv.MORPH_ELLIPSE, (8,8)))
soil = cv.dilate(soil,cv.getStructuringElement(cv.MORPH_RECT, (14,14)))
soil = cv.dilate(soil,cv.getStructuringElement(cv.MORPH_RECT, (14,14)))
soil = cv.erode(soil,cv.getStructuringElement(cv.MORPH_ERODE, (3,3)))

#result2 = cv.bitwise_or(result, modul, mask=soil)

contours2, hierarchy = cv.findContours(soil, 1, 2)

cnt1 = contours2[0]

result2 = cv.drawContours(modul, contours2, 0, (0,0,255), 2)

cv.imshow("source", citra)
cv.imshow("mask panel", mask)
cv.imshow("mask soil", mask2)
cv.imshow("soil", soil)
cv.imshow("panel", panel)
cv.imshow("result", result2)

cv.waitKey(0)
cv.destroyAllWindows()