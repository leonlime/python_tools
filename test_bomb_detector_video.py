#!/usr/bin/env python 
from classes.bomb_detector import Bomb_detector
import cv2
import numpy as np

# create color detectors
bomb_detect = Bomb_detector(np.array([136, 87, 111]), 
                            np.array([180, 255, 255]),
                            np.array([25, 52, 72]), 
                            np.array([102, 255, 255]),                      
                            np.array([94, 80, 2]), 
                            np.array([120, 255, 255]),                      
                            np.array([20, 100, 100]), 
                            np.array([32, 255, 255]))

# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 

while(1):
  # read a image
  _, image = webcam.read()
  cv2.imshow("raw", image)

  bmb = bomb_detect.color_det(image)

  cv2.imshow("bomb", bmb)

  key = cv2.waitKey(0)    
  if key == 27:
    break

  # cv2.destroyAllWindows()

  