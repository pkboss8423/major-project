import os
from turtle import width
from PIL import Image
from scipy.fftpack import dct, idct
import numpy as np
from Utils.createFolder import create_folder
import cv2


def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


def custom_dct(st, file_loc, ext, hybrid=False):
    im = cv2.imread(file_loc)
    wid = im.shape[1]

    hgt = im.shape[0]
    x=150
    y=(x/hgt)*100
    z=(wid*y)/100
    if hgt < 1920:
        h = hgt-x
    else:
        h = 1920
    if wid < 1280:
        w = wid-z
    else:
        w = 1280
    im = cv2.resize(im, (h, w))

    imF = dct2(im)
    im1 = idct2(imF)
    np.allclose(im, im1)

    x = create_folder()
    comp_file = 'final_dct.jpg'
    path = os.path.join(x, comp_file)

    cv2.imwrite(path, im1)
    im1 = np.float32(im1)
    image = Image.open(path)
    # image.show(title='Original:')
    if hybrid == False:
        st.image(image, caption="DCT Image", width=500)
    return path
