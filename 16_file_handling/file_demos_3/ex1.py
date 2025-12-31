import os

file_name = "data.txt"
if os.path.exists(file_name):
    print("File is present")
else:
    print("File not present")
