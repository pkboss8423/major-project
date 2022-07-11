from EnchanmentAlgo.claheEnchancer import CLAHE
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.histogramEqualization import calculate_histogram
from Utils.psnrValue import send_path


def enhacement(st,pathO,pathE,y,ext):
    if y=="CLAHE":
        pathclahe = CLAHE(pathE, ext)
        st.write("Original Image")
        calculate_histogram(st,pathO)
        st.write("Histogram for Clahe image")
        calculate_histogram(st, pathclahe)
        v = send_path(pathO, pathclahe)
        st.write(f"PSNR value is {v} dB")
    if y=="AHE":
        pathahe = AHE(pathE, ext)
        st.write("Histogram for original image")
        calculate_histogram(st,pathO)
        st.write("Histogram for Ahe image")
        calculate_histogram(st, pathahe)
        v = send_path(pathO, pathahe)
        st.write(f"PSNR value is {v} dB")
