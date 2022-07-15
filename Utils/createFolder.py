import os

#this file makes the folder structure for the output files for windows system

def create_major_folder():
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, 'Downloads')
    if not os.path.exists(path+"/Major_Project"):
        os.makedirs(path+"/Major_Project")
    path = os.path.join(userprofile, 'Downloads', 'Major_Project')
    return path


def create_image_folder():
    
    path = create_major_folder()
    if not os.path.exists(path+"/Compressed_images"):
        os.makedirs(path+"/Compressed_images")
    path = os.path.join(path, 'Compressed_images')
    return path


def create_video_folder():
    
    path = create_major_folder()
    if not os.path.exists(path+"/Compressed_videos"):
        os.makedirs(path+"/Compressed_videos")
    path = os.path.join(path, "Compressed_videos")
    return path


def create_video_frames():
    userprofile = os.environ['USERPROFILE']
    path = create_video_folder()
    if not os.path.exists(path+"/Video_frames"):
        os.makedirs(path+"/Video_frames")
    path = os.path.join(path, 'Video_frames')
    return path


def create_data_sets():
    
    path = create_major_folder()
    if not os.path.exists(path+"/Data_sets"):
        os.makedirs(path+"/Data_sets")
    path = os.path.join(path, 'Data_sets')
    return path
