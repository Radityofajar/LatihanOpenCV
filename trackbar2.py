import numpy as np
import cv2 as cv

#initialise variables with a default
nlm_thresh = 5
bino_thresh = 5
canny_thresh = 5
# functions that update a variable, 
# then call image processing function
def change_nlm(val):
    global nlm_thresh
    nlm_thresh = val
    thresh_callback()

def change_bino(val):
    global bino_thresh
    bino_thresh = val
    thresh_callback()

def change_canny(val):
    global canny_thresh
    canny_thresh = val
    thresh_callback()

# your function that processes the image
def thresh_callback():
    img = cv.imread('hotspot3.png')
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    nlm = cv.fastNlMeansDenoising(imgray,nlm_thresh,nlm_thresh,11,21)
    bino = cv.adaptiveThreshold(nlm,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,bino_thresh,8)
    canny_output = cv.Canny(bino, canny_thresh, canny_thresh * 2)
    contours, hierarchy = cv.findContours(canny_output,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cnt = sorted(contours, key=cv.contourArea, reverse=True)
    cnts = cnt[0]
    area = cv.contourArea(cnts)
    print (area)

    drawing = cv.drawContours(img, cnt, 0, (0,255,0), 3)

    cv.imshow('Contours2', canny_output)
    cv.imshow(source_window, drawing)


source_window = 'Source'
cv.namedWindow(source_window)
max_thresh = 1000
thresh = 5
# create trackbars
cv.createTrackbar('nlm_thresh:', source_window, thresh, max_thresh, change_nlm)
cv.createTrackbar('bino_thresh:', source_window, thresh, max_thresh, change_bino)
cv.createTrackbar('canny_thresh:', source_window, thresh, max_thresh, change_canny)

thresh_callback()

cv.waitKey(0) & 0xFF  
cv.destroyAllWindows()