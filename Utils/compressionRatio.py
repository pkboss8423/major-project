import os
from Utils.dataSet import add_row, check_cr

from Utils.psnrValue import send_path
import pandas as pd


def compression_ratio(st, pathIn, pathOut,type=""):
    row=[]
    row.append(os.path.basename(pathIn))
    original_size = os.path.getsize(pathIn)
    row.append(float("{:.2f}".format(original_size/(1000*1000))))
    final_size = os.path.getsize(pathOut)
    row.append(float("{:.2f}".format(final_size/(1000*1000))))
    st.header(f"FOR {type}:")
    st.subheader("Original Size:")
    st.write("In kiloBytes:", "{:.2f}".format(original_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(original_size/(1000*1000)), "MB")
    st.subheader("Final Size:")
    st.write("In kiloBytes:", "{:.2f}".format(final_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(final_size/(1000*1000)), "MB")
    st.subheader("Compression ratio:")
    cr = float("{:.2f}".format(final_size/original_size))
    row.append(cr)
    st.write("Ratio:","{: .2f}".format(
        (final_size/original_size)))
    value = send_path(pathIn, pathOut)
    st.subheader("PSNR:")
    st.write("Value :" + "{: .2f}".format(value)+" dB")
    
    
    path= add_row(row, type)

    df = pd.read_csv(path)
    df = df.dropna()
    st.header(f"{type} dataset")
    st.write(df)
    cr=check_cr(path)
    cr=[float(i) for i in cr]
    cr1=sum((cr))/len(cr)
    st.write("Average Compression ratio:","{:.2f}".format(cr1))

   
    
