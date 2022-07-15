from turtle import color
from EnchanmentAlgo.claheEnchancer import CLAHE
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.histogramEqualization import calculate_histogram
from Utils.psnrValue import send_path


def Clahe(st, pathO, pathE, ext):
    st.header("FOR CLAHE:")
    pathclahe = CLAHE(st, pathE, ext)
    st.subheader("Histogram for Original Image")
    calculate_histogram(st, pathO)
    st.subheader("Histogram for Clahe image")
    calculate_histogram(st, pathclahe)
    v = send_path(pathO, pathclahe)
    st.subheader("PSNR:")
    st.write("Value :" + "{: .2f}".format(v)+" dB")
    

def ahe(st, pathO, pathE, ext):
    
    st.header("FOR AHE:")
    pathahe = AHE(st, pathE, ext)
    st.subheader("Histogram for original image")
    calculate_histogram(st, pathO)
    st.subheader("Histogram for Ahe image")
    calculate_histogram(st, pathahe)
    v = send_path(pathO, pathahe)
    st.subheader("PSNR:")
    st.write("Value :" + "{: .2f}".format(v)+" dB")
    
    
def enhacement(st, pathO, pathE, y, ext):
    if y == "CLAHE":
        Clahe(st,pathO,pathE,ext)
    if y == "AHE":
        ahe(st, pathO, pathE, ext)
        
    if y=="Both":
        Clahe(st, pathO, pathE, ext)
        ahe(st, pathO, pathE, ext)
