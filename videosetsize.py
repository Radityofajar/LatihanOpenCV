import cv2 as cv
import datetime

vid = cv.VideoCapture(0) #args dapat berupa file video atau kamera webcam 0/1/2/-1 
#format codecs fourcc di https://www.fourcc.org/codecs.php


#640 = target width, 480 = target height--tp tergantung dari kamera
#vid.set(3, 640) #3 = video width/ cv.CAP_PROP_FRAME_WIDTH)
#vid.set(4, 480) #4 = video height/ cv.CAP_PROP_FRAME_HEIGHT
#vid.set(cv.CAP_PROP_FPS, 30)

fps = vid.get(cv.CAP_PROP_FPS)
height = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv.CAP_PROP_FRAME_WIDTH)
print(fps)
print(width)
print(height)

while(vid.isOpened()): #membuat loop terus menerus hingga perintah keluar
    ret, frame = vid.read() #menangkap gambar per-frame

    #bila tidak dapat menangkap frame akan muncul notif
    if not ret:
        print("Tidak dapat menerima frame")
        break
    
    #frame = cv.flip(frame, 0)
    if ret == True:
        

        #operasi tiap frame dilakukan berdasarkan perintah dibawah
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #mengubah frame (RGB) menjadi GrayScale
        
        font = cv.FONT_HERSHEY_COMPLEX

        #menunjukkan resolusi video dan fps
        text = 'Width: ' + str(width) + ' Height: ' + str(height) + ' FPS: ' + str(fps)

        #menunjukkan tanggal dan waktu
        date = str(datetime.datetime.now())

        cv.putText(frame, date, (10,50), font, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow('frame', frame) #menampilkan tiap frame-nya di layar monitor 

        #membuat perintah keluar 
        if cv.waitKey(1) & 0xFF == ord('q'): #perintah keluar ada ditombol q
            break
    else:
        break

#melepaskan video dan menutup window
vid.release()

cv.destroyAllWindows()