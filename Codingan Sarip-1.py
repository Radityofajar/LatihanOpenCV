import cv2 as cv
import numpy as np
import sys

kernalClose = np.ones((5,5),"uint8")
kernalOpen = np.ones((7,7),"uint8")

def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)

img = cv.imread("DJI_0602.JPG")

kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
kernelC = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
KernelD = cv.getStructuringElement(cv.MORPH_RECT,(10,10))

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize (frame, dimensions, interpolation=cv.INTER_AREA)

gambar = rescaleFrame(img)

blur = cv.GaussianBlur(gambar,(7,7), 2)

#b,g,r = cv.split(gambar) 
b,g,r = cv.split(blur)

cv.imshow("Blue", b)
cv.imshow("Red", r)

ret, thresh = cv.threshold(b, 125, 255, cv.THRESH_BINARY)
ret1, thresh1 = cv.threshold(r, 125, 255, cv.THRESH_BINARY)
show_wait_destroy("Thresh", thresh)
show_wait_destroy("Thresh1", thresh1)
#cv.imshow("Threhs", thresh)
#cv.imshow("Thresh1", thresh1)


bitwise_xor = cv.bitwise_xor(thresh1, thresh)
#cv.imshow("bitwise_xor", bitwise_xor)

bitwise_xor1 = cv.bitwise_and(thresh, bitwise_xor)
#cv.imshow("bitwise_xor1", bitwise_xor1) 

opening = cv.morphologyEx(bitwise_xor1, cv.MORPH_OPEN, kernel)
#cv.imshow("Opening",opening)


if len(opening.shape) != 2:
        gray = cv.cvtColor(opening, cv.COLOR_BGR2GRAY)
else:
        gray = opening
    # Show gray image
show_wait_destroy("gray", gray)


close = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernelC)
open = cv.morphologyEx(close, cv.MORPH_OPEN, kernelC)
dilate = cv.dilate(open, KernelD , iterations= 6)
erode = cv.erode(dilate, KernelD, iterations = 4)

#open1 = cv.morphologyEx(close1, cv.MORPH_OPEN, kernelC)


show_wait_destroy("Close", close)
show_wait_destroy("open", open)
show_wait_destroy("dilate", dilate)
show_wait_destroy("erode", erode)

masking = cv.bitwise_and(gambar, gambar, mask = erode)
show_wait_destroy("Mask", masking)

blur2 = cv.GaussianBlur(masking,(7,7), 2)

b1,g1,r1 = cv.split(blur2)

cv.imshow("Blue", b1)
cv.imshow("Red", r1)

ret2, thresh2 = cv.threshold(b1, 100, 255, cv.THRESH_BINARY)
ret3, thresh3 = cv.threshold(r1, 140 , 255, cv.THRESH_BINARY)
show_wait_destroy("Thresh2", thresh2)
show_wait_destroy("Thresh3", thresh3)
#cv.imshow("Threhs", thresh)
#cv.imshow("Thresh1", thresh1)


bitwise_xor2 = cv.bitwise_xor(thresh2, thresh3)
#cv.imshow("bitwise_xor2", bitwise_xor2)
show_wait_destroy("Bitwise_Xor2",bitwise_xor2)

bitwise_xor3 = cv.bitwise_and(thresh2, bitwise_xor2)
#cv.imshow("bitwise_xor3", bitwise_xor3) 
show_wait_destroy("Bitwise_Xor3", bitwise_xor3)

opening1 = cv.morphologyEx(bitwise_xor3, cv.MORPH_OPEN, kernel)
#cv.imshow("Opening1",opening)
show_wait_destroy("opening1", opening1)


if len(opening1.shape) != 2:
        gray2 = cv.cvtColor(opening1, cv.COLOR_BGR2GRAY)
else:
        gray2 = opening1
    # Show gray image
show_wait_destroy("gray2", gray2)

    # [gray]
    # [bin]
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
gray = cv.bitwise_not(gray)
bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    # Show binary image
#show_wait_destroy("binary", bw)
    # [bin]

    # Create the images that will use to extract the horizontal and vertical lines
horizontal = np.copy(bw)
vertical = np.copy(bw)
    # [init]
    # [horiz]
    # Specify size on horizontal axis
cols = horizontal.shape[1]
horizontal_size = cols // 30
    # Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
    # Apply morphology operations
horizontal = cv.erode(horizontal, horizontalStructure)
horizontal = cv.dilate(horizontal, horizontalStructure)
    # Show extracted horizontal lines
#show_wait_destroy("horizontal", horizontal)

rows = vertical.shape[0]
verticalsize = rows // 30
    # Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
vertical = cv.erode(vertical, verticalStructure)
vertical = cv.dilate(vertical, verticalStructure)
    # Show extracted vertical lines
#show_wait_destroy("vertical", vertical)

 # Inverse vertical image
vertical = cv.bitwise_not(vertical)
#show_wait_destroy("vertical_bit", vertical)

    #step1
edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
#show_wait_destroy("edges", edges)
    # Step 2
kernel = np.ones((2, 2), np.uint8)
edges = cv.dilate(edges, kernel)
#show_wait_destroy("dilate", edges)
    # Step 3
smooth = np.copy(vertical)
    # Step 4
smooth = cv.blur(smooth, (2, 2))
    # Step 5
(rows, cols) = np.where(edges != 0)
vertical[rows, cols] = smooth[rows, cols]
    # Show final result
#show_wait_destroy("smooth - final", vertical)
    # [smooth]

     #step1
edges2 = cv.adaptiveThreshold(horizontal, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
#show_wait_destroy("edges2", edges2)
    # Step 2
kernel = np.ones((2, 2), np.uint8)
edges = cv.dilate(edges, kernel)
#show_wait_destroy("dilate", edges2)
    # Step 3
smooth = np.copy(horizontal)
    # Step 4
smooth = cv.blur(smooth, (2, 2))
    # Step 5
(rows, cols) = np.where(edges != 0)
horizontal[rows, cols] = smooth[rows, cols]
    # Show final result
#show_wait_destroy("smooth - final", horizontal)
    # [smooth]

notVertical = cv.bitwise_not(horizontal)
panel = cv.bitwise_and(notVertical, vertical)
show_wait_destroy("Panel", panel)     

panel2 = cv.bitwise_not(panel)
show_wait_destroy("Panel2", panel2)  


lines = cv.HoughLinesP(gray,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(blur,(x1,y1),(x2,y2),(0,0,255),2)
show_wait_destroy('houghlines5.jpg',blur)

gray2 = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
show_wait_destroy("gray2", gray2)

ret2, thresh2 = cv.threshold(gray2,  80, 255, cv.THRESH_BINARY)
show_wait_destroy("Threshold", thresh2)

and2 = cv.bitwise_and(panel2, thresh2)
show_wait_destroy("testing", and2)

open_ = cv.morphologyEx(and2, cv.MORPH_OPEN,kernalOpen) 
dilation = cv.dilate(open_,kernalClose,iterations = 2 )
erosion = cv.erode(dilation,kernalClose,iterations = 1)

show_wait_destroy("Open", open_)
show_wait_destroy("Final", erosion) 

contours2, hierarchy = cv.findContours(erosion, 1, 2)

result = cv.drawContours(gambar, contours2 , 0, (0,0,255), 2)
show_wait_destroy("Gambar akhir", gambar)