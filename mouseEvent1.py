import numpy as np
import cv2 as cv
# fungsi mouse callback
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK: # event berupa mouse left button
        cv.circle(img,(x,y),100,(255,0,0),1) #hasilnya adalah lingkaran
        cv.drawMarker(img, (x,y), (255, 0, 0), markerType= cv.MARKER_CROSS, 
        markerSize= 20,thickness= 5, line_type=cv.LINE_AA)
        print('x:', x, 'y:', y)

# membuat sebuah gambar hitam dengan resolusi 512x512 
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

#memanggil dan menerapkan fungsi mouse callback pada gambar tsb 
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27: #keluar menggunakan tombol escape
        break
cv.destroyAllWindows()