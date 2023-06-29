# backup important files to external drive
import shutil
import os
from datetime import datetime

source_dirs = [
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Desktop"),
]

backup_drive = "E:/Backup"  # change this

def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for src in source_dirs:
        if os.path.exists(src):
            dest = os.path.join(backup_drive, timestamp, os.path.basename(src))
            print(f"Backing up {src}...")
            # shutil.copytree(src, dest)
    print("Done")

# backup()
