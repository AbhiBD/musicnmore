# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog, ttk  # Added ttk for Progressbar
import pygame.mixer as mixer         # pip install pygame
import os
from mutagen.mp3 import MP3           # pip install mutagen


# Initializing the mixer
mixer.init()

# Creating the master GUI
root = Tk()
root.geometry('700x250')  # Adjusted to make space for the progress bar
root.title('Music N More Music Player')
root.resizable(0, 0)
root.iconbitmap('C:/Class12/Computer/musicnmore/music.ico')

# Play, Stop, Load, and Pause & Resume functions
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")
    
     # Get total duration of the song using mutagen
    audio = MP3(songs_list.get(ACTIVE))
    total_duration = audio.info.length  # Duration in seconds
    progress_bar['maximum'] = total_duration  # Set the max value of the progress bar

    status.set("Song PLAYING")
    
    # Start the progress bar update
    update_progress_bar(total_duration)

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")
    progress_bar.stop()  # Stop the progress bar when the song is stopped

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = [track for track in os.listdir() if track.endswith(('.mp3', '.wav'))]
    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

# Function to update the progress bar
def update_progress_bar(total_duration):
    if mixer.music.get_busy():  # Check if the song is playing
        current_time = mixer.music.get_pos() // 1000  # Get current playback time in seconds

        # Update the progress bar value
        progress_bar['value'] = current_time

        # Continue updating every second if the current time is less than the total duration
        if current_time <= total_duration:
            root.after(1000, lambda: update_progress_bar(total_duration))
        else:
            progress_bar['value'] = total_duration  # Ensure it reaches the end when finished

# All the frames
song_frame = LabelFrame(root, text='Current Song', bg='#282A36', width=400, height=100, fg='#BD93F9')
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='#282A36', width=400, height=129, fg='#BD93F9')
button_frame.place(y=100)

listbox_frame = LabelFrame(root, text='Playlist', bg='#282A36', fg='#BD93F9')
listbox_frame.place(x=400, y=0, height=231, width=300)

# All StringVar variables
current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='#22242E')
scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)
playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='#1C1E26', font=('Times', 10,), fg='#50FA7B').place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=current_song, bg='#1C1E26', font=("Times", 12), width=25, fg='#50FA7B')
song_lbl.place(x=150, y=20)

# Adding a progress bar widget

s = ttk.Style()
s.theme_use('clam')
s.configure('Style.Horizontal.TProgressbar',background='#50FA7B',troughcolor='#282A36')

progress_bar = ttk.Progressbar(song_frame, orient="horizontal",style='Style.Horizontal.TProgressbar',length=350, mode="determinate")
progress_bar.place(x=20, y=50)

# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='#1C1E26', font=("Georgia", 13), width=7,
                    command=lambda: pause_song(song_status), fg='#50FA7B')
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='#1C1E26', font=("Georgia", 13), width=7,
                  command=lambda: stop_song(song_status), fg='#50FA7B')
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg='#1C1E26', font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, song_status), fg='#50FA7B')
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='#1C1E26', font=("Georgia", 13), width=7,
                    command=lambda: resume_song(song_status), fg='#50FA7B')
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='#1C1E26', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist), fg='#50FA7B')
load_btn.place(x=10, y=55)

# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='#282A36', font=('Times', 9, 'bold'), justify=LEFT, fg='#BD93F9').pack(side=BOTTOM, fill=X)

# Finalizing the GUI
root.update()
root.mainloop()
