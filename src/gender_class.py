from fastai.vision.all import * 
import cv2

#load the trained model 
classifier = load_learner('gender.pkl')

#run the prediction
paths = [('../download.jpeg'),
        ('../download (1).jpeg'),
        ('../images.jpeg'),
        ('../images (1).jpeg')]

for path in paths:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    results = classifier.predict(img)
    print(results)