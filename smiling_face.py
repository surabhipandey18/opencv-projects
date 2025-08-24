import cv2
import mediapipe as mp
import pyautogui # for controlling the mouse
import winsound
import time

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
webcam = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
last_snap_time = 0

while True:
    _, img = webcam.read()
    img = cv2.flip(img, 1)
    fh, fw, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(img_rgb)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)
            if id == 43: 
                x1 = x
                y1 = y
            if id == 287:
                x2 = x
                y2 = y    
        dist = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
        print(dist)
        if dist > 75:
            cv2.imwrite("selfie.png", img)
            winsound.PlaySound("camera1.wav", winsound.SND_FILENAME)
            time.sleep(1)
            last_snap_time = time.time()
    cv2.imshow("Auto Selfie Face", img)
    key = cv2.waitKey(1)
    if key == 27: #(27 is escape key)
        break
webcam.release()
cv2.destroyAllWindows()    