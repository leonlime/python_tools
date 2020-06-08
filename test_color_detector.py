from classes.color_detector import Color_detector
import cv2
import numpy as np

# create color detectors
blue_detect = Color_detector(np.array([110,50,50]), np.array([130,255,255]))

yellow_detect = Color_detector(np.array([20, 100, 100]), np.array([32, 255, 255]))

brown_detect  = Color_detector(np.array([0, 0, 70]), np.array([255, 255, 80]))

# read a image
image = cv2.imread('images/colors.png')

# detect colors
blue = blue_detect.color_det(image)
yellow = yellow_detect.color_det(image)
brown = brown_detect.color_det(image)

# print info
print('Blue: ' + str(blue))
print('Yellow: ' + str(yellow))
print('Brown: ' + str(brown))
