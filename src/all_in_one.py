from fastai.vision.all import * 
import cv2


#load the trained model 
gen_class = load_learner('gender.pkl')
age_class = '' #load_learner('age.pkl')
yolo = '' #load yolo 

def gender_detect(img):

    results = gen_class.predict(img)
    if results[0] == '0':
        gender = 'M'
    else:
        gender = 'F'
    
    return gender


def age_detect(img):
    
    results = age_class.predict(img)

    return age


def detect(frame):
    PATH = './yolov5/best.pt'
    #return a list of face recognized

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
            detect(gray)

        # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
