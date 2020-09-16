from datetime import datetime
import csv
from os.path import join
from cv2 import imwrite


def save(image):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")	

    gender = '' # gender_detect(image)

    age = '' #age_detect(image)

    filename = date_time + gender + age + '.jpg' #counter?

    folder = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_founded/' # look how to always determine the location of this folder
    file_path = join(folder, filename)
    imwrite(file_path, image)

    with open('*.csv', mode='w') as faces_file:
        face_writer = csv.writer(faces_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        face_writer.writerow([filename, gender, age, datetime])

save('x')