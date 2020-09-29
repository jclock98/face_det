from fastai.vision.all import *

classifier = load_learner('age.pkl')

#run the prediction
path = ''
img = cv2.imread(path, cv2.IMREAD_COLOR)
results = classifier.predict(img)
print(results)