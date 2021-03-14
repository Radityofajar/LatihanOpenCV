import numpy as np
import cv2 as cv

img = cv.imread('opencv/samples/data/lena.jpg', 1)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        
        mycolorImage = np.zeros((512,512,3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv.imshow("Warna", mycolorImage)
        print('blue:' + str(blue) + ', ' + 
           'green:' + str(green) + ', ' + 
           'red:' + str(red))

cv.imshow('Gambar', img)
points = []
cv.setMouseCallback('Gambar', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
