from classes.vision import Vision
import rospy
import cv2

# main function
if __name__	== '__main__':
  try:
    cam_print = Vision(1)  
    cX, cY = cam_print.get_point(cv2.imread('images/test_vision.png')) 
    
    print('cX: ' + str(cX))
    print('cY: ' + str(cY))

  except rospy.ROSInterruptException:
    pass	