import cv2


def videoUpload(pathIn):
    instance = cv2.VideoCapture(pathIn)
    return instance
