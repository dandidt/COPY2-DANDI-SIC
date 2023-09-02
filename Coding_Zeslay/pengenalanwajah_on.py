import numpy as np
import face_recognition
import cv2
import buzzer_on
import selenoid_off
# import selenoid_on
import time 

face_encodings = np.load("face_encodings.npy")
face_ids = np.load("face_ids.npy")

cam = cv2.VideoCapture(0)
cam.set(3, 340) 
cam.set(4, 255) 

cam.set(cv2.CAP_PROP_FPS, 30)

face_names = []

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(gray)
    
    for (top, right, bottom, left) in faces:
        face_encoding = face_recognition.face_encodings(img, [(top, right, bottom, left)])[0]
        matches = face_recognition.compare_faces(face_encodings, face_encoding)
        
        name = "Tidak Dikenal"
        if True in matches:
            matched_ids = face_ids[np.where(matches)]
            name = str(matched_ids[0])
            selenoid_off.close_sele()
            buzzer_on.main_buzzer()
        
        face_names.append(name)
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        # run = selenoid_on.setup()
        # print (run)
    
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
