import cv2
import numpy as np

#this file calculates PSNR values
def PSNR(img1, img2):
    psnr = cv2.PSNR(img1, img2)
    return psnr


def send_path(pathIn, pathOut):
    original = cv2.imread(pathIn)
    compressed = cv2.imread(pathOut)
    original = cv2.resize(original, (500, 600))
    compressed = cv2.resize(compressed, (500, 600))
    value = PSNR(original, compressed)

    return value
