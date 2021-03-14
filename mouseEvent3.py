import numpy as np
import cv2 as cv

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.imread('opencv/samples/data/lena.jpg', 1)
#img = np.zeros((512,512,3), np.uint8)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        strXY = str(x) + ', ' + str(y)
        cv.putText(img, strXY, (x,y), font, .5, (255, 0, 0), 2)
        cv.imshow('Gambar', img)

    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 0]
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red) 
        cv.putText(img, strBGR, (x,y), font, .5, (0, 255, 0), 2)
        cv.imshow('Gambar', img)


cv.imshow('Gambar', img)

cv.setMouseCallback('Gambar', click_event)

cv.waitKey(0)
cv.destroyAllWindows()