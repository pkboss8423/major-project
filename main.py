import os
import streamlit as st
from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt
from CompressionAlgo.hybridImageCompression import custom_dwt_dct
from EnchanmentAlgo.aheEnchancer import AHE
from EnchanmentAlgo.claheEnchancer import CLAHE
from Utils.compressionRatio import compression_ratio
from Utils.enhancement import enhacement
from Utils.extensionFinder import extension
from PIL import Image
def start_image(filePath,compressionTypes,EnhancementType):
    ext=extension(filePath)
    for compression in compressionTypes:
        if compression == "DCT":
            pathdct=custom_dct(st,filePath,ext)
            compression_ratio(st,filePath, pathdct, "DCT")
            enhacement(st,filePath,pathdct,EnhancementType,ext)
        if compression == "DWT":
            pathdwt = custom_dwt(st,filePath, ext)
            compression_ratio(st, filePath, pathdwt, "DWT")
            enhacement(st, filePath, pathdwt, EnhancementType, ext)
        if compression == "Hybrid DCT-DWT":
            pathdwt = custom_dwt_dct(st,filePath, ext)
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


if choice == 'image':
    st.title("image compression")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        file_details = {"Filename": image_file.name,
                        "FileType": image_file.type, "FileSize": (image_file.size)}
        st.write(file_details)
        path = save_uploaded_file(image_file)
        st.image(Image.open(path),caption="Original Image",width=500)
        Compression = st.multiselect(
            'Select Types of Compression Algorithms',
            ['DCT', 'DWT', 'Hybrid DCT-DWT'])
        Enhancers=st.radio(
            "Select Types of Enhancers Algorithms",
            ('AHE', 'CLAHE'))
        if st.button("Start"):
            start_image(path,Compression,Enhancers)
elif choice == 'video':
    st.title("video compression")
    video_file = open('FILENAME', 'rb')  # enter the filename with filepath

    video_bytes = video_file.read()  # reading the file

    st.video(video_bytes)  # displaying the video
        
    