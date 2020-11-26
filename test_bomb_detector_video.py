#!/usr/bin/env python 
from classes.bomb_detector import Bomb_detector
import cv2
import numpy as np

classificador1 = cv2.CascadeClassifier('cascade1.xml')
classificador2 = cv2.CascadeClassifier('cascade2.xml')
classificador3 = cv2.CascadeClassifier('cascade3.xml')

# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 

while True:
  # read a image
  _, image1 = webcam.read()
  _, image2 = webcam.read()
  _, image3 = webcam.read()

  bomb_detect1 = Bomb_detector(classificador1, 50)
  bmb1, ident1 = bomb_detect1.bomb_det(image1)

  bomb_detect2 = Bomb_detector(classificador2, 50)
  bmb2, ident2 = bomb_detect2.bomb_det(image2)

  bomb_detect3 = Bomb_detector(classificador3, 50)
  bmb1, ident3 = bomb_detect3.bomb_det(image3)

  cv2.imshow("raw1", image1)
  cv2.imshow("raw2", image2)
  cv2.imshow("raw3", image2)
  
  if cv2.waitKey(10) & 0xFF == ord('q'): 
    cap.release() 
    cv2.destroyAllWindows() 
    break

  # cv2.destroyAllWindows()
