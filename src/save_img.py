from datetime import datetime
import csv
from os.path import join
from PIL import Image, ImageFile
import cv2
from numpy.random import seed, randint


def save(image, folder='~/Documents/Progetti_Vari/Face_Detection/Faces_found'):
    seed(42)
    
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")	

    gender = '' # gender_detect(image)

    age = '' #age_detect(image)

    rand_counter = str(randint(1,99,1)[0])

    filename = date_time + '_' + gender + '_' + age + '_' + rand_counter + '.jpeg'

    #folder = '~/Documents/Progetti_Vari/Face_Detection/Faces_found/'
    file_path = join(folder, filename)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image.save(file_path, "JPEG", quality=100, optimize=True, progressive=True)

    with open(join(folder, 'face_found.csv'), mode='a') as faces_file:
        face_writer = csv.writer(faces_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        face_writer.writerow([filename, gender, age, date_time])

