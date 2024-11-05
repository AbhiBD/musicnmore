# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog, ttk  # Added ttk for Progressbar
import pygame.mixer as mixer         # pip install pygame
import os
from mutagen.mp3 import MP3           # pip install mutagen

# Initializing the mixer
mixer.init()

absolute_path = os.path.dirname(__file__)
relative_path = "music.ico"
full_path = os.path.join(absolute_path, relative_path)

# Creating the master GUI
root = Tk()
root.geometry('700x250')  # Adjusted to make space for the progress bar
root.title('Music N More Music Player')
root.resizable(0, 0)
root.iconbitmap(full_path)

# Import necessary modules
from tkinter import *
from tkinter import filedialog, ttk  # Added ttk for Progressbar
import pygame.mixer as mixer         # pip install pygame
import os
from mutagen.mp3 import MP3           # pip install mutagen

# Initialize the mixer
mixer.init()

# Variables
current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')
current_after_id = None

# Global variable for the total duration of the song
total_duration = 0

# Play song function with progress bar update
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("Song PLAYING")

    # Get the total duration using mutagen
    audio = MP3(songs_list.get(ACTIVE))
    total_duration = audio.info.length  # Duration in seconds
    progress_bar['maximum'] = total_duration  # Set the max value of the progress bar

    # Start the progress bar update
    update_progress_bar(total_duration)

# Stop song function
def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")
    progress_bar.stop()  # Stop the progress bar when the song is stopped

# Seek function to set the playback to a specific time
def seek(position):
    global current_after_id
    mixer.music.play(start=position)
    progress_bar['value'] = position  # Update the progress bar to the new position

    # Cancel any previously scheduled update call
    if current_after_id:
        root.after_cancel(current_after_id)
        current_after_id = None

    # Restart the update loop from the new position
    update_progress_bar(progress_bar['maximum'], start_time=position)

# Update progress bar function to accept a start_time parameter
def update_progress_bar(total_duration, start_time=0):
    global current_after_id
    if mixer.music.get_busy():  # Check if the song is playing
        current_time = (mixer.music.get_pos() // 1000) + start_time  # Get current playback time in seconds

        if current_time > total_duration:
            current_time = total_duration  # Ensure it doesn't exceed the max

        progress_bar['value'] = current_time

        # Continue updating every second if the current time is less than the total duration
        if current_time <= total_duration:
            current_after_id = root.after(1000, lambda: update_progress_bar(total_duration, start_time))
        else:
            progress_bar['value'] = total_duration  # Ensure it reaches the end when finished

# Play, Stop, Load, and Pause & Resume functions

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
s.configure('Style.Horizontal.TProgressbar', background='#50FA7B', troughcolor='#282A36')

progress_bar = ttk.Progressbar(song_frame, orient="horizontal", style='Style.Horizontal.TProgressbar', length=350, mode="determinate")
progress_bar.place(x=20, y=50)

# Bind progress bar click for seeking
def on_progress_bar_click(event):
    total_duration = progress_bar['maximum']
    new_position = (event.x / progress_bar.winfo_width()) * total_duration
    seek(new_position)

progress_bar.bind("<Button-1>", on_progress_bar_click)

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
