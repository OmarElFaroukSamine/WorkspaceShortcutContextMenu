import json
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(
    initialdir="/",
    title="Select a Folder"
)

if folder_path:
    desktop = os.path.expanduser("~/Desktop")
    folder_name = os.path.basename(folder_path)
    f = open(desktop + "/"+folder_name+".code-workspace","w")
    content = "{\"folders\": [{\"path\": \"" + folder_path + "\"}],\"settings\": {}}"
    f.write(str(content));
    f.close()
else:
    print("No folder selected.")