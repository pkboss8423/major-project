from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt


def custom_dwt_dct(pathIn, ext):
    dct_path = custom_dct(pathIn, ext, hybrid=True)
    dwt_path = custom_dwt(dct_path, ext)

    return dwt_path
    