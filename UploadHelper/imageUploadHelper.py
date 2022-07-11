from skimage.io import imread


def imageUpload(pathIn):
    instance = imread(pathIn)
    return instance
