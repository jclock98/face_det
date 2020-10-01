from datetime import datetime
import csv
from os.path import join
from PIL import Image, ImageFile
import cv2
from numpy.random import seed, randint
from copy import deepcopy

min_img_dim = 640


def resize(img):
    if img.shape[0] <= img.shape[1]:
        width = min_img_dim
        scale = img.shape[0]/width
        height = img.shape[1]*scale
        resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    else:
        height = min_img_dim
        scale = img.shape[1]/width
        width = img.shape[0]*scale
        resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    return resized


def save(image, folder='~/Documents/Progetti_Vari/Face_Detection/Faces_found'):
    seed(randint(0, 99, 1)[0])
    
    if image.shape[0] < min_img_dim or image.shape[1] < min_img_dim:
        resized_img = resize(image)#resize face
        print('Resizing face')
    else:
        resized_img = image

    gender_image = resized_img.copy()
    age_image = resized_img

    gender = '' # gender_detect(gender_image)

    age = '' #age_detect(age_image)

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")	

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

