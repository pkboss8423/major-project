import cv2
import matplotlib.pylab as plt
import streamlit as st


def erosion(image):
    st.header("Erosion:")
    for i in range(0, 3):
        eroded = cv2.erode(image.copy(), None, iterations=i + 1)
        st.image(eroded, caption="Eroded {} times".format(i + 1))


def dilation(image):
    st.header("Dilation:")
    # apply a series of dilations
    for i in range(0, 3):
        dilated = cv2.dilate(image.copy(), None, iterations=i + 1)
        st.image(dilated, caption="Dilated {} times".format(i + 1))


def opening(image):
    st.header("Opening:")
    kernelSizes = [(3, 3), (5, 5), (7, 7), (9, 9), (11, 11)]
    # loop over the kernels sizes
    for kernelSize in kernelSizes:
        # construct a rectangular kernel from the current size and then
        # apply an "opening" operation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        st.image(opening, caption="Opening: ({}, {})".format(
            kernelSize[0], kernelSize[1]))


def closing(image):
    st.header("Closing:")
    kernelSizes = [(3, 3), (5, 5), (7, 7), (9, 9), (11, 11)]
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        st.image(closing, caption="Closing: ({}, {})".format(
            kernelSize[0], kernelSize[1]))


def morphological_gradient(image):
    st.header("Gradient:")
    kernelSizes = [(3, 3), (5, 5), (7, 7), (9, 9), (11, 11)]
    # loop over the kernels a final time
    for kernelSize in kernelSizes:
        # construct a rectangular kernel and apply a "morphological
        # gradient" operation to the image
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
        st.image(gradient, caption="Gradient: ({}, {})".format(
            kernelSize[0], kernelSize[1]))



