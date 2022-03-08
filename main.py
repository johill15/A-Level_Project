import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("Music Player")
music_player.geometry("500x550")

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
# make a list that only lists possible values (mp3, wav, ogg)
playlist = tkr.Listbox(music_player, font = "Verdana 12 bold",
                       fg = "white", bg = "black", selectmode = tkr.SINGLE)
print (playlist)
x = 0
for i in song_list:
    playlist.insert(x,i)
    x += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer_music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer_music.play()

def stop():
    pygame.mixer_music.stop()

def pause():
    pygame.mixer_music.pause()

def unpause():
    pygame.mixer_music.unpause()

def volumeup():
    pygame.mixer_music.set_volume(1)

def volumedown():
    pygame.mixer_music.set_volume(0.5)



Button1 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "PLAY",
                     command = play, bg = "grey", fg = "white")
Button2 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "STOP",
                     command = stop, bg = "grey", fg = "white")
Button3 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "PAUSE",
                     command = pause, bg = "grey", fg = "white")
Button4 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "UNPAUSE",
                     command = unpause, bg = "grey", fg = "white")
Button5 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "VOLUME UP",
                     command = volumeup, bg = "grey", fg = "white")
Button6 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Verdana 12 bold", text = "VOLUME DOWN",
                     command = volumedown, bg = "grey", fg = "white")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font = "Verdana 12 bold", textvariable = var)

song_title.pack()
Button1.pack(fill = "x")
Button2.pack(fill = "x")
Button3.pack(fill = "x")
Button4.pack(fill = "x")
Button5.pack(fill = "x")
Button6.pack(fill = "x")
playlist.pack(fill = "both", expand = "yes")

music_player.mainloop()

