import cv2
import datetime
import numpy as np
import pytesseract as tess


platecascade = cv2.CascadeClassifier("C:\haarcascade_russian_plate_number.xml")
minArea = 500
cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("http://192.168.10.101:8080/video")

count = 0
while True:
    success, img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = platecascade.detectMultiScale(imgGray, 1.1, 4)

    for(x, y, w, h) in numberplates:
        wT, hT, cT=img.shape
        a, b = (int(0.02 * wT), int(0.02 * hT))
        plate=img[y+a:y+h-a, x+b:x+w-b, :]
        kernel=np.ones((1, 1), np.uint8)
        plate=cv2.dilate(plate, kernel, iterations=1)
        plate=cv2.erode(plate, kernel, iterations=1)
        plate_gray=cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        (thresh, plate)=cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))  #highlighting the number plate

        cv2.imshow("plate", plate)

    cv2.imshow("Detected Plate", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):   #it will save RoI image
        cv2.imwrite("C:\\Users\\nikun\PycharmProjects\\rsmieee\\IMAGES"+str(count)+".jpg", plate)
        cv2.rectangle(img, (0, 200), (640, 300), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, "Scan saved!", (15, 265), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 0)
        cv2.imshow("Detected  Plate", img)
        cv2.waitKey(500)

        count+=1
        break




        #code to detect the number plate of a vehicle.