import cv2
import numpy as np

class Bomb_detector:
  def __init__ (self, classifier, min_neighbors):
    self.status = False # if bomb has detected or not
    self.classifier = classifier # haar cascade classificator
    self.neig = min_neighbors # set min neighbors
    self.center_box = 0 # center of the detection box
    self.lenght = 0 # lenght of the detection box

  def bomb_det(self, image_in):
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    image_grey = cv2.cvtColor(image_in, cv2.COLOR_BGR2GRAY)

    detections = self.classifier.detectMultiScale(image_grey, scaleFactor=1.1,
                                           minNeighbors = self.neig,
                                           minSize=(1,1),
                                           maxSize=(3000,3000))

    print(detections) # print bomb detections(for debug)

    if len(detections) == 0:
      self.status = False
    else:
      self.status = True

    # draw a square in detections and calc center of the box and lenght (last bomb detected)
    for (x, y, l, a) in detections:
      cv2.rectangle(image_in, (x, y), (x + l, y + a), (0,255,0), 2)
      self.center_box = x + (l/2)
      self.lenght = l

    # prints for debug
    print(self.center_box)
    print(self.lenght)
    print(self.status)

    return image_in, self.status, self.center_box, self.lenght 