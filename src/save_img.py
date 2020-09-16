from datetime import datetime
import csv
from os.path import join
from PIL import Image, ImageFile
import cv2

def save(image):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")	

    gender = '' # gender_detect(image)

    age = '' #age_detect(image)

    filename = date_time + gender + age + '.jpeg' #counter?

    folder = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found/' # look how to always determine the location of this folder
    file_path = join(folder, filename)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image.save(file_path, "JPEG", quality=100, optimize=True, progressive=True)

    with open('/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found/face_found.csv', mode='a') as faces_file:
        face_writer = csv.writer(faces_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        face_writer.writerow([filename, gender, age, date_time])

x = cv2.imread('../1263-045134-imagepage-scaled.jpg')
x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
save(x)
