import cv2
import mediapipe as mp
import pyautogui # for controlling the mouse
import math
import time

capture_hands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
webcam = cv2.VideoCapture(0)

x1 = y1 = x2 = y2 = 0
click_cooldown = 0

while True:
    _,img = webcam.read()
    image_height, image_width, _ = img.shape
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(img_rgb)
    hands = output_hands.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_option.draw_landmarks(img, hand)
            one_hand_landmarks = hand.landmark
            for id, landmark in enumerate(one_hand_landmarks):
                x = int(landmark.x * image_width)
                y = int(landmark.y * image_height)
                
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    cv2.circle(img, (x, y), 10, (0, 255, 0))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(img, (x, y), 10, (0, 255, 0))
        dist = math.hypot(x2 - x1, y2 - y1)
        print(dist)        
        if dist < 40:
            if time.time() - click_cooldown > 0.3: # 1 second cooldown
                pyautogui.click()
                print("Click")
                click_cooldown = time.time()

    cv2.imshow("Hand Gesture Movement", img)
    key = cv2.waitKey(1)
    if key == 27: #(27 is escape key)
        break
webcam.release()
cv2.destroyAllWindows()    
