from EnchanmentAlgo.claheEnchancer import CLAHE
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.histogramEqualization import calculate_histogram
from Utils.psnrValue import send_path


def enhacement(st, pathO, pathE, y, ext):
    if y == "CLAHE":
        pathclahe = CLAHE(st, pathE, ext)
        st.subheader("Original Image")
        calculate_histogram(st, pathO)
        st.subheader("Histogram for Clahe image")
        calculate_histogram(st, pathclahe)
        v = send_path(pathO, pathclahe)
        st.subheader("PSNR:")
        st.write("Value :" + "{: .2f}".format(v)+" dB")
    if y == "AHE":
        pathahe = AHE(st, pathE, ext)
        st.subheader("Histogram for original image")
        calculate_histogram(st, pathO)
        st.subheader("Histogram for Ahe image")
        calculate_histogram(st, pathahe)
        v = send_path(pathO, pathahe)
        st.subheader("PSNR:")
        st.write("Value :" + "{: .2f}".format(v)+" dB")
