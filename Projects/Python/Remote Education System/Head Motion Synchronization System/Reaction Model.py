﻿import cv2
import numpy as np
from naoqi import ALProxy

# Set IP address and port
motion = ALProxy("ALMotion", "192.168.1.161", 9559)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:\Users\Robin\Desktop\nodcontrol.avi', fourcc, 20.0, (640, 480))

# Distance function
def distance(x,y):
    import math
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

# Capture source video
cap = cv2.VideoCapture(0)

# Parameters for ShiTomasi corner detection
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

# Parameters for Lucas Kanade Optical Flow
lk_params = dict(winSize = (15, 15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Path to face cascade
face_cascade = cv2.CascadeClassifier('C:\Users\Robin\Documents\Visual Studio 2010\Projects\Head Nodding Detection\Head Nodding Detection\haarcascade_frontalface_alt.xml')

# Function to get coordinates
def get_coords(p1):
    try: return int(p1[0][0][0]), int(p1[0][0][1])
    except: return int(p1[0][0]), int(p1[0][1])

# Define font and text color
font = cv2.FONT_HERSHEY_SIMPLEX

# Define movement thresholds
max_head_movement = 20
movement_threshold = 50
gesture_threshold = 40

# Find the face in the image
face_found = False
frame_num = 0
while frame_num < 30:
    # Take first frame and find corners in it
    frame_num += 1
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        face_found = True
    cv2.imshow('image', frame)
    out.write(frame)
    cv2.waitKey(1)
face_center = x+w/2, y+h/3
p0 = np.array([[face_center]], np.float32)

gesture = False
x_movement = 0
y_movement = 0
gesture_show = 10 # Number of frames a gesture is shown

while True:
     ret, frame = cap.read()
     old_gray = frame_gray.copy()
     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
     cv2.circle(frame, get_coords(p1), 4, (0,0,255), -1)
     cv2.circle(frame, get_coords(p0), 4, (255, 0, 0))

     # Get the xy coordinates for point p0 and p1
     a, b = get_coords(p0), get_coords(p1)
     x_movement += abs(a[0] - b[0])
     y_movement += abs(a[1] - b[1])

     text = 'x_movement: ' + str(x_movement)
     if not gesture: cv2.putText(frame, text, (50, 50), font, 0.8, (0, 0, 255), 2)
     text = 'y_movement: ' + str(y_movement)
     if not gesture: cv2.putText(frame, text, (50, 100), font, 0.8, (0, 0, 255), 2)

     if x_movement > gesture_threshold:
         gesture = 'No'
     if y_movement > gesture_threshold:
         gesture = 'Yes'
     if gesture and gesture_show > 0:
         cv2.putText(frame, 'Gesture Detected: ' + gesture, (50, 50), font, 1.2, (0, 0, 255), 3)
         gesture_show -= 1
     if gesture_show == 0:
          gesture = False
          x_movement = 0
          y_movement = 0
          gesture_show = 10 # Number of frames a gesture is shown
     if (y_movement > gesture_threshold) and gesture_show == 1: 
        # Set stiffness on head motors
        motion.setStiffnesses("Head", 1.0)

        # Will go to 0.1 then 0 radian in 0.5 sec (2.0 Hz)
        motion.angleInterpolation (["HeadPitch"], 
                                   [0.0, 0.1, 0.0, -0.1, 0.0], 
                                   [0.1, 0.2, 0.3, 0.4, 0.5], 
                                   False, 
                                   _async = True)

        # Set stiffness off for head motors
        motion.setStiffnesses("Head", 0.0)

        print distance(get_coords(p0), get_coords(p1))
        p0 = p1

     cv2.imshow('image', frame)
     out.write(frame)
     cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()
















