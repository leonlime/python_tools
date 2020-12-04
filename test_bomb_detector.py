#!/usr/bin/env python 
from classes.bomb_detector import Bomb_detector
import cv2
import numpy as np

image = cv2.imread('images/bomba8.jpeg')
classificador1 = cv2.CascadeClassifier('cascade4.xml')

# create bomb detectors
bomb_detect = Bomb_detector(classificador1, 70)
bmb, ident = bomb_detect.bomb_det(image)

cv2.imshow("bomb_det", bmb)

cv2.waitKey(0)    
cv2.destroyAllWindows()

