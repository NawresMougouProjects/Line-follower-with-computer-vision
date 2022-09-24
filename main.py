import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('1.png')
cap = cv2.VideoCapture("http://192.168.1.8:8080/video")
cap.set(3,680)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    img = cv2.resize(img, (680, 480))
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        #if myData in myDataList:
        #    myOutput = 'Authorized'
        #    myColor = (0,255,0)
        #else:
        #    myOutput = 'Un-Authorized'
        #    myColor = (0, 0, 255)#

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(0,255,0),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xff == ord('q'):  # 1 is the time in ms
        break

capture.release()
cv2.destroyAllWindows