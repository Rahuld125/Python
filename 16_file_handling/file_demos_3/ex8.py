import os

old_file = "data.txt"
new_file = "secret.txt"
if os.path.exists(old_file):
    if not os.path.exists(new_file):
        os.rename(old_file, new_file)
        print("File renamed successfully")
    else:
        print(f"A file by the name {new_file} already exists")
else:
    print(f"The file {old_file} does not exists")
