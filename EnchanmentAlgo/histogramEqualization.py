import cv2
import numpy as np


def calculate_histogram(st,pathIn):
    # img = cv2.imread(pathIn)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    # fig, ax = plt.subplots()
    # #fig = plt.figure(figsize=(10, 5))
    # ax.hist(img,bins=20)
    # st.pyplot(fig)
    image = cv2.imread(pathIn)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    histr = cv2.calcHist([image],[0],None,[256],[0,256])
    st.line_chart(histr)
