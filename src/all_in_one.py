from fastai.vision.all import * 
import cv2

from datetime import datetime
import csv
from os.path import join
from PIL import Image, ImageFile
import random 

random.seed(random.random())

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


def save(image):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")	

    gender = gender_detect(image)

    age = '' #age_detect(image)

    filename = date_time + gender + age + random.randint(0, 99) +'.jpeg' 

    folder = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found/' # look how to always determine the location of this folder
    file_path = join(folder, filename)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image.save(file_path, "JPEG", quality=100, optimize=True, progressive=True)

    with open('/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found/face_found.csv', mode='a') as faces_file:
        face_writer = csv.writer(faces_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        face_writer.writerow([filename, gender, age, date_time])


def detect(frame):
    PATH = './yolov5/best.pt'
    
    #for face in face_detected_list -> save image
    for face in faces_det:
        w *= 1.25
        h *= 1.25
        image = frame[x:x+w, y:y+h]
        save(image)

def video_capture():
# Video source - can be camera index number given by 'ls /dev/video*
# or can be a video file, e.g. '~/Video.avi'
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
        # Our operations on the frame come here
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detect(frame)

        # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
