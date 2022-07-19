import os

#this functions prints the video sizes
def get_size(st,pathIn,pathOut,type):
    original_size = os.path.getsize(pathIn)
    final_size = os.path.getsize(pathOut)
    st.header(f"FOR {type}:")
    st.subheader("Original Size:")
    st.write("In kiloBytes:", "{:.2f}".format(original_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(original_size/(1000*1000)), "MB")
    st.subheader("Final Size:")
    st.write("In kiloBytes:", "{:.2f}".format(final_size/1000), "KB")
    st.write("In megaBytes:", "{:.2f}".format(final_size/(1000*1000)), "MB")
