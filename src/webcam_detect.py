import torch 
import os
import sys
import cv2


def video_capture():
# Video source - can be camera index number given by 'ls /dev/video*
# or can be a video file, e.g. '~/Video.avi'
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
        # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            print('Shape of gray farme: ', gray.shape)
            #detect(gray)

        # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

""" 
def detect(frame):
    PATH = './yolov5/best.pt'
    
    #load model and detect """
    
video_capture()