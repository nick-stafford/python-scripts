# batch rename photos with date prefix
import os
from datetime import datetime

folder = input("Enter folder path: ")

for f in os.listdir(folder):
    if f.endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(folder, f)
        mtime = os.path.getmtime(path)
        date = datetime.fromtimestamp(mtime).strftime('%Y%m%d')
        new_name = f"{date}_{f}"
        print(f"{f} -> {new_name}")
        # os.rename(path, os.path.join(folder, new_name))
