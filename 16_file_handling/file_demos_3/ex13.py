import os

file_names = ["a.txt", "b.txt", "c.txt"]
for file in file_names:
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} deleted")
