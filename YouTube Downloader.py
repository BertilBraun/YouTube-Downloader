from pytube import YouTube

from tkinter import *
import os
import time

Lb1 = None
video = None


def Download():

    global video
    global Lb1

    if Lb1 is None or video is None:
        print("is none")
        return
        
    value = Lb1.get(int(Lb1.curselection()[0]))
    
    for stream in video.streams.filter(file_extension = "mp4"):
    
        tokens = value.split(' ')
        if str(stream.resolution) == tokens[0] and str(stream.fps) == tokens[1]:
        
            stream.download()
            L2 = Label(top, text = "Downloaded!")
            L2.pack()
            return
            
def URL_entered():

    global video
    global Lb1

    video = YouTube(E1.get())

    res_fps_set = []
    
    for stream in video.streams.filter(file_extension = "mp4"):
        
        if (stream.resolution, stream.fps) not in res_fps_set and stream.resolution != None:
            res_fps_set.append((stream.resolution, stream.fps))
        
    Lb1 = Listbox(top)
        
    res_fps_set.sort(key = lambda x : int(x[0][:-1]), reverse = True)
    for i, (res, fps) in enumerate(res_fps_set):
        Lb1.insert(i, str(res) + " " + str(fps))
        
    Lb1.pack()
    
    B2 = Button(top, text ="Download", command = Download)
    B2.pack()


top = Tk()

L1 = Label(top, text="URL")
L1.pack()
E1 = Entry(top, bd =5)
E1.insert(0, "https://www.youtube.com/watch?v=A7wmkBRNptg")
E1.pack()

B1 = Button(top, text ="Submit", command = URL_entered)
B1.pack()
    

top.mainloop()
