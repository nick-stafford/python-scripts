# quick script to organize downloads folder
# TODO: add more file types

import os
import shutil

downloads = os.path.expanduser("~/Downloads")

extensions = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.xlsx': 'Excel',
    '.docx': 'Docs'
}

for file in os.listdir(downloads):
    ext = os.path.splitext(file)[1].lower()
    if ext in extensions:
        dest = os.path.join(downloads, extensions[ext])
        if not os.path.exists(dest):
            os.makedirs(dest)
        # shutil.move(os.path.join(downloads, file), dest)
        print(f"Would move {file} to {extensions[ext]}")
