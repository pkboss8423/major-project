import os

from Utils.psnrValue import send_path


# def writeToFile(data):
#     f = open("C:/Users/prakh/Downloads/output.txt", 'a')
#     f.write(data)
#     f.write('\n')


def compression_ratio(st, pathIn, pathOut, type=""):
    original_size = os.path.getsize(pathIn)
    final_size = os.path.getsize(pathOut)
    st.header(f"FOR {type}:")
    st.subheader("Original Size:")
    st.write("In kiloBytes:", "{:.2f}".format(original_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(original_size/(1000*1000)), "MB")
    st.subheader("Final Size:")
    st.write("In kiloBytes:", "{:.2f}".format(final_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(final_size/(1000*1000)), "MB")
    st.subheader("Compression ratio:")
    st.write("Ratio:","{: .2f}".format(
        (final_size/original_size)))
    value = send_path(pathIn, pathOut)
    st.subheader("PSNR:")
    st.write("Value :" + "{: .2f}".format(value)+" dB")
    # d = f"{type}-Original Size = " + str(original_size) + " Compression Size = " + str(
    #     final_size) + " Ratio = " + str(final_size/original_size)
    # writeToFile(d)
