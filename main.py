# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        # pip install pygame
import os

# Initializing the mixer
mixer.init()

# Creating the master GUI
root = Tk()
root.geometry('700x220')
root.title('Music N More Music Player')
root.resizable(0, 0)
root.iconbitmap('C:/Class12/Computer/musicnmore/music.ico')

"""
 
Tk() assignment will be used to initialize the window.

title() and .geometry() will be used to specify the title and initial geometry of the GUI window of music player.
resizable() method is used to permit/forbid the user from being able to resize the window. This method takes the arguments in the form of (height, width) ; the default for both of these are True but you can change it 0 or False to forbid the user from resizing the window.
update() and mainloop() methods are used to put the window on loop and stop it from closing the moment it opens.
Note: The line of code where the .mainloop() is written will be the last line that will be executed that updates the main window. Line 180

"""

# Play, Stop, Load and Pause & Resume functions
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")


def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

"""
In the load function, we will ask the user for a directory that has the audio files and then insert all the files in python music player as values in the ListBox widget we will provide as an argument to the function.
The os.chdir() command is used to change the current working directory to the specified path.
The tkinter.filedialog.askdirectory() method is used to request a directory from the user.
The os.listdir() command is used to list all the files in the current working directory in the form of a list.
The .insert() function, that takes the index, and *elements arguments, is used to insert new element(s) to the Listbox widget on the index parameter.
The play function, which loads and plays a file, requires 3 arguments: 2 StringVar objects and a ListBox object where the StringVar objects manipulate the text in the Labels that display the current song and its status:
Firstly, we set the song_name argument to the name of the song by getting the selected option from the ListBox object and set the status to “Playing”.
The .set() method of a StringVar class changes the value of the StringVar object.
The .get() method of the ListBox class is used to get certain values from the object. When ACTIVE is provided as an argument to it, it gives you the selected value in the object.
The stop(), pause() and resume() functions are all provided with only one StringVar object as argument, use their respective functions and set the StringVar object to their corresponding status.

"""


# All the frames
song_frame = LabelFrame(root, text='Current Song', bg='#282A36', width=400, height=80,fg='#BD93F9')
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='#282A36', width=400, height=120,fg='#BD93F9')
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='#282A36',fg='#BD93F9')
listbox_frame.place(x=400, y=0, height=200, width=300)

# All StringVar variables
current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

"""

A LabelFrame is a container in Python Tkinter GUIs that acts as a container for different window layouts.
The master parameter is the parent window it is associated with.
The text parameter is the text that will be displayed on the frame.
The width, height parameters are used to specify the width and height of the widget.
The bg parameter specifies the background color.
The StringVar class is used to manipulate and edit text in Labels, Entry widgets, and OptionMenus.
The value parameter denotes the initial value of the widget. Default is ”.
The master parameter is the same as in LabelFrames.
The .pack() method is one of the 3 Tkinter geometry manager methods that is used to position a widget in its parent using abscissa and ordinate points as though the parent widget/window is a Cartesian Plane. The default is (0, 0) , which is also the North West corner of the parent widget/window.
The x, y parameters denote the horizontal and vertical offsets of the widget this method is associated with.

"""

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

"""
Now that all the LabelFrame objects have been defined, let us place all the components in them.
Horizontal and vertical offsets of the widgets, using the .place() method have to be according to their parent widget, not the master window.
In the playlist LabelFrame we will define a Listbox with a Scrollbar packed to it.
The ListBox class is used to add a Listbox widget on the window, which displays multiple values in different lines to choose from.
master and font parameters have the same description as in the other widgets.
selectbackground parameter defines the color of the background when a value is selected.
selectmode parameter specifies how many values can be selected at once. Default is ‘browse’ for single selection, and other options include ‘multiple’ and ‘extended’ that allow multiple selection.
config() method is used to configure some other parameters to the widget it is associated with.
yscrollcommand parameter defines the Scrollbar object that will be associated with the widget. Similarly, the xscrollcommand defines the vertical Scrollbar.
The ScrollBar class is used to add a Scrollbar to the music player window.
master parameter and .command() and .config() method have the same description as in the other widgets.
orient parameter defines whether the Scrollbar will control the widget vertically, or horizontally.
set() method is used to set the Scrollbar to another widget.
In the current_song LabelFrame, we will define 2 Labels; one with a constant text and the other with variable text.
The Label widget is used to display static text on its parent widget.
master, width and bg are the same as they are in the Label widget.
font parameter is used to designate the font family and font effects of the text on the widget.
textvariable parameter is a Tkinter variable that will automatically update the value in the widget when the argument provided is updated.
In the control_panel LabelFrame, we will define the buttons whose commands we defined in the last-to-last step.
The Button class is used to add a button to the GUI application that executes a command when it is pressed.
master, text, bg, font and width parameters have the same description as in the other widgets.
command parameter is used to define the command the button will execute when it is pressed. It may be a statement, function with or without arguments. The functions without arguments can be executed without anything extra, but you need to use the lambda: keyword to assign functions with arguments.
The .pack() method, another Tkinter geometry manager method, is used to pack a widget as though the master window or the parent widget was a spreadsheet, in the form of rows and columns.
The side parameter of the .pack() method is used to specify where the widget will be placed on the parent widget or the master window.
The fill parameter defines whether the widget will fill the horizontal (X has to be provided as argument) or the vertical (Y has to be provided as argument) parts of the parent widget/window or the entire parent (BOTH has to be provided as argument).
The padx, pady parameters define how many pixels to leave between the widget and the nearby borders (horizontal, vertical).

"""

# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='#282A36', font=('Times', 9,'bold'), justify=LEFT,fg='#BD93F9').pack(side=BOTTOM, fill=X)

# Finalizing the GUI
root.update()
root.mainloop()
