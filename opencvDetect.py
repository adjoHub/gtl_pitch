import numpy as np
import cv2

#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade.xml')

#Capture video from the webcam
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    #Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(gray,(x,y),(x+w, y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow('Oculus',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()