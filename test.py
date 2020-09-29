import numpy as np
import cv2
from yolov5 import detect, utils
import torch
from src.save_img import save
from threading import Thread


weight = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/src/best.pt'
source = '0'
# output = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found'
folder = '/Users/jacopoclocchiatti/Documents/Progetti_Vari/Face_Detection/Faces_found'

if __name__ == '__main__':
    with torch.no_grad():
        for face in detect.detect(weights=weight, source=source):
            thread = Thread(target=save, args=([face, folder]), daemon=True)
            print('\nStarting saving thread')
            thread.start
            #save(face, folder)

