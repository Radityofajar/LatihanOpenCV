import cv2 as cv
import numpy as np 

img = cv.imread('opencv/samples/data/messi5.jpg')
img2 = cv.imread('opencv-logo.png')


print('Shape: ' ,img.shape)
print('Size: ' ,img.size)
print('dtype: ' ,img.dtype)

print('Shape: ' ,img2.shape)
print('Size: ' ,img2.size)
print('dtype: ' ,img2.dtype)

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

#bola = img[280:340, 330:390] #[x1:y1, x2:y2] koordinat u/persegi
#img[273:333, 100:160] = bola
#img = bola

img = cv.resize(img, (300, 300))
img2 = cv.resize(img2, (300,300))

img3 = cv.add(img, img2)
img4 = cv.addWeighted(img, 0.5, img2, 0.5, 0)

cv.imshow('Gambar', img3)
#cv.imshow('Gambar', img4)


cv.waitKey(0)
cv.destroyAllWindows()