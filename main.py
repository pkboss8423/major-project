from cProfile import run
import os
import streamlit as st
from CompressionAlgo.dctImageCompression import custom_dct
from CompressionAlgo.dwtImageCompression import custom_dwt
from CompressionAlgo.hybridImageCompression import custom_dwt_dct
from CompressionAlgo.videoCompression import video_compression
from Utils.compressionRatio import compression_ratio
from Utils.enhancement import enhacement
from Utils.extensionFinder import extension
from PIL import Image
from Utils.morphHelper import morph
from Utils.playVideo import run_video
from Utils.videoSize import get_size


def start_image(filePath, compressionTypes, EnhancementType, Morp_op):
    ext = extension(filePath)
    for compression in compressionTypes:
        if compression == "DCT":
            pathdct = custom_dct(st, filePath, ext)
            compression_ratio(st, filePath, pathdct,  "DCT")
            if EnhancementType != "None":
                enhacement(st, filePath, pathdct, EnhancementType, ext)
            morph(pathdct, Morp_op)
        if compression == "DWT":
            pathdwt = custom_dwt(st, filePath, ext)
            compression_ratio(st, filePath, pathdwt, "DWT",)
            if EnhancementType != "None":
                enhacement(st, filePath, pathdwt, EnhancementType, ext)
            morph(pathdwt, Morp_op)
        if compression == "Hybrid DCT-DWT":
            pathdwt = custom_dwt_dct(st, filePath, ext)
            compression_ratio(st, filePath, pathdwt, "HYBRID DCT-DWT")
            if EnhancementType != "None":
                enhacement(st, filePath, pathdwt, EnhancementType, ext)
            morph(pathdwt, Morp_op)


st.title('HOWDY!')

# creating UI menu
menu = ["image", "video"]
choice = st.sidebar.selectbox("select image or video for processing...", menu)

# this function saves the path of uploaded file


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


def start_video(path, compressionTypes):
    if compressionTypes == "DCT":
        pathOut, pathnew = video_compression(path, "DCT")
        run_video(st, pathnew)
        get_size(st, path, pathOut, "DCT")
    if compressionTypes == "DWT":
        pathOut, pathnew = video_compression(path, "DWT")
        run_video(st, pathnew)
        get_size(st, path, pathOut, "DWT")
    if compressionTypes == "Hybrid DCT-DWT":
        pathOut, pathnew = video_compression(path, "Hybrid DCT-DWT")
        run_video(st, pathnew)
        get_size(st, path, pathOut, "Hybrid DCT-DWT")


# starting code for image
if choice == 'image':
    st.title("image compression")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        file_details = {"Filename": image_file.name,
                        "FileType": image_file.type, "FileSize": (image_file.size)}
        st.write(file_details)
        path = save_uploaded_file(image_file)
        st.image(Image.open(path), caption="Original Image", width=500)

        # creating and array of compression algorithms based on user input
        Compression = st.multiselect(
            'Select Types of Compression Algorithms',
            ['DCT', 'DWT', 'Hybrid DCT-DWT'])

        # creating radio buttons for enhacement algorithms
        Enhancers = st.radio(
            "Select Type of Enhancers Algorithms",
            ('AHE', 'CLAHE', 'Both', 'None'), index=3)
        st.write(
            "Note:  We recommend to use morphological operations only for medical images.")
        # creating an array for morphological operations
        Morphological_operations = st.multiselect(
            "Select Type of Morphological operation",
            ['Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient',  "None"])
        if st.button("Start"):
            start_image(path, Compression, Enhancers, Morphological_operations)

# starting code for video
elif choice == 'video':
    st.title("video compression")
    f = st.file_uploader("Upload file (Please select Minimum size of 10mb)")

    if f is not None:
        file_details = {"Filename": f.name,
                        "FileType": f.type, "FileSize": (f.size)}
        st.write(file_details)
        path = save_uploaded_file(f)
        run_video(st, path)

    Compression = st.radio(
        "Select Types of Compression Algorithms",
        ('DCT', 'DWT', 'Hybrid DCT-DWT'))

    if st.button("Start"):
        start_video(path, Compression)
