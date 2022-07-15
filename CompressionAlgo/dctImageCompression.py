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
    im = cv2.imread(file_loc)
    # wid = im.shape[1]

    # hgt = im.shape[0]
    # if hgt < 150*2:
    #     h = hgt

    # else:
    #     x = 150
    # if x == 150:
    #     y = (x/hgt)*100
    #     z = (wid*y)/100
    # if hgt < 1920:
    #     if hgt < 150*2:
    #         h = hgt
    #     else:
    #         h = hgt-x
    # else:
    #     h = 1920
    # if wid < 1280:
    #     if hgt < 150*2:
    #         w = wid
    #     else:
    #         w = wid-z
    # else:
    #     w = 1280
    # st.write(h,w)
    # im = cv2.resize(im, (int(h), int(w)))
    wid=im.shape[1]
    hgt = im.shape[0]
    wid = int(wid/2)
    hgt = int(hgt/2)
    im = cv2.resize(im, (wid, hgt))

    imF = dct2(im)
    im1 = idct2(imF)
    np.allclose(im, im1)

    x = create_image_folder()
    comp_file = 'final_dct'+ext
    path = os.path.join(x, comp_file)

    cv2.imwrite(path, im1)
    im1=Image.open(path)
    if hybrid == False:
        st.image(im1, caption="DCT Image", width=500)
    return path
