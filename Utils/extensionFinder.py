
#this function finds the extension of the input file
def extension(path):
    s=path.split("/")
    e=s[-1]
    return "."+str(e.split(".")[-1])