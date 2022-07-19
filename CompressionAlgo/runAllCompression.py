from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt
from CompressionAlgo.hybridImageCompression import custom_dwt_dct
from Utils.compressionRatio import compression_ratio

#this file not in use
def run_all(pathIn, ext):
    a = custom_dct(pathIn, ext)
    compression_ratio(pathIn, a, "DCT")
    b = custom_dwt(pathIn, ext)
    compression_ratio(pathIn, b, "DWT")
    c = custom_dwt_dct(pathIn, ext)
    compression_ratio(pathIn, c, "HYBRID DCT-DWT")
    return c
