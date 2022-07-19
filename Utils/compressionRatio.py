import os
from Utils.dataSet import add_row, check_cr
from Utils.psnrValue import send_path
import pandas as pd

#this function does all calculations regarding compression ratios and psnr values
def compression_ratio(st, pathIn, pathOut,type=""):
    #creting empty row for creating a dataset
    row=[]
    
    #adds file name to the array
    row.append(os.path.basename(pathIn))
    
    #get original size and add it to the array
    original_size = os.path.getsize(pathIn)
    row.append(float("{:.2f}".format(original_size/(1000*1000))))
    
    #get final size and add it to the array
    final_size = os.path.getsize(pathOut)
    row.append(float("{:.2f}".format(final_size/(1000*1000))))
    
    #diaplying everything in streamlit UI
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
    
    #calculate psnr
    value = send_path(pathIn, pathOut)
    st.subheader("PSNR:")
    st.write("Value :" + "{: .2f}".format(value)+" dB")
    
    #create a dataset or add a new row to exixting dataset
    path= add_row(row, type)
    
    #create a data frame of the existing dataset
    df = pd.read_csv(path)
    
    #to remove any empty rows in between te dataset
    df = df.dropna()
    st.header(f"{type} dataset")
    
    #display dataset on the UI
    st.write(df)
    
    #calculate average Compression ratio of the dataset
    cr=check_cr(path)
    cr=[float(i) for i in cr]
    cr1=sum((cr))/len(cr)
    st.write("Average Compression ratio:","{:.2f}".format(cr1))

   
    
