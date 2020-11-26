import cv2
import numpy as np

class Bomb_detector:
  def __init__ (self, classifier, min_neighbors):
    self.ident = False
    self.classifier = classifier
    self.neig = min_neighbors

  def bomb_det(self, image_in):
    # Converting the Input Into HSV Format (this is a test)
    hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    
    imagemcinza = cv2.cvtColor(image_in, cv2.COLOR_BGR2GRAY)

    detections = self.classifier.detectMultiScale(imagemcinza, scaleFactor=1.1,
                                           minNeighbors = self.neig,
                                           minSize=(10,10),
                                           maxSize=(3000,3000))

    for (x, y, l, a) in detections:
      cv2.rectangle(image_in, (x, y), (x + l, y + a), (0,255,0), 2)

    return image_in, self.ident