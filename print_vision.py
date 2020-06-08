import cv2
import matplotlib.pylab as plt
import numpy as np

# FUNCTIONS:
def region_of_interest(img, vertices):
  mask = np.zeros_like(img)
  match_mask_color = 255
  cv2.fillPoly(mask, vertices, match_mask_color)
  masked_image = cv2.bitwise_and(img, mask)
  return masked_image

# read, grey convert and invert colors:
image = cv2.imread('images/test_vision.png') 
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_inv = cv2.bitwise_not(image_grey)

cv2.imwrite('images/inv.png', image_inv)

# get image sizes
height = image.shape[0]
width = image.shape[1]
region_of_interest_vertices = [
  (0, height),
  (width/2, height/2),
  (width, height)
]

#cropp image
cropped_image = region_of_interest(image_inv, np.array([region_of_interest_vertices], np.int32))

cv2.imwrite('images/crop.png', cropped_image)

# get threshold
thresh = cv2.threshold(cropped_image, 125, 255, cv2.THRESH_BINARY)[1]

# find contours
_, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for c in contours:
	# get bigger area
  c = max(contours, key = cv2.contourArea)
  # compute the center of the conto
  M = cv2.moments(c)
  if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    cv2.drawContours(thresh, [c], -1, (0, 255, 0), -2)
    cv2.circle(thresh, (cX, cY), 7, (120, 50, 26), -1)

cv2.imwrite('images/point.png', thresh)
#------------------------------------------------------------------
print("The images have been saved in the folder")
