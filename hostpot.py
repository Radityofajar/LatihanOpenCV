import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

#cv.namedWindow('trackbar')
# create trackbars for color change
#cv.createTrackbar('R','threshold',127,255,nothing)

while True:

    img = cv.imread('hotspot6.jpg',0)
    mean, std = cv.meanStdDev(img)
    img = cv.medianBlur(img,5)
    dst = cv.GaussianBlur(img, (5,5), 2)
    thres1 = (mean + 2*std)
    thres2 = (mean + 0.55*std)

    #r = cv.getTrackbarPos('R','threshold')

    ret,th1 = cv.threshold(dst,thres1,255,cv.THRESH_TOZERO)
    ret,th4 = cv.threshold(dst,thres2,255,cv.THRESH_TOZERO)
    th2 = cv.adaptiveThreshold(dst,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY, 155, -1 )
    th3 = cv.adaptiveThreshold(dst,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY, 155 ,0)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    contours, hierarchy = cv.findContours(th1, 1, 2)
    
    cnt1 = contours[0]
    cnt2 = contours[0]
    #print(cnt)
    M1 = cv.moments(cnt1)
    M2 = cv.moments(cnt2)

    cx1 = int(M1['m10']/M1['m00'])
    cy1 = int(M1['m01']/M1['m00'])
    cx2 = int(M2['m10']/M2['m00'])
    cy2 = int(M2['m01']/M2['m00'])
    #print(M)
    area1 = cv.contourArea(cnt1)
    area2 = cv.contourArea(cnt2)
    #print(area)

    Erode1 = cv.erode(th4, cv.getStructuringElement(cv.MORPH_ELLIPSE, (12,12)))
    Dilate = cv.dilate(Erode1, cv.getStructuringElement(cv.MORPH_ELLIPSE, (14,14)))
    Erode2 = cv.erode(Dilate, cv.getStructuringElement(cv.MORPH_ERODE, (5,5)))
    Panel = cv.dilate(Erode2, cv.getStructuringElement(cv.MORPH_RECT, (7,7)))

    contourspanel, hierarchy = cv.findContours(Panel, 1, 2)

    cntp1 = contourspanel[0]
    cntp2 = contourspanel[1]
    #print(cnt)
    M1p = cv.moments(cntp1)
    M2p = cv.moments(cntp2)

    cx1p = int(M1p['m10']/M1p['m00'])
    cy1p = int(M1p['m01']/M1p['m00'])
    cx2p = int(M2p['m10']/M2p['m00'])
    cy2p = int(M2p['m01']/M2p['m00'])
    #print(M)
    area1p = cv.contourArea(cntp1)
    area2p = cv.contourArea(cntp2)

    #bit = cv.bitwise_or(Panel, img)

    result = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

    #citra = cv.rectangle(result,(cx1-25, cy1-25),(cx1+25, cy1+25),(0, 0, 255), 4)
    #citra = cv.circle(citra, (cx1, cy1), 5, (0, 0, 255), -1)
    #citra = cv.putText(citra, "centroid", (cx1 - 25, cy1 - 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    citra = cv.drawContours(result, contours, 0, (0,0,255), 1)
    #citra = cv.rectangle(result,(cx1p-25, cy1p-25),(cx1p+25, cy1p+25),(255, 0, 0), 4)
    citra = cv.circle(citra, (cx1p, cy1p), 5, (255, 0, 0), -1)
    #citra = cv.putText(citra, "centroid", (cx1p - 25, cy1p - 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    citra = cv.drawContours(citra, contourspanel, 0, (255,0,0), 1)

    #final = cv.rectangle(citra,(cx2-25, cy2-25),(cx2+25, cy2+25),(0, 0, 255), 4)
    #final = cv.circle(citra, (cx2, cy2), 5, (0, 0, 255), -1)
    #final = cv.putText(final, "centroid", (cx2 - 25, cy2 - 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    final = cv.drawContours(citra, contours, 0, (0,0,255), 1)
    final = cv.circle(final, (cx2p, cy2p), 5, (255, 0, 0), -1)
    #final = cv.putText(final, "centroid", (cx2p - 25, cy2p - 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    final = cv.drawContours(final, contourspanel, 1, (255,0,0), 1)

    cv.imshow('threshold', th1)
    #cv.imshow('th2', th2)
    #cv.imshow('th3', th3)
    cv.imshow('Ori', img)
    #cv.imshow('th4', th4)
    cv.imshow('Panel', Panel)
    cv.imshow('Final', final)


    key = cv.waitKey(1)
    if key == 27: #tombol escape
        break

print('Area Hot1 = ', area1, ', Area Hot2 = ', area2)
print('Area Panel1 = ', area1p, ', Area Panel2 = ', area2p)
print('cx1, cy1 = ', cx1, ',', cy1)
print('cx2, cy2 = ', cx2, ',', cy2)
print('cx1panel, cy1panel = ', cx1p, ',', cy1p)
print('cx2panel, cy2panel = ', cx2p, ',', cy2p)

Area_Hotspot = area1 + area2
Area_Panel = area1p + area2p
defect = (Area_Hotspot/Area_Panel)*100

print('Defect = ', defect, '%')

cv.destroyAllWindows()
'''
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''
