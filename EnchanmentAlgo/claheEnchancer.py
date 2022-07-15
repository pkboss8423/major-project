import os
import cv2
from Utils.createFolder import  create_image_folder
#from PIL import Image


def CLAHE(st,pathIn, ext):
    image = cv2.imread(pathIn, 0)

    image = cv2.resize(image, (1920, 1280))
    clahe = cv2.createCLAHE(clipLimit=5)
    final_img = clahe.apply(image) + 30
    _, ordinary_img = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)

    x = create_image_folder()
    clahe_img = "clahe_img"+ext
    path = os.path.join(x, clahe_img)
    cv2.imwrite(path, final_img)
    # img = Image.open(path)
    st.image(final_img, caption="CLAHE Enhancement", width=500)
    # print(path)
    return path
