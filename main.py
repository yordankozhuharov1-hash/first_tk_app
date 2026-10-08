from tkinter import *
from tkinter import filedialog
import os
import subprocess as su
from datetime import datetime

window = Tk()
window.title("Notification Sound on click ")
window.minsize(width=500, height=300)  # Set the minimum size of the window

my_label = Label(text="Click the button to start the sound", font=("Arial", 24))
my_label.pack(side="top")

def button_clicked():
    os.system("start C:\\Users\\a1bg546125\\Downloads\\day-27\\mixkit-correct-answer-tone-2870.wav")
def exit_button_clicked():
    window.destroy()
    os.system("taskkill /f /im Microsoft.Media.Player.exe")  # Example to stop Windows Media Player if it's playing the sound
button_for_sound = Button(text="Click Me", command=button_clicked)
button_for_sound.pack()
date = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%H:%M:%S")

def logging():
    with open("log.txt", "a") as log_file:
        log_file.write(f"Exit button clicked on {date} - {time}\n")

exit_button = Button(text="Exit", command=lambda: [exit_button_clicked(), logging()])
exit_button.pack()
window.mainloop()