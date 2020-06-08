import cv2
import matplotlib.pylab as plt
import numpy as np

class Vision:
  def __init__(self, type_r):
    self.type_road = type_r

  def region_of_interest(self, img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image    
  
  def get_point(self, image_in):
    image = image_in 
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_inv = cv2.bitwise_not(image_grey)

    # get image sizes
    height = image.shape[0]
    width = image.shape[1]

    # region type 1
    if self.type_road == 1:
      region_of_interest_vertices = [
        (0, height), 
        (width/2, height/2),
        (width, height)
      ]

    # region type 2
    if self.type_road == 2:
      region_of_interest_vertices = [
        (0, 0),
        (0, height),
        (width, 0),
        (width, height)
      ]

    #cropp image
    cropped_image = self.region_of_interest(image_inv, np.array([region_of_interest_vertices], np.int32))

    # get threshold
    thresh = cv2.threshold(cropped_image, 125, 255, cv2.THRESH_BINARY)[1]

    # find contours
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
      # get bigger area
      c = max(contours, key = cv2.contourArea)
      # compute the center of the conto
      M = cv2.moments(c)
      if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    # return central point of road
    return (cX, cY)