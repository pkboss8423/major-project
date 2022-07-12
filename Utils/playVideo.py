from tkinter import *
from tkVideoPlayer import TkinterVideo


def play_video(path, type):

    window = Toplevel()
    window.title(f"{type}")
    window.geometry("1280x720")
    window.configure(bg="gray")

    def open_file(file):

        if file is not None:
            global filename
            filename = file
            global videoplayer
            videoplayer = TkinterVideo(master=window, scaled=True)
            videoplayer.load(r"{}".format(filename))
            videoplayer.pack(expand=True, fill="both")

            videoplayer.play()

    openbtn = Button(window, text='Play', command=lambda: open_file(path))

    openbtn.pack(side=TOP, pady=2)

    window.mainloop()
