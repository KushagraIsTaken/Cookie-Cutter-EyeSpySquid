import cv2 as cv
from Hand_Tracking_Module import handDetector

capture = cv.VideoCapture(0)
detector = handDetector.handDetector(maxHands=2, detectionCon=0.77)
## max hands for no of hands we need to detect
## detectionCon for percentage of error we can allow. Range is from 0 to 1

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

    cv.imshow('Video', frame)

    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows() 
