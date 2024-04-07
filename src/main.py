import os, winshell
import sys
from win32com.client import Dispatch
import tkinter as tk
from tkinter import filedialog,  messagebox
from pathlib import Path

root = tk.Tk()
root.withdraw()


#Getting the icon from the data folder
cpath = Path(sys.argv[0]).resolve().parent
icopath = str(cpath.parent / "data" / "icon.ico")


#Assigning it to the tkinter filedialog
root.iconbitmap(icopath)


#Selecting the folder we want to create a workspace from, and where to save this workspace file
folder_path = filedialog.askdirectory(
    initialdir="/",
    title="Select workspace folder"
)
save_location = filedialog.askdirectory(
    initialdir="/",
    title="Save workspace"
)



#Checking if the user actually selected a valid folder path and save location
if folder_path and save_location:
    
    #Creating the code-workspace file in the save location
    folder_name = os.path.basename(folder_path)
    filepath = os.path.join(save_location, folder_name + ".code-workspace")
    with open(filepath, "w") as f:
        content = '{"folders": [{"path": "' + folder_path + '"}],"settings": {}}'
        f.write(content)

    
    #Creating the shortcut on the desktop
    desktop = winshell.desktop()
    path = os.path.join(desktop, folder_name + ".lnk")
    target = filepath
    wDir = save_location
    icon = icopath
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
else :
    #Showing a warning if the user didn't select valid workspace folder and save location
    messagebox.showwarning(title="Warning", message="Error while selecting folders")