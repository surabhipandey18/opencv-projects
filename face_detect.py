import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)
while True:
    _,img = webcam.read()
    cv2.imshow("Face Detection", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Face Detection", img)    
    key = cv2.waitKey(10)
    if key == 27: #(27 is esclape key)
        break 
webcam.release()
cv2.destroyAllWindows()



