#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    i11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy    
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                if id == 17:
                    id17 = int(id)
                    cx17 = cx    
                if id == 9:
                    id9 = int(id)
                    cy9 = cy
                if id == 0:
                    id0 = int(id)
                    cy0 = cy    


        
            if cy9 < cy0:
                    if cx4 > cx3 and cx5 > cx17:
                        cv2.putText(img,"Thumb Finger" , (10,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 0, 93), 3)
                    if cx4 < cx3 and cx5 < cx17:
                        cv2.putText(img,"Thumb Finger" , (10,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 0, 93), 3)    
                    if  cy8 < cy7:
                        cv2.putText(img,"Index Finger" , (10,110), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 21, 0), 3)
                    if  cy12 < cy11:
                        cv2.putText(img,"Middle Finger" , (10,150), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (97,255,0), 3)
                    if  cy16 < cy15:
                        cv2.putText(img,"Ring Finger" , (10,190), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0,255,233), 3)    
                    if  cy20 < cy19:
                        cv2.putText(img,"Pinky Finger" , (10,230), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 255), 3)    
                    if  cx5 < cx17: 
                        cv2.putText(img,"Left Hand" , (400,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 0), 3)
                    if  cx5 > cx17:
                        cv2.putText(img,"Right Hand" , (400,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 0), 3)   
            elif cy9 > cy0:
                    if cx4 > cx3 and cx5 > cx17:
                        cv2.putText(img,"Thumb Finger" , (10,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 0, 93), 3)
                    if cx4 < cx3 and cx5 < cx17:
                        cv2.putText(img,"Thumb Finger" , (10,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 0, 93), 3)    
                    if  cy8 > cy7:
                        cv2.putText(img,"Index Finger" , (10,110), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (255, 21, 0), 3)
                    if  cy12 > cy11:
                        cv2.putText(img,"Middle Finger" , (10,150), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (97,255,0), 3)
                    if  cy16 > cy15:
                        cv2.putText(img,"Ring Finger" , (10,190), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0,255,233), 3)    
                    if  cy20 > cy19:
                        cv2.putText(img,"Pinky Finger" , (10,230), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 255), 3)    
                    if  cx5 < cx17: 
                        cv2.putText(img,"Left Hand" , (400,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 0), 3)
                    if  cx5 > cx17:
                        cv2.putText(img,"Right Hand" , (400,70), cv2.FONT_HERSHEY_PLAIN, 2.5,
                        (0, 0, 0), 3)   

                    
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
   
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()
