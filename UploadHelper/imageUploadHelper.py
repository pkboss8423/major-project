import cv2

#this function reads image and converts it into grayscale
def image_Read(pathIn):
    instance = cv2.imread(pathIn)
    instance = cv2.cvtColor(instance, cv2.COLOR_BGR2GRAY)
    return instance
