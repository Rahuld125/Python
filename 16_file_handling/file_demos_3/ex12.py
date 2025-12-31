import os

if os.path.exists("data.txt"):
    if os.path.isfile("data.txt"):
        os.remove("data.txt")
        print("File deleted")
    else:
        print("It is not a file")
else:
    print("File not present")
