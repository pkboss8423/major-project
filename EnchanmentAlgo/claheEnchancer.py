import os
import cv2
from Utils.createFolder import  create_image_folder
def CLAHE(st,pathIn, ext):
    
    #read image
    image = cv2.imread(pathIn, 0)
    
    # Resizing the image for compatibility
    image = cv2.resize(image, (1920, 1280))
    
    # apply histogram equalization
    final_img = cv2.equalizeHist(image)
    
    # The declaration of CLAHE
    # clipLimit -> Threshold for contrast limiting
    #clipLimit – This parameter sets the threshold for contrast limiting. The default value is 40.
    clahe = cv2.createCLAHE(clipLimit=5)
    final_img = clahe.apply(image) + 30
    
    # Ordinary thresholding the same image
    _, ordinary_img = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)
    
    #creating image folder
    x = create_image_folder()
    clahe_img = "clahe_img"+ext
    
    #creating image path
    path = os.path.join(x, clahe_img)
    
    #writing image
    cv2.imwrite(path, final_img)
    
    #displaying image on streamlit
    st.image(final_img, caption="CLAHE Enhancement", width=500)
    
    #returing path of the clahe image 
    return path
