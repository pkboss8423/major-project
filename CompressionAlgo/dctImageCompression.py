import os
from PIL import Image
from scipy.fftpack import dct, idct
import numpy as np
from PIL import Image
from Utils.createFolder import create_folder
global chuvin
import cv2


def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


def custom_dct(file_loc,ext, hybrid=False):
    im = cv2.imread(file_loc)
    im = cv2.resize(im, (1920, 1280))

    imF = dct2(im)
    im1 = idct2(imF)
    np.allclose(im, im1)

    x = create_folder()
    comp_file = 'final_dct.jpg'
    path = os.path.join(x, comp_file)

    cv2.imwrite(path, im1)
    im1 = np.float32(im1)
    image = Image.open(path)
    #image.show(title='Original:')
    if hybrid == False:
        image.show(title="DCT:")
    return path
