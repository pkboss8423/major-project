import os
import cv2
import numpy as np
from Utils.createFolder import create_folder
from PIL import Image

def AHE(pathIn,ext):
    img = cv2.imread(pathIn, 0)

    equ = cv2.equalizeHist(img)

    # stacking images side-by-side
    res = np.hstack((img, equ))
    x = create_folder()
    ahe_img = "ahe_img"+ext
    path = os.path.join(x, ahe_img)
    cv2.imwrite(path, equ)
    img = Image.open(path)
    img.show()
    return path
