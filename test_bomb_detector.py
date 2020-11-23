from classes.color_detector import Color_detector
import cv2
import numpy as np

# create color detectors
red_detect = Color_detector(np.array([17, 15, 100]), np.array([50, 56, 200]))

blue_detect = Color_detector(np.array([110,50,50]), np.array([130,255,255]))

yellow_detect = Color_detector(np.array([20, 100, 100]), np.array([32, 255, 255]))

green_detect  = Color_detector(np.array([25, 52, 72]), np.array([102, 255, 255]))

# read a image
image = cv2.imread('images/bomba.jpg')

# detect colors
red, red_area = red_detect.color_det(image)
blue, blue_area = blue_detect.color_det(image)
yellow, yellow_area = yellow_detect.color_det(image)
green, green_area = green_detect.color_det(image)

# print info
print('Red: ' + str(red))
print('Red area: ' + str(red_area))
print('Blue: ' + str(blue))
print('Blue area: ' + str(blue_area))
print('Yellow: ' + str(yellow))
print('Yellow area: ' + str(yellow_area))
print('Green: ' + str(green))
print('Green area: ' + str(green_area))
