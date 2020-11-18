import cv2
import numpy as np
import sys
import os
import fnmatch

def sharpen(image):
    kernel= ([[0,-1,0],[-1,5,-1],[0,-1,0]])
    new_image=  cv2.filter2D(image, -1, kernel)
    cv2.imshow("Sharpened",image)
    cv2.waitKey(0)
    return


def blur(image):
    kernels={3,5,9,13}
    for idx, k in enumerate(kernels):
        image_b1=cv2.blur(image,ksize=(k,k))
        cv2.imshow(str(k),image_b1)
        cv2.waitKey(0)
    return
def resize(fname,width,height):
    image=cv2.imread(fname)
    cv2.imshow("original Image",image)
    cv2.waitKey(0)
    org_height,org_width=image.shape[0:2]
    print("width:",org_width)
    print("height",org_height)


    if org_width>=org_height:
        new_image=cv2.resize(image,(width, height))
    else:
        new_image=cv2.resize(image,(height,width))
    return fname,new_image




filename,newimage=resize("heybuddy.jpg",1200,500)
#cv2.imshow("resize Image",new_image)
#cv2.waitKey(10)
blur(new_image)
#image=sharpen(new_image)
