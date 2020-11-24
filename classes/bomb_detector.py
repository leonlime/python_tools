import cv2
import numpy as np

class Bomb_detector:
  def __init__ (self, low_red, 
                      upp_red,
                      low_green,
                      upp_green,     
                      low_blue,
                      upp_blue,
                      low_yellow,
                      upp_yellow):

    self.lower_red = low_red
    self.upper_red = upp_red

    self.lower_green = low_green
    self.upper_green = upp_green

    self.lower_blue = low_blue
    self.upper_blue = upp_blue

    self.lower_yellow = low_yellow
    self.upper_yellow = upp_yellow

  def color_det(self, image_in):
    # CONVERT AND CREATE THE MASK ################################################
    # Converting the Input Into HSV Format
    hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    
    # Filtering out color Pixels
    red_mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
    green_mask = cv2.inRange(hsv, self.lower_green, self.upper_green)
    blue_mask = cv2.inRange(hsv, self.lower_blue, self.upper_blue)
    yellow_mask = cv2.inRange(hsv, self.lower_yellow, self.upper_yellow)

    # Morphological Transform, Dilation for each color and bitwise_and operator between imageFrame and mask determines to detect only that particular color 
    kernal = np.ones((5, 5), "uint8") 
    # red
    red_mask = cv2.dilate(red_mask, kernal) 
    res_red = cv2.bitwise_and(image_in, image_in, mask = red_mask)
    # green
    green_mask = cv2.dilate(green_mask, kernal) 
    res_green = cv2.bitwise_and(image_in, image_in, mask = green_mask)
    # blue
    blue_mask = cv2.dilate(blue_mask, kernal) 
    res_blue = cv2.bitwise_and(image_in, image_in, mask = blue_mask)
    # yellow
    yellow_mask = cv2.dilate(yellow_mask, kernal) 
    res_yellow = cv2.bitwise_and(image_in, image_in, mask = yellow_mask)

    # COUNTOR SECTION AND PRINT THE IMAGE ################################################
    # Creating contour to track red color ------------------------------------------------
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    area_r = 0  
    for pic, contour in enumerate(contours): 
      area = cv2.contourArea(contour) 
      if(area > area_r):
        area_r = area
        contour_r = contour 
        
    x, y, w, h = cv2.boundingRect(contour_r) 
    image_in = cv2.rectangle(image_in, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Creating contour to track green color ------------------------------------------------
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    area_g = 0  
    for pic, contour in enumerate(contours): 
      area = cv2.contourArea(contour)
      if(area > area_g):
        area_g = area
        contour_g = contour 

    x, y, w, h = cv2.boundingRect(contour_g) 
    image_in = cv2.rectangle(image_in, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Creating contour to track blue color ------------------------------------------------
    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    area_b = 0  
    for pic, contour in enumerate(contours): 
      area = cv2.contourArea(contour)
      if(area > area_b):
        area_b = area
        contour_b = contour 
      
    x, y, w, h = cv2.boundingRect(contour_b) 
    image_in = cv2.rectangle(image_in, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Creating contour to track yellow color ------------------------------------------------
    contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    area_y = 0 
    for pic, contour in enumerate(contours):       
      area = cv2.contourArea(contour) 
      if(area > area_y):
        area_y = area
        contour_y = contour    
        
    x, y, w, h = cv2.boundingRect(contour_y) 
    image_in = cv2.rectangle(image_in, (x, y), (x + w, y + h), (0, 255, 255), 2)             

    # DEBUG PRINTS AND RETURN ################################################
    print("RED AREA: " + str(area_r))
    print("GREEN AREA: " + str(area_g))
    print("BLUE AREA: " + str(area_b))
    print("YELLOW AREA: " + str(area_y))

    if ((area_r * area_g * area_b * area_y) != 0):
      cv2.putText(image_in, "*BOMBA DETECTADA*", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))

    return image_in