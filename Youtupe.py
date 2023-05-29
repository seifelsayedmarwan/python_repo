from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Youtube downloader by king of python")

Label(root, text="Youtube downloader", font="arial 20 bold").pack()

link = StringVar()

Label(root, text="Paste link here:", font="arial 15 bold").place(x = 160, y = 60)
link_enter = Entry(root, width=70, textvariable= link).place(x = 32, y = 90)

def high():
    
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text="DOWNLOAD!", font="arial 15 bold").place(x = 180, y = 210)

Button(root, text="High resulotion", font= "arial 15 bold",bg="yellow", padx = 2, command=high).place(x = 180, y = 150)

def low():
    
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text="DOWNLOAD!", font="arial 15 bold").place(x = 180, y = 210)

Button(root, text="Low resulotion", font= "arial 15 bold",bg="red", padx = 2, command=low).place(x = 110, y = 200)


def audio_only():
    
    url = YouTube(str(link.get()))
    video = url.streams.get_audio_only()
    video.download()
    Label(root, text="DOWNLOAD!", font="arial 15 bold").place(x = 180, y = 210)

Button(root, text="Audio only", font= "arial 15 bold",bg="light blue", padx = 2, command=audio_only).place(x = 280, y = 200)


root.mainloop()