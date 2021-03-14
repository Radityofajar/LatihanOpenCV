import cv2 as cv
import numpy as np

citra = cv.imread('opencv/samples/data/opencv-logo.png', 1)
#citra = np.random.randint(0, 256, size=(512, 512, 3), dtype=np.uint8)
#citra = np.zeros([512, 512, 3], dtype=np.uint8)

#dimensi dari gambar -> panjang, lebar, jumlah channel warna (512,512,3)
dimensi = citra.shape
height = citra.shape[0]
width = citra.shape[1]
channels = citra.shape[2]

print("dimensi:", dimensi)
print('height', height)
print('width', width)

#x1,y1----------
#|             |
#|             |
#|             |
#|---------x2,y2             

#garis --- (gambar, titik awal/x1,y1 , titik akhir/x2,y2 , warna, ketebalan)
citra = cv.line(citra, (0,0), (511, 511), (0, 255, 0), 5) 
citra = cv.line(citra, (511,0), (0, 511), (0, 255, 0), 5)

#kotak --- S = (X,Y) merupakan titik tengah
S = (width//2, height//2) #karena gambar berdimensi persegi maka titik tengah S = x/2, y/2
print(S)
citra = cv.rectangle(citra,((S[0]-50),S[0]-50),((S[1]+50),S[1]+50), 
        (0, 0, 255), 4)

#lingkaran
citra = cv.circle(citra, S, 50, (100, 0, 100), 5)

#cross di titik ujung
citra = cv.drawMarker(citra, (S), (255, 0, 0), markerType= cv.MARKER_CROSS, 
        markerSize= 20,thickness= 5, line_type=cv.LINE_AA)

#teks
font = cv.FONT_HERSHEY_COMPLEX
citra = cv.putText(citra, 'Latihan OpenCV', (10, 500), font, 1.8, (0,0,0), 2, cv.LINE_AA) 

cv.imshow('image', citra)

cv.waitKey(0)
cv.destroyAllWindows()