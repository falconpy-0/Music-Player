from tkinter import *
from PIL import Image, ImageTk
import pygame
from pygame import mixer

window = Tk()
window.geometry("700x840")
window.config(bg="#1E1E1E")
pygame.init()
mixer.init()

# --- SONGS DATA ---
Songs = [
    {
        "title": "Limerence",
        "artist": "Limerence - Yves Tumor",
        "file": "C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\playlist\\Yves Tumor - Limerence Official Audio.mp3",
        "cover": "C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\cover.png"
    },

    {
        "title": "Judas",
        "artist": "Judas - Lady Gaga",
        "file": "C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\playlist\\Lady Gaga - Judas Lyrics.mp3",
        "cover": "C:\\Users\\LENOVO\\Downloads\\judascover2.png"
    },

    {
        "title": "Good Day",
        "artist": "It Was A Good Day - Ice Cube",
        "file": "C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\playlist\\ice cube - it was a good day slowed.mp3",
        "cover": "C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\ice cube.png"
    }

]

# --- VARIABLES ---
current_index = 0
is_playing = False

# --- LOAD COVER IMAGES ---
covers = [ImageTk.PhotoImage(Image.open(song["cover"])) for song in Songs]

# --- FUNCTIONS ---
def play_pause():
    global is_playing
    if not is_playing:
        mixer.music.unpause()
        play_pause_button.configure(image=pause_img)
        is_playing = True
    else:
        mixer.music.pause()
        play_pause_button.configure(image=play_img)
        is_playing = False

def load_song(index):
    song = Songs[index]
    mixer.music.load(song["file"])
    mixer.music.play()
    play_pause_button.configure(image=pause_img)
    update_ui()
    global is_playing
    is_playing = True

def next_song():
    global current_index
    current_index = (current_index + 1) % len(Songs)
    load_song(current_index)

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(Songs)
    load_song(current_index)

def update_ui():
    song = Songs[current_index]
    playing.config(text=song["title"])
    info.config(text=song["artist"])
    cover_album.config(image=covers[current_index])
    cover_album.image = covers[current_index]

def volume_control(x):
    mixer.music.set_volume(int(x) / 100)

# --- UI COMPONENTS ---

# Background frame
mainbox_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\mainbox786.png")
mainbox = Label(window, image=mainbox_img, borderwidth=0, bg="#1E1E1E")
mainbox.place(x=149, y=33)

# Album Cover
cover_album = Label(mainbox, bg="#A74200", image=covers[current_index])
cover_album.place(x=48, y=60)

# Play / Pause Button
pause_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\pause (1).png")
play_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\play.png")
play_pause_button = Button(window, image=play_img, bg="#1E1E1E", command=play_pause, activebackground="#1E1E1E", borderwidth=0)
play_pause_button.place(x=309, y=697)

# Next / Prev Buttons
next_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\next.png")
prev_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\previous.png")
next_button = Button(window, image=next_img, bg="#1E1E1E", command=next_song, activebackground="#1E1E1E", borderwidth=0)
prev_button = Button(window, image=prev_img, bg="#1E1E1E", command=previous_song, activebackground="#1E1E1E", borderwidth=0)
next_button.place(x=450, y=696)
prev_button.place(x=165, y=697)

# Bookmark / Music Icon
bookmark_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\bookmark.png")
musicicon_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\musicicon.png")
bookmark_button = Button(window, image=bookmark_img, bg="#1E1E1E", activebackground="#1E1E1E", borderwidth=0)
musicicon_button = Button(window, image=musicicon_img, bg="#1E1E1E", activebackground="#1E1E1E", borderwidth=0)
bookmark_button.place(x=502, y=533)
musicicon_button.place(x=165, y=531)

# Volume Icon
volumn_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Music Player App\\assets\\volume.png")
volumn_button = Button(window, image=volumn_img, bg="#1E1E1E", activebackground="#1E1E1E", borderwidth=0)
volumn_button.place(x=46, y=474)

# Song Title and Artist
playing = Label(window, text=Songs[0]["title"], font=("Krona One", 32, "bold"), fg="#CCCCCC", bg="#1E1E1E")
info = Label(window, text=Songs[0]["artist"], font=("Krona One", 16, "bold"), fg="#999999", bg="#1E1E1E")
playing.place(x=230, y=523)
info.place(x=235, y=567)

# Volume Slider
Volumn_bar = Scale(window, from_=100, to=0, orient=VERTICAL, width=13, bg="#1E1E1E", fg="#CCCCCC",
                   troughcolor="#999999", highlightthickness=0, borderwidth=0, showvalue=0,
                   length=429, sliderlength=10, command=volume_control)
Volumn_bar.set(50)
Volumn_bar.place(x=63, y=33)

# Start with first song loaded
load_song(current_index)

window.mainloop()
