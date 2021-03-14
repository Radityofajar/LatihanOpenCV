import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv.imshow('Gambar', img)

img = np.zeros((512, 512,3), np.uint8)

cv.imshow('Gambar', img)
points = []
cv.setMouseCallback('Gambar', click_event)

cv.waitKey(0)
cv.destroyAllWindows()