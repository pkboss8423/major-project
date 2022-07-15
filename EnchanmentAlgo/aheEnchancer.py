import os
import cv2
import numpy as np
from Utils.createFolder import create_image_folder
from PIL import Image

def AHE(st,pathIn,ext):
    img = cv2.imread(pathIn, 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)

    # stacking images side-by-side
    res = np.hstack((img, equ))
    x = create_image_folder()
    ahe_img = "ahe_img"+ext
    path = os.path.join(x, ahe_img)
    cv2.imwrite(path, equ)
    img = Image.open(path)
    st.image(img, caption="AHE Enhancment",  width=500)
    return path
