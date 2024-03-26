import os
import tkinter as tk
from tkinter import filedialog
from pyshortcuts import make_shortcut
from pathlib import Path

root = tk.Tk()
root.withdraw()

cpath = str(Path.cwd())
icopath = cpath + r"\\data\\icon.ico"

root.iconbitmap(icopath)

folder_path = filedialog.askdirectory(
    initialdir="/",
    title="Select a Folder"
)

save_location = filedialog.askdirectory(
    initialdir="/",
    title="Select where you want this workspace to be saved"
)

if folder_path:
    folder_name = os.path.basename(folder_path)
    filepath = os.path.join(save_location, folder_name + ".code-workspace")

    with open(filepath, "w") as f:
        content = '{"folders": [{"path": "' + folder_path + '"}],"settings": {}}'
        f.write(content)

    shortcut_name = folder_name
    make_shortcut(
        filepath,
        name=shortcut_name,
        icon=icopath,
        folder=None
    )

else:
    print("No folder selected.")
