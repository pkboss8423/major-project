import os

from Utils.psnrValue import send_path


# def writeToFile(data):
#     f = open("C:/Users/prakh/Downloads/output.txt", 'a')
#     f.write(data)
#     f.write('\n')


def compression_ratio(st,pathIn, pathOut, type=""):
    original_size = os.path.getsize(pathIn)
    final_size = os.path.getsize(pathOut)
    st.write(f"FOR {type}:")
    st.write("Original Size:", original_size)
    st.write("Final:", final_size)
    st.write("Compression ratio:", ((final_size/original_size)))
    value = send_path(pathIn, pathOut)
    st.write(f"PSNR value is {value} dB")
    # d = f"{type}-Original Size = " + str(original_size) + " Compression Size = " + str(
    #     final_size) + " Ratio = " + str(final_size/original_size)
    # writeToFile(d)
