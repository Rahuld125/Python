f = None
try:
    f = open("message.txt", "w")
    print("Type something and to stop press ENTER")
    lines = 0
    while True:
        text = input()
        if text == "":
            break
        f.write(text + "\n")
        lines += 1
    print("Total lines saved in file:", lines)
except FileNotFoundError as ex1:
    print("Could not open the file", ex1)
except OSError as ex2:
    print("Error in writing the file", ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
