from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

window=Tk()
window.title("Music Player by Panos")
window.geometry("920x670+100+100")
window.configure(bg="Dark Blue")
window.resizable(False,False)

mixer.init()
pausecheck=0

def open_folder():
    global songs
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
def stop():
    global pausecheck
    mixer.music.stop()
    music.config(text="")
    pausecheck=0
def pause():
    global pausecheck
    mixer.music.pause()
    if "||" not in music.cget("text"):
        music.config(text=(" || "+music.cget("text")))
    pausecheck=1
def play_song():
    global pausecheck
    if pausecheck==1:
        mixer.music.unpause()
        playing=music.cget("text")
        music.config(text=playing.replace("||",''))
        pausecheck=0
    else:
        music_name = playlist.get(ACTIVE)
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()
        music.config(text=music_name[0:-4])
#images
img1=PhotoImage(file="Images/logo.png")
img1Label=Label(window,image=img1)
img1Label.place(x=60,y=150)
#buttons
    #play
playL=Label(window,text="Play",font="Verdana 10 bold",fg="White",bg="Dark Blue")
playL.place(x=60,y=380)
playimg=PhotoImage(file="Images/play.png")
playimgB=Button(window,image=playimg,command=play_song) 
playimgB.place(x=30,y=400)
    #pause
pauseL=Label(window,text="Pause",font="Verdana 10 bold",fg="White",bg="Dark Blue")
pauseL.place(x=230,y=380)
pauseimg=PhotoImage(file="Images/pause.png")
pauseimgB=Button(window,image=pauseimg,command=pause)
pauseimgB.place(x=210,y=400)
    #stop
stopL=Label(window,text="Stop",font="Verdana 10 bold",fg="White",bg="Dark Blue")
stopL.place(x=140,y=380)
stopimg=PhotoImage(file="Images/stop.png")
stopimgB=Button(window,image=stopimg,command=stop)
stopimgB.place(x=120,y=400)
#music
musicframe=Frame(window,bd=2)
musicframe.place(x=330,y=350,height=250,width=550)
openbutton=Button(window,text="Open folder",width=10,height=2,font="Verdana 15",bg="purple",fg="white",borderwidth=0,command=open_folder) 
openbutton.place(x=330,y=280)
#scrollbar
scroll=Scrollbar(musicframe)
playlist=Listbox(musicframe,width=100,bd=0,bg="Gray",fg="Black",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=Y)
#music label
currently=Label(window,text="Currently playing:",font="Verdana 10",bg="Dark Blue",fg="White")
currently.place(x=330,y=150)
music=Label(window,text="",bg="Dark Blue",font="Verdana 25",fg="White")
music.place(x=330,y=200)

window.mainloop()