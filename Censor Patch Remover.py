from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
import re

def reset_widgets(button, label):
    label["text"] = check_file()
    if fileExists:
        button["text"] = "Remove Censor File"
        button["command"] = remove_file
    else:
        button["text"] = "Re-select directory"
        button["command"] = select_dir

def check_file():
    if os.path.exists(tempdir + filename):
        txt = "Censor file found"
        global fileExists
        fileExists = True
    else:
        txt = "Censor file not found"
    return txt

def remove_file():
    global tempdir, button
    os.remove(tempdir + filename)
    messagebox.showinfo("Done!", "ffbff2ac5b7a7948961212cefd4d402c has been removed")
    reset_widgets(button, label)

def select_dir():
    global tempdir, button, label
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select your pso2_bin directory')
    reset_widgets(button, label)
    
fileExists = False
filename="/data/win32/ffbff2ac5b7a7948961212cefd4d402c"
root = Tk()
root.title("Censor file remover")
root.geometry("300x50")
window = Frame(root)
window.grid()

currdir = os.getcwd()
messagebox.showinfo("Please Read", "Select your pso2_bin folder")
tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select your pso2_bin directory')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)

label = Label(window)
label.grid()
button = Button(window)
button.grid()

reset_widgets(button, label)

root.mainloop()
