
from scipy.fftpack import dct, idct
import numpy as np
import cv2
import os
import matplotlib.pylab as plt
import shutil
import pywt
import re
from os.path import isfile, join
from PIL import Image, ImageEnhance
import numpy
import streamlit as st


def create_folder():
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, 'Documents')
    if not os.path.exists(path+"/C_Videos"):
        os.makedirs(path+"/C_Videos")
    path = os.path.join(userprofile, 'Documents', 'C_videos')
    return path


def frame_rate(cam):
    _, fo = cam.read()
    framei = cv2.cvtColor(fo, cv2.COLOR_BGR2GRAY)
    bg_avg = np.float32(framei)
    video_width = int(cam.get(3))
    video_height = int(cam.get(4))
    fr = int(cam.get(5))
    print("frame rate of stored video:::", fr)
    return fr


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    sorted_images = sorted(files, key=natural_sort_key)
    for i in range(len(sorted_images)):
        filename = pathIn + sorted_images[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'MP4V'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    st.write("Video Finished")
    out.release()


def max_ndarray(mat):
   
    return np.amax(mat) if type(mat).__name__ == 'ndarray' else 0


def extract_rgb_coeff(img):
  
    (width, height) = img.size
    img = img.copy()

    mat_r = numpy.empty((width, height))
    mat_g = numpy.empty((width, height))
    mat_b = numpy.empty((width, height))

    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            mat_r[i, j] = r
            mat_g[i, j] = g
            mat_b[i, j] = b

    coeffs_r = pywt.dwt2(mat_r, 'haar')

    coeffs_g = pywt.dwt2(mat_g, 'haar')

    coeffs_b = pywt.dwt2(mat_b, 'haar')

    return (coeffs_r, coeffs_g, coeffs_b)


def img_from_dwt_coeff(coeff_dwt):
   
    # Channel Red
    (coeffs_r, coeffs_g, coeffs_b) = coeff_dwt

    cc = numpy.array((coeffs_r, coeffs_g, coeffs_b), dtype=object)

    (width, height) = (len(coeffs_r[0]), len(coeffs_r[0][0]))

    cARed = numpy.array(coeffs_r[0])
    
    # Channel Green
    cAGreen = numpy.array(coeffs_g[0])
   
    # Channel Blue
    cABlue = numpy.array(coeffs_b[0])
    

    # maxValue per channel par matrix
    cAMaxRed = max_ndarray(cARed)
    cAMaxGreen = max_ndarray(cAGreen)
    cAMaxBlue = max_ndarray(cABlue)

    

    # Image object init
    dwt_img = Image.new('RGB', (width, height), (0, 0, 20))
    # cA reconstruction

    '''
    The image formed from the low frequnecy of the images which contains the main content of the image
    '''
    for i in range(width):
        for j in range(height):
            R = cARed[i][j]
            R = (R/cAMaxRed)*100.0
            G = cAGreen[i][j]
            G = (G/cAMaxGreen)*100.0
            B = cABlue[i][j]
            B = (B/cAMaxBlue)*100.0
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i, j), new_value)

    return dwt_img


def load_img(path):

    try:
        return Image.open(path)
    except IOError:
        return None


def running(file):
    img = load_img(file)
    coef = extract_rgb_coeff(img)
    image = img_from_dwt_coeff(coef)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)
    return image


def custom_dwt(image):
    a = running(image)

    return a


def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


def custom_dct(a):
    imF = dct2(a)
    im1 = idct2(imF)
    np.allclose(a, im1)
    return im1


def custom_dwt_dct(A):
    x = custom_dct(A)
    z = create_folder()
    comp_file = 'frame.jpg'
    path = os.path.join(z, comp_file)
    cv2.imwrite(path, x)
    y = custom_dwt(path)
    return y


def extractImages(pathIn, pathOut,x):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    success = True
    while success and x == "DWT":
        success, image = vidcap.read()
        if success == False:
            break
        z = create_folder()
        comp_file = 'frame.jpg'
        path = os.path.join(z, comp_file)
        cv2.imwrite(path, image)

        image = custom_dwt(path)

        image.save(pathOut + "\\%d.jpg" % count)     # save frame as JPEG file
        count += 1
    while success and x == "DCT":
        success, image = vidcap.read()
        if success == False:
            break

        image = custom_dct(image)

        cv2.imwrite(pathOut + "\\%d.jpg" %
                    count, image)     # save frame as JPEG file
        count += 1
    while success and x == "Hybrid DCT-DWT":
        success, image = vidcap.read()
        if success == False:
            break

        image = custom_dwt_dct(image)

        image.save(pathOut + "\\%d.jpg" % count)     # save frame as JPEG file
        count += 1
    st.write("Frame Breaking Completed,total frames=", count)

def empty_path(pathOut):
    for filename in os.listdir(pathOut):
        file_path = os.path.join(pathOut, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            
def video_compression(pathIn,type):
    path=create_folder()
    if not os.path.exists(path+"/V_frames"):
        os.makedirs(path+"/V_frames")
    path = os.path.join(path, 'V_frames')
    pathOut = path

    empty_path(pathOut)

    extractImages(pathIn, pathOut,type)
    pathx = path+"/"
    pathy = create_folder()
    pathOut=os.path.join(pathy,f"{type}_Output_video.mp4")
    #st.write(pathx,pathOut)
    cam = cv2.VideoCapture(pathIn)
    fps = frame_rate(cam)
    convert_frames_to_video(pathx, pathOut, fps)
    return pathOut
