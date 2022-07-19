from EnchanmentAlgo.claheEnchancer import CLAHE
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.histogramEqualization import calculate_histogram
from Utils.psnrValue import send_path

#this is CLAHE and AHE helper file
def Clahe(st, pathO, pathE, ext):
    st.header("FOR CLAHE:")
    
    #calling CLAHE function from EnchanmentAlgo.claheEnchancer
    pathclahe = CLAHE(st, pathE, ext)
    st.subheader("Histogram for Original Image")
    
    #calcualting histogram
    calculate_histogram(st, pathO)
    st.subheader("Histogram for Clahe image")
    calculate_histogram(st, pathclahe)
    
    #calculating psnr
    v = send_path(pathO, pathclahe)
    st.subheader("PSNR:")
    
    #writing psnr values in streamlit UI
    st.write("Value :" + "{: .2f}".format(v)+" dB")
    

def ahe(st, pathO, pathE, ext):
    
    st.header("FOR AHE:")
    
    #calling CLAHE function from EnchanmentAlgo.aheEnchancer
    pathahe = AHE(st, pathE, ext)
    
    #calcualting histogram
    st.subheader("Histogram for original image")
    calculate_histogram(st, pathO)
    st.subheader("Histogram for Ahe image")
    calculate_histogram(st, pathahe)
    
    #calculating psnr
    v = send_path(pathO, pathahe)
    st.subheader("PSNR:")
    
    #writing psnr values in streamlit UI
    st.write("Value :" + "{: .2f}".format(v)+" dB")
    

#main function to call from other modules 
#this is the function you will call in order to run the attached above functions  
def enhacement(st, pathO, pathE, y, ext):
    if y == "CLAHE":
        Clahe(st,pathO,pathE,ext)
    if y == "AHE":
        ahe(st, pathO, pathE, ext)
        
    if y=="Both":
        Clahe(st, pathO, pathE, ext)
        ahe(st, pathO, pathE, ext)
