import os

folder_name = "demo1"
if os.path.exists(folder_name):
    print("Folder is present")
else:
    print("Folder not present")
