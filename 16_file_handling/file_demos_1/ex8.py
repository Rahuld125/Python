f = None
try:
    f = open("data.txt", "r")
    text = f.read()
    print(text)
except FileNotFoundError as ex1:
    print("Could not open the file", ex1)
finally:
    if f is not None:
        f.close()
        print("File closed Successfully!!")
