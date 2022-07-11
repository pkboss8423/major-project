from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt


def custom_dwt_dct(st,pathIn, ext):
    dct_path = custom_dct(st,pathIn, ext, hybrid=True)
    dwt_path = custom_dwt(st,dct_path, ext,hybrid=True)

    return dwt_path
    