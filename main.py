import tempfile
import cv2 as cv
import os
import streamlit as st
from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt
from CompressionAlgo.hybridImageCompression import custom_dwt_dct
from CompressionAlgo.videoCompression import video_compression
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.claheEnchancer import CLAHE
from Utils.compressionRatio import compression_ratio
from Utils.enhancement import enhacement
from Utils.extensionFinder import extension
from PIL import Image
from Utils.playVideo import play_video


from Utils.videoSize import get_size


def start_image(filePath, compressionTypes, EnhancementType):
    ext = extension(filePath)
    for compression in compressionTypes:
        if compression == "DCT":
            pathdct = custom_dct(st, filePath, ext)
            compression_ratio(st, filePath, pathdct, "DCT")
            enhacement(st, filePath, pathdct, EnhancementType, ext)
        if compression == "DWT":
            pathdwt = custom_dwt(st, filePath, ext)
            compression_ratio(st, filePath, pathdwt, "DWT")
            enhacement(st, filePath, pathdwt, EnhancementType, ext)
        if compression == "Hybrid DCT-DWT":
            pathdwt = custom_dwt_dct(st, filePath, ext)
            compression_ratio(st, filePath, pathdwt, "HYBRID DCT-DWT")
            enhacement(st, filePath, pathdwt, EnhancementType, ext)


st.title('Main project')

menu = ["image", "video"]
choice = st.sidebar.selectbox("select image or video for processing...", menu)


def save_uploaded_file(uploadedfile):
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, "Documents", uploadedfile.name)
    try:
        with open(os.path.join(userprofile, "Documents", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())
        return path
    except:
        print("Some Error")
        return ""


def run_video(path):
    video_file = open(path, 'rb')
    video_bytes = video_file.read()  # reading the file
    st.video(video_bytes)


def start_video(path, compressionTypes):
    if compressionTypes == "DCT":
        pathOut = video_compression(path, "DCT")
        #st.write(pathOut)
        #play_video(pathOut, "DCT")
        get_size(st, path, pathOut, "DCT")

    if compressionTypes == "DWT":
        pathOut = video_compression(path, "DWT")
        #play_video(pathOut, "DWT")
        get_size(st, path, pathOut, "DWT")
    if compressionTypes == "Hybrid DCT-DWT":
        pathOut = video_compression(path, "Hybrid DCT-DWT")
        #play_video(pathOut, "Hybrid DCT-DWT")
        get_size(st, path, pathOut, "Hybrid DCT-DWT")


if choice == 'image':
    st.title("image compression")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        file_details = {"Filename": image_file.name,
                        "FileType": image_file.type, "FileSize": (image_file.size)}
        st.write(file_details)
        path = save_uploaded_file(image_file)
        st.image(Image.open(path), caption="Original Image", width=500)
        Compression = st.multiselect(
            'Select Types of Compression Algorithms',
            ['DCT', 'DWT', 'Hybrid DCT-DWT'])
        Enhancers = st.radio(
            "Select Types of Enhancers Algorithms",
            ('AHE', 'CLAHE'))
        if st.button("Start"):
            start_image(path, Compression, Enhancers)
elif choice == 'video':
    st.title("video compression")
    f = st.file_uploader("Upload file")
    tfile = tempfile.NamedTemporaryFile(delete=False)
    if f is not None:
        # tfile.write(f.read())
        file_details = {"Filename": f.name,
                        "FileType": f.type, "FileSize": (f.size)}
        st.write(file_details)
        path = save_uploaded_file(f)
        run_video(path)

    Compression = st.radio(
        "Select Types of Compression Algorithms",
        ('DCT', 'DWT', 'Hybrid DCT-DWT'))

    if st.button("Start"):
        start_video(path, Compression)
