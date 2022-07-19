
#plays the video on streamlit UI
def run_video(st,path):
    video_file = open(path, 'rb')
    video_bytes = video_file.read()  # reading the file
    st.video(video_bytes)
