import numpy as np
import cv2
from yolov5 import detect1
import torch

weight = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/src/best.pt'
source = '0'
output = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found'

with torch.no_grad():
    detect1.detect(weights=weight, source=source, out=output)
