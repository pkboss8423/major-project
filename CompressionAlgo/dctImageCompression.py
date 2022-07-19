import os
from PIL import Image
from scipy.fftpack import dct, idct
import numpy as np
from Utils.createFolder import  create_image_folder
import cv2
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')
def custom_dct(st, file_loc, ext, hybrid=False):
    im = cv2.imread(file_loc)                                       #read image using cv2
    wid=im.shape[1]
    hgt = im.shape[0]
    wid = int(wid/2)
    hgt = int(hgt/2)
    im = cv2.resize(im, (wid, hgt))                                 #resizing image for faster dct
    imF = dct2(im)                                                  #dct function  returns image
    im1 = idct2(imF)                                                #inverse dct function returuns image
    np.allclose(im, im1)                                            #return true or false after checking fault tolerance
    x = create_image_folder()                                       #creating a local folder to save image
    comp_file = 'final_dct'+ext
    path = os.path.join(x, comp_file)                               #creating image path                  
    cv2.imwrite(path, im1)                                          #saving path
    im1=Image.open(path)
    if hybrid == False:                                             #condition in case of hybrid is run
        st.image(im1, caption="DCT Image", width=500)
    return path
