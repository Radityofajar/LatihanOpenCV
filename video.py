import cv2 as cv

vid = cv.VideoCapture(0) #args dapat berupa file video atau kamera webcam 0/1/2/-1 
#format fourcc https://www.fourcc.org/codecs.php
fourcc = cv.VideoWriter_fourcc(*'MJPG') #dapat juga ditulis 'X', 'V', 'I', 'D'
output = cv.VideoWriter('output.avi', fourcc, 20.0 , (1280, 720))

if not vid.isOpened():
    print("Tidak dapat membuka video ataupun kamera")
    exit()

while(vid.isOpened()): #membuat loop terus menerus hingga perintah keluar
    ret, frame = vid.read() #menangkap gambar per-frame

    #bila tidak dapat menangkap frame akan muncul notif
    if not ret:
        print("Tidak dapat menerima frame")
        break
    
    #frame = cv.flip(frame, 0)
    if ret == True:
        

        print(vid.get(cv.CAP_PROP_FPS))
        print(vid.get(cv.CAP_PROP_FRAME_WIDTH))
        print(vid.get(cv.CAP_PROP_FRAME_HEIGHT))

        #operasi tiap frame dilakukan berdasarkan perintah dibawah
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #mengubah frame (RGB) menjadi GrayScale
        cv.imshow('frame', gray) #menampilkan tiap frame-nya di layar monitor 

        output.write(frame)

        #membuat perintah keluar 
        if cv.waitKey(1) & 0xFF == ord('q'): #perintah keluar ada ditombol q
            break
    else:
        break
#melepaskan video dan menutup window
vid.release()
output.release()
cv.destroyAllWindows()