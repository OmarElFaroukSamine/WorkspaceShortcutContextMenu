import os
import sys
import tkinter as tk
from tkinter import filedialog,  messagebox
import pyshortcuts
from win32com.client import Dispatch
from pathlib import Path

root = tk.Tk()
root.withdraw()

cpath = Path(sys.argv[0]).resolve().parent
icopath = cpath.parent / "data" / "icon.ico"

root.iconbitmap(icopath)

folder_path = filedialog.askdirectory(
    initialdir="/",
    title="Select workspace folder"
)

save_location = filedialog.askdirectory(
    initialdir="/",
    title="Save workspace"
)

if folder_path and save_location:
    folder_name = os.path.basename(folder_path)
    filepath = os.path.join(save_location, folder_name + ".code-workspace")

    with open(filepath, "w") as f:
        content = '{"folders": [{"path": "' + folder_path + '"}],"settings": {}}'
        f.write(content)

    shortcut_name = folder_name
    pyshortcuts.make_shortcut(
        filepath,
        name=shortcut_name,
        icon=str(icopath),
        folder=None
    )
else :
    messagebox.showwarning(title="Warning", message="Error while selecting folders")
