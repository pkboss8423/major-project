from EnchanmentAlgo.morphologicaloperations import *
from UploadHelper.imageUploadHelper import image_Read


def morph(path,types):
    
    # read image and covert rgb to bgr
    image = image_Read(path)
    
    #types is an array
    if "None" in types:
        return
    elif len(types)==0:
        return
    else:
        st.header("Morphological Operations:")
        for y in types:
            
            if y=="Erosion":
                
                erosion(image)
            if y == "Dilation":
                dilation(image)
            if y == "Opening":
                opening(image)
            if y == "Closing":
                closing(image)
            if y == "Gradient":
                morphological_gradient(image)
            if y == "Blackhat_tophat":
                blackhat_tophat(image)
    
        
    
    