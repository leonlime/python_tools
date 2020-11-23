import cv2
import numpy as np

class Color_detector:
  def __init__ (self, low_col, upp_col):
    self.lower_color = low_col
    self.upper_color = upp_col

  def color_det(self, image_in):
    # Converting the Input Into HSV Format
    hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    
    # Filtering out color Pixels
    color_mask = cv2.inRange(hsv, self.lower_color, self.upper_color)

    # Finding Contours
    _, contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # color_det var
    color_det = False

    # changing color_det var to TRUE if a color object are detected
    for contour in contours:
      area = cv2.contourArea(contour)
      if (area > 0):
        color_det = True

    # return TRUE or FALSE
    return color_det, area
    
