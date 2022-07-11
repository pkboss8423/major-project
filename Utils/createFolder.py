import os
def create_folder():
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, 'Documents')
    if not os.path.exists(path+"/C_images"):
        os.makedirs(path+"/C_images")
    path = os.path.join(userprofile, 'Documents', 'C_images')
    return path
