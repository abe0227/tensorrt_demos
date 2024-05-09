import RPi.GPIO as GPIO
import cv2

from utils.yolo_classes import get_cls_dict
####################################################################################
# EXP2
def show_info (boxes, confs, clss):
   print ("//-----------------------------------")
   # for-loop fitting boxes[x],confs[x],clss[x] to i,j,k 
   for i,j,k in zip(boxes, confs, clss):
      cls_list = get_cls_dict(80)  # set cls_list = coco dataset class name
      cls_name=cls_list[int(k)]    # turn float type clss to class name
      print ('clss:',cls_name,'confs:',j,'boxes:',i)

def detect_human (boxes, confs, clss, output_pin):
   '''
   # write your code there and delete 'pass'
   # note: clss==0 is person
   '''
   pass

def detect_human_num (boxes, confs, clss, output_pin, num):
   '''
   # write your code there and delete 'pass'
   '''
   pass
   


def detect_mode (mode, boxes, confs, clss, output_pin, num=5):
   if mode == 0:
      pass
   elif mode == 1:
      show_info (boxes, confs, clss)
   elif mode == 2:
      detect_human (boxes, confs, clss, output_pin)
   elif mode == 3:
      detect_human_num (boxes, confs, clss, output_pin, num)

####################################################################################
# EXP3
def detect_human_distance (img, boxes, confs, clss, output_pin):
   '''
   # write your code there
   # note: boxes[x] = (top_left x, top_left y, bottom_right x, bottom_right y)
   # note: use 'img=cv2.circle(img, (x, y), 5, (0, 0, 255), -1)' to draw the circle
                    cv2.circle(img, position, radius, (B,G,R), -1(fill up))
   '''
   
   return img
