# INITIAL SETUP
# ----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os

folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0];
kill = graphic[1];
winner = graphic[2];

cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
cv2.waitKey(1)

while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    '''
kill = cv2.imread("frames\img2.png")
cv2.imshow('frame')
cv2.waitKey(10000)
winner = cv2.imread("frames\img3.png")
cv2.imshow('frame')
cv2.waitKey(10000)
'''
capture = cv2.VideoCapture(0)

# to stop video/webcam
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)

    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break



img = cv2.imread('img\sqr(2).png')
cv2.imshow('Cookie', img)
cv2.waitKey(1000)

while True:
    cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

capture = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=2, detectionCon=0.77)
while True:
    isTrue, frame = capture.read()
    hands, img = detector.findHands(frame, flipType=True)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

    cv2.imshow('web cam', frame)


    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows() 


gameOver = False
NotWon = True

# GAME LOGIC UPTO THE TEAMS
# -----------------------------------------------------------------------------------------
while not gameOver:
    success, img = cam.read()
    img = cv2.flip(img, 1)
    img = overlayPNG(intro, img, [150, 100])
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        bbox = hand["bbox"]
        fingers = detector.fingersUp(hand)
        if fingers == [0, 0, 0, 0, 0]:
            x, y = lmList[8][1], lmList[8][2]
            x_center, y_center = (bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2
            if x_center - 50 < x < x_center + 50 and y_center - 50 < y < y_center + 50:
                img = overlayPNG(mlsa, img, [x_center - 50, y_center - 50])
                if x_center - 50 < 200 < x_center + 50 and y_center - 50 < 300 < y_center + 50:
                    NotWon = False
                    break
    cv2.imshow("Dalgona Game", img)
    cv2.waitKey(1)

# LOSS SCREEN
if NotWon:
    for i in range(10):
        img = overlayPNG(kill, img, [0, 0])
        cv2.imshow("Dalgona Game", img)
        cv2.waitKey(100)
    while True:
        img = overlayPNG(kill, img, [0, 0])
        cv2.imshow("Dalgona Game", img)
        if cv2.waitKey(1) == ord("q"):
            break

else:
    # WIN SCREEN
    img = overlayPNG(winner, img, [0, 0])
    cv2.imshow("Dalgona Game", img)
    while True:
        img = overlayPNG(winner, img, [0, 0])
        cv2.imshow("Dalgona Game", img)
        if cv2.waitKey(1) == ord("q"):
            break

# destroy all the windows
cv2.destroyAllWindows()
