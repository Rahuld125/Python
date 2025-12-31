f = None
try:
    f = open("message.txt", "r")
    lines = 0
    for text in f:
        print(text, end="")
        lines += 1
    print("Total lines read:", lines)
except FileNotFoundError as ex1:
    print("Cannot open the file", ex1)
except OSError as ex2:
    print("Error in reading the file", ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
