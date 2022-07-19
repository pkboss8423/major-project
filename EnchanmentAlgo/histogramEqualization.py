import cv2
import numpy as np

#this function displays a histogram of the image
def calculate_histogram(st,pathIn):
    image = cv2.imread(pathIn)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    histr = cv2.calcHist([image],[0],None,[256],[0,256])
    st.line_chart(histr)
